from typing import List
from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np
import psycopg2
import yfinance as yf
from statsmodels.tsa.stattools import adfuller, coint
import datetime


load_dotenv()
DB_URL = os.getenv("DB_CONNECTION_STRING")
EXPECTED_DF_LEN = 1006
TRAINING_DATE_RANGE = ("2019-08-31", "2022-08-31")
TESTING_DATE_RANGE = ("2022-09-01", "2023-08-31")
DATE_RANGE = ("2019-08-31", "2023-08-31")
# The percentage of data that we will be contained within our z_score band
TARGET_THRESHOLD = 0.8
CURRENT_WINDOW = 10  # The number of days used to calculate the current mean
HISTORIC_WINDOW = 30  # The number of days used to calculate the historic mean

# Database Management


def get_stock_prices(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    takes a ticker, start date, and end date. Returns a dataframe
    of the stock prices from yfinance.

    Parameters:
        ticker (str): the stock symbol
        start_date (str): the start date of the date range, use date format YYYY-MM-DD
        end_date (str): the end date of the date range, use date format YYYY-MM-DD

    Returns:
        prices_df (pd.DataFrame): returns a dataframe of the stock prices from yfinance
    """
    prices_df = yf.Ticker(ticker).history(
        start=start_date, end=end_date, raise_errors=True
    )
    prices_df["Ticker"] = ticker
    return prices_df


def test_stock_cointegration(stock_one: pd.Series, stock_two: pd.Series) -> tuple:
    """
    takes two pandas series of stock prices and returns a tuple of a
    boolean indicating if the p_value was significant and a tuple of
    results from the statsmodel cointegration test.

    The Null hypothesis is that there is no cointegration,
    the alternative hypothesis is that there is cointegrating relationship.
    If the pvalue is small, below a critical size, then we can reject the
    hypothesis that there is no cointegrating relationship.

    Parameters:
        stock_one (pd.Series): 1st pandas series of stock prices to compare cointegration
        stock_two (pd.Series): 2nd pandas series of stock prices to compare cointegration
    Returns:
        tuple
    """
    res = coint(stock_one, stock_two)
    p_value = res[1]
    signifigance_level = 0.05
    return p_value < signifigance_level, res


def adf_test(series: pd.Series) -> tuple:
    """
    takes a pandas series of stock prices and returns a tuple of a
    boolean indicating if the p_value was significant and a tuple of
    results from the statsmodel adfuller stationarity test.

    The null hypothesis of the Augmented Dickey-Fuller is
    that there is a unit root, with the alternative that
    there is no unit root. If the pvalue is above a critical
    size, then we cannot reject that there is a unit root.

    Parameters:
        series (pd.Series): Pandas series of stock prices to test for stationarity
    Returns:
        tuple
    """

    res = adfuller(series)
    p_value = res[1]
    signifigance_level = 0.05
    return p_value < signifigance_level, res


def connect_with_database() -> psycopg2.extensions.connection:
    """
    this function connects to the database and returns a connection to the database

    Parameters:
        None
    Returns:
        psycopg2.extensions.connection: returns a connection to the database
    """
    db_connection = psycopg2.connect(DB_URL)
    return db_connection


def sql_execution_wrapper(sql_statement: str) -> None:
    """
    this is a wrapper function to handle the execution of sql statements.
    It will connect to the database.
    Execute the sql statement.
    Commit the changes.
    Then close the connection.

    Parameters:
        sql_statement (str): the sql statement to execute
    Returns:
        psycopg2.extensions.connection: returns a connection to the database
    """
    conn = connect_with_database()
    cur = conn.cursor()

    cur.execute(sql_statement)

    conn.commit()
    cur.close()
    conn.close()


def create_stock_price_table() -> None:
    """
    This function creates the stock_prices table in the database if it does not exist.

    Parameters:
        None
    Returns:
        None
    """
    sql_query = """
                CREATE TABLE IF NOT EXISTS stock_prices(
                    id SERIAL PRIMARY KEY,
                    ticker VARCHAR(20) NOT NULL,
                    sector VARCHAR(20) NOT NULL,
                    price FLOAT(8) NOT NULL,
                    date DATE NOT NULL,
                    UNIQUE(ticker, date)
                );
                """
    sql_execution_wrapper(sql_query)


def drop_stock_cointegration_table() -> None:
    """
    This function deletes the stock_cointegrations table in the database if it exists.

    Parameters:
        None
    Returns:
        None
    """
    sql_query = """DROP TABLE IF EXISTS stock_cointegrations;"""
    sql_execution_wrapper(sql_query)


def create_stock_cointegration_table() -> None:
    """
    This function creates the stock_cointegrations table in the database if it does not exist.

    Parameters:
        None
    Returns:
        None
    """
    sql_query = """
                CREATE TABLE IF NOT EXISTS stock_cointegrations(
                    id SERIAL PRIMARY KEY,
                    stock_one VARCHAR(20) NOT NULL,
                    stock_two VARCHAR(20) NOT NULL,
                    pvalue FLOAT(8) NOT NULL,
                    sector VARCHAR(20) NOT NULL,
                    ratio_stationarity FLOAT(8) NOT NULL,
                    UNIQUE(stock_one, stock_two)         
                );
                """
    sql_execution_wrapper(sql_query)


def insert_stock_coint_pairs_to_db(stock_pairs_list: List[List]) -> None:
    """
    Takes list of lists from the find_cointegrated_pairs
    function and inserts them into the database into
    the stock_cointegrations table.

    Parameters:
        stock_pairs_list (List[List]): a list of lists of stock pairs
                                       that are cointegrated. each list contains
                                       first stock, second stock, p_value for cointegration,
                                       sector, and p_value for stationarity
    Returns:
        None
    """
    insert_stmt = ",".join(
        [
            f"('{stock_one}', '{stock_two}', {pvalue}, '{sector}',{ratio_stationarity})"
            for stock_one, stock_two, pvalue, sector, ratio_stationarity in stock_pairs_list
        ]
    )

    sql_query = f"""
                    INSERT INTO public.stock_cointegrations(stock_one, stock_two, pvalue, sector, ratio_stationarity)
                    VALUES {insert_stmt};
                    """
    sql_execution_wrapper(sql_query)


def drop_stock_prices_table() -> None:
    """
    This function deletes the stock_prices table in the database if it exists.

    Parameters:
        None
    Returns:
        None
    """
    sql_query = """DROP TABLE IF EXISTS stock_prices;"""
    sql_execution_wrapper(sql_query)


def find_cointegrated_pairs(
    df: pd.DataFrame, tickers: List[str], sector: str
) -> List[tuple]:
    """
    takes a dataframe of stock prices, a list of stock symbols, and a sector.
    Then runs a cointegration test on each pair of stocks.
    If the p_value is significant, then it will also conduct an
    adfuller test on the ratio of the two stocks. To prevent duplicates,
    a set is used to keep track of the stock pairs that have already been tested.
    The stocks are sorted alphabetically and then joined with a comma to create a string.
    If the combination is new. It will be appended to the list that is returned by the function,
    as a list containing:
        first stock, second stock, p_value for cointegration, sector, p_value for stationarity

    Parameters:
        df (pd.DataFrame): dataframe of stock prices
        tickers (List[str]): list of stock symbols
        sector (str): the sector the tickers list of stocks belongs to
    Returns:
        List[List]: returns a list of list of stock pairs that are cointegrated
    """
    unique_pairs = set()
    pairs = []
    for t1 in tickers:
        for t2 in tickers:
            if t1 == t2:
                continue
            does_cointegrate, res = test_stock_cointegration(df[t1], df[t2])
            if not does_cointegrate:
                continue
            str_stock_pair = ",".join(list(sorted([t1, t2])))
            curr_len = len(unique_pairs)
            unique_pairs.add(str_stock_pair)
            if len(unique_pairs) != curr_len:
                ratio_stationarity = adf_test(df[t1] / df[t2])[1][1]
                coint_pair = [
                    *list(sorted([t1, t2])),
                    f"{round(res[1], 5)}",
                    sector,
                    f"{round(ratio_stationarity, 5)}",
                ]
                print(coint_pair)
                pairs.append(coint_pair)
    return pairs


def insert_stock_records_to_db(
    ticker: str, sector: str, start_date: str, end_date: str
) -> None:
    """
    Orchestrates the insertion of stock prices into the database.
    Provides a warning if the data is not the expected length.
    If there is an issue while trying to insert the data, it will print to the console.

    Parameters:
        ticker (str): stock symbol
        sector (str): sector the stock belongs to
        start_date (str): the start date, use date format YYYY-MM-DD
        end_date (str): the end date, use date format YYYY-MM-DD
    Returns:
        None
    """
    try:
        df = get_stock_prices(ticker, start_date, end_date).reset_index()
        if len(df) != EXPECTED_DF_LEN:
            print(
                f"{ticker} in sector {sector}, does not contain the expected number of rows: {len(df)}"
            )
        df["sql_insert"] = df["Date"].dt.strftime("%Y-%m-%d")
        df["sql_insert"] = (
            "("
            + round(df["Close"], 2).astype(str)
            + ",'"
            + df["Ticker"]
            + "','"
            + df["sql_insert"]
            + "','"
            + sector
            + "')"
        )
        insert_string = ",\n".join(df["sql_insert"].array)
        sql_query = f"""
                    INSERT INTO public.stock_prices(price, ticker, date, sector)
                    VALUES {insert_string};
                    """
        sql_execution_wrapper(sql_query)
    except Exception:
        print(
            f"Unable to find Stock Data for {ticker} in sector {sector}, skipping this entry"
        )


def get_stock_prices_from_db() -> pd.DataFrame:
    """
    returns a dataframe of the stock_prices table

    Parameters:
        None
    Returns:
        pd.DataFrame: returns a dataframe of the stock_prices table
    """
    return pd.read_sql_query("SELECT * FROM public.stock_prices", DB_URL)


def get_stock_coint_pairs_from_db() -> pd.DataFrame:
    """
    returns a dataframe of the stock_cointegrations table

    Parameters:
        None
    Returns:
        pd.DataFrame: returns a dataframe of the stock_prices table
    """
    return pd.read_sql_query("SELECT * FROM public.stock_cointegrations", DB_URL)


# Signal Research


def trade_threshold(data):
    # Find a z_score upper and lower bound such that the lower bound is negative of the upper bound
    # Our goal is that as close to this proportion of data will be inside our threshold
    target_threshold = TARGET_THRESHOLD
    z_scores = data.dropna().values
    # Because our tails won't exactly be symmetrical, we will have a margin or error of 5%
    desired_percentage_range = (target_threshold - 0.05, target_threshold + 0.05)
    tolerance = 0.01
    estimate = np.median(z_scores)
    # Iterate through
    while True:
        # Calculate the bounds around the estimate
        lower_bound = -estimate
        upper_bound = estimate
        # Calculate the percentage of data within the bounds
        percentage_within_bounds = np.mean(
            (data >= lower_bound) & (data <= upper_bound)
        )
        # Check if the percentage is within the desired range
        if (
            desired_percentage_range[0]
            <= percentage_within_bounds
            <= desired_percentage_range[1]
        ):
            break  # Estimate is within the desired range
        # Adjust the estimate based on the percentage
        if percentage_within_bounds < target_threshold:
            estimate += tolerance  # Increase the estimate
        else:
            estimate -= tolerance  # Decrease the estimate
    return estimate


def mvg_avg_z_score(data):
    # 10 day moving avg represents our current mean
    current_mvg_avg = data.rolling(window=CURRENT_WINDOW).mean()

    # 30 day moving avg represents our historical mean
    historic_mvg_avg = data.rolling(window=HISTORIC_WINDOW).mean()
    historic_std = data.rolling(window=HISTORIC_WINDOW).std()

    # Calculate z-score for difference between current and historical mean
    z_score_currvshist = (current_mvg_avg - historic_mvg_avg) / historic_std

    return z_score_currvshist


def trade_signals(data, train_data):
    signal_threshold = trade_threshold(
        mvg_avg_z_score(train_data)
    )  # Z_score threshold to trade
    stop_threshold = 1.32  # Z_score threshold to stop strategy
    trades = data.copy()
    # when the z-score is above 1, sell the spread
    trades[mvg_avg_z_score(data) > signal_threshold] = -1
    # when the z-score is below -1, buy the spread
    trades[mvg_avg_z_score(data) < -signal_threshold] = 1
    trades[
        (mvg_avg_z_score(data) >= -signal_threshold)
        & (mvg_avg_z_score(data) <= signal_threshold)
        | np.isnan(mvg_avg_z_score(data))
    ] = 0  # otherwise, do nothing

    # stop the strategy if we cross a certain threshold
    stop_condition = (mvg_avg_z_score(data) > stop_threshold) | (
        mvg_avg_z_score(data) < -stop_threshold
    )
    stop_index = stop_condition.idxmax() if stop_condition.any() else None
    if not pd.isnull(stop_index):
        # If our trade signal is 100, that means we stop our strategy
        trades[stop_index:] = 100
    return trades


def trade_signals_no_stop_loss(data, train_data):
    signal_threshold = trade_threshold(
        mvg_avg_z_score(train_data)
    )  # Z_score threshold to trade
    # stop_threshold = 1.32 # Z_score threshold to stop strategy
    stop_threshold = 99
    trades = data.copy()
    # when the z-score is above 1, sell the spread
    trades[mvg_avg_z_score(data) > signal_threshold] = -1
    # when the z-score is below -1, buy the spread
    trades[mvg_avg_z_score(data) < -signal_threshold] = 1
    trades[
        (mvg_avg_z_score(data) >= -signal_threshold)
        & (mvg_avg_z_score(data) <= signal_threshold)
        | np.isnan(mvg_avg_z_score(data))
    ] = 0  # otherwise, do nothing

    # stop the strategy if we cross a certain threshold
    stop_condition = (mvg_avg_z_score(data) > stop_threshold) | (
        mvg_avg_z_score(data) < -stop_threshold
    )
    stop_index = stop_condition.idxmax() if stop_condition.any() else None
    if not pd.isnull(stop_index):
        # If our trade signal is 100, that means we stop our strategy
        trades[stop_index:] = 100
    return trades


def calculate_profit(stock_1, stock_2, data, train_data):
    trades = trade_signals(data, train_data)

    daily_profits = pd.DataFrame(index=trades.index, columns=["Profit"])
    daily_profits["Profit"] = 0.0  # Initialize daily profits to zero
    daily_profits["Position_Stock_1"] = 0.0  # Initialize positions to zero
    daily_profits["Position_Stock_2"] = 0.0  # Initialize positions to zero

    balance = 0  # Initial balance of 0
    position_stock_1 = 0
    position_stock_2 = 0
    next_day_position_stock_1 = 0
    next_day_position_stock_2 = 0
    investment_per_stock = 100  # $100 to invest in each stock

    # Simulate the trading strategy and calculate daily profits
    for date in trades.index:
        trade_signal = trades.loc[date]

        # Calculate the number of shares to buy/sell
        stock_1_shares = investment_per_stock / stock_1.loc[date]
        stock_2_shares = investment_per_stock / stock_2.loc[date]

        if trade_signal == -1:
            # Short $100 of stock_1 and long $100 of stock_2
            next_day_position_stock_1 -= stock_1_shares
            next_day_position_stock_2 += stock_2_shares
        elif trade_signal == 1:
            # Long $100 of stock_1 and short $100 of stock_2
            next_day_position_stock_1 += stock_1_shares
            next_day_position_stock_2 -= stock_2_shares
        elif trade_signal == 100:
            # If trade_signal is 100, immediately close all positions
            break

        # Calculate the daily profit based on positions and stock price changes
        daily_profit_stock_1 = position_stock_1 * (
            stock_1.loc[date] - stock_1.shift(1).loc[date]
        )
        daily_profit_stock_2 = position_stock_2 * (
            stock_2.loc[date] - stock_2.shift(1).loc[date]
        )
        daily_profit = daily_profit_stock_1 + daily_profit_stock_2

        # Update the balance with daily profit
        if not np.isnan(daily_profit):
            balance += daily_profit

        # Update the daily profit and positions in the DataFrame
        daily_profits.loc[date, "Profit"] = float(daily_profit)
        daily_profits.loc[date, "Position_Stock_1"] = float(position_stock_1)
        daily_profits.loc[date, "Position_Stock_2"] = float(position_stock_2)
        daily_profits.loc[date, "Cumulative Profit"] = balance

        # Update positions for the next day
        position_stock_1 = next_day_position_stock_1
        position_stock_2 = next_day_position_stock_2
    # Close positions at stop threshold or after time period ends
    return (balance, daily_profits)


def calculate_profit_no_stop_loss(stock_1, stock_2, data, train_data):
    trades = trade_signals_no_stop_loss(data, train_data)

    daily_profits = pd.DataFrame(index=trades.index, columns=["Profit"])
    daily_profits["Profit"] = 0.0  # Initialize daily profits to zero
    daily_profits["Position_Stock_1"] = 0.0  # Initialize positions to zero
    daily_profits["Position_Stock_2"] = 0.0  # Initialize positions to zero

    balance = 0  # Initial balance of 0
    position_stock_1 = 0
    position_stock_2 = 0
    next_day_position_stock_1 = 0
    next_day_position_stock_2 = 0
    investment_per_stock = 100  # $100 to invest in each stock

    # Simulate the trading strategy and calculate daily profits
    for date in trades.index:
        trade_signal = trades.loc[date]

        # Calculate the number of shares to buy/sell
        stock_1_shares = investment_per_stock / stock_1.loc[date]
        stock_2_shares = investment_per_stock / stock_2.loc[date]

        if trade_signal == -1:
            # Short $100 of stock_1 and long $100 of stock_2
            next_day_position_stock_1 -= stock_1_shares
            next_day_position_stock_2 += stock_2_shares
        elif trade_signal == 1:
            # Long $100 of stock_1 and short $100 of stock_2
            next_day_position_stock_1 += stock_1_shares
            next_day_position_stock_2 -= stock_2_shares
        elif trade_signal == 100:
            # If trade_signal is 100, immediately close all positions
            break

        # Calculate the daily profit based on positions and stock price changes
        daily_profit_stock_1 = position_stock_1 * (
            stock_1.loc[date] - stock_1.shift(1).loc[date]
        )
        daily_profit_stock_2 = position_stock_2 * (
            stock_2.loc[date] - stock_2.shift(1).loc[date]
        )
        daily_profit = daily_profit_stock_1 + daily_profit_stock_2

        # Update the balance with daily profit
        if not np.isnan(daily_profit):
            balance += daily_profit

        # Update the daily profit and positions in the DataFrame
        daily_profits.loc[date, "Profit"] = float(daily_profit)
        daily_profits.loc[date, "Position_Stock_1"] = float(position_stock_1)
        daily_profits.loc[date, "Position_Stock_2"] = float(position_stock_2)
        daily_profits.loc[date, "Cumulative Profit"] = balance

        # Update positions for the next day
        position_stock_1 = next_day_position_stock_1
        position_stock_2 = next_day_position_stock_2
    # Close positions at stop threshold or after time period ends
    return (balance, daily_profits)


def calculate_sp500_investment_returns(TESTING_DATE_RANGE, initial_investment):
    # Define the SPX ticker symbol for S&P 500
    spx_ticker = "^SPX"

    # Convert date strings to datetime objects
    start_date = datetime.datetime.strptime(TESTING_DATE_RANGE[0], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(TESTING_DATE_RANGE[1], "%Y-%m-%d")

    # Download historical data for SPX
    sp500 = yf.download(spx_ticker, start=start_date, end=end_date)

    # Calculate daily returns
    sp500["Daily_Return"] = sp500["Adj Close"].pct_change()

    # Calculate the cumulative returns
    sp500["Cumulative_Returns"] = (1 + sp500["Daily_Return"]).cumprod()

    # Calculate the portfolio value
    sp500["Portfolio_Value"] = initial_investment * sp500["Cumulative_Returns"]

    # Calculate the profit
    sp500["Profit"] = sp500["Portfolio_Value"] - initial_investment

    return sp500
