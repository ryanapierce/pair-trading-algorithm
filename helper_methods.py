from dotenv import load_dotenv
import os
import pandas as pd
import psycopg2
import yfinance
from statsmodels.tsa.stattools import adfuller, coint
load_dotenv()
DB_URL = os.getenv('DB_CONNECTION_STRING')


def get_stock_prices(ticker, start_date, end_date):
    # use date format YYYY-MM-DD
    prices_df = yfinance.Ticker(ticker).history(
        start=start_date, end=end_date)
    prices_df['Ticker'] = ticker
    return prices_df


def test_stock_cointegration(stock_one, stock_two):
    # The Null hypothesis is that there is no cointegration,
    # the alternative hypothesis is that there is cointegrating relationship.
    # If the pvalue is small, below a critical size, then we can reject the
    # hypothesis that there is no cointegrating relationship.
    res = coint(stock_one, stock_two)
    p_value = res[1]
    signifigance_level = .05
    return p_value < signifigance_level


def adf_test(series):
    # The null hypothesis of the Augmented Dickey-Fuller is
    # that there is a unit root, with the alternative that
    # there is no unit root. If the pvalue is above a critical
    # size, then we cannot reject that there is a unit root.
    res = adfuller(series)
    p_value = res[1]
    signifigance_level = .05
    return p_value < signifigance_level


def connect_with_database():
    db_connection = psycopg2.connect(DB_URL)
    return db_connection


def sql_execution_wrapper(sql_statement):
    conn = connect_with_database()
    cur = conn.cursor()

    cur.execute(sql_statement)

    conn.commit()
    cur.close()
    conn.close()


def create_stock_price_table():
    sql_query = """
                CREATE TABLE IF NOT EXISTS stock_prices(
                    id SERIAL PRIMARY KEY,
                    ticker VARCHAR(10) NOT NULL,
                    price FLOAT(8) NOT NULL,
                    date DATE NOT NULL,
                    UNIQUE(ticker, date)
                );
                """
    sql_execution_wrapper(sql_query)


def drop_stock_prices_table():
    sql_query = """DROP TABLE stock_prices;"""
    sql_execution_wrapper(sql_query)


def insert_df_records_to_db(df):
    new_df = df[['Date', 'Close', 'Ticker']].copy()

    new_df['sql_insert'] = new_df['Date'].dt.strftime('%Y-%m-%d')
    new_df['sql_insert'] = '(' + round(new_df['Close'], 2).astype(str) + ',\'' + \
        new_df['Ticker'] + '\',\'' + new_df['sql_insert'] + '\')'

    insert_string = ',\n'.join(new_df['sql_insert'].array)
    sql_query = f"""
                INSERT INTO public.stock_prices(price, ticker, date)
                VALUES {insert_string};
                """
    sql_execution_wrapper(sql_query)


def get_stock_prices_from_db():
    return pd.read_sql_query('SELECT * FROM public.stock_prices', DB_URL)
