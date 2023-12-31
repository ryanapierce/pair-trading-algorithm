from datetime import date
import web_scraper
from helper_methods import EXPECTED_DF_LEN, DATE_RANGE,  TRAINING_DATE_RANGE, create_stock_cointegration_table, drop_stock_cointegration_table, drop_stock_prices_table, create_stock_price_table, find_cointegrated_pairs, get_stock_prices_from_db, insert_stock_coint_pairs_to_db, insert_stock_records_to_db
import pandas as pd


def seed_stock_info() -> None:
    """
    Orchestrates web scraping of stock symbols from StockAnalysis. 
    Creation the database table,
    Insertion of the relevant yfinance stock ticker information for each stock.

    Parameters:
        None
    Returns:
        None
    """
    start_date, end_date = DATE_RANGE
    stocks_with_sectors = web_scraper.scrape_stock_symbols()

    drop_stock_prices_table()
    create_stock_price_table()

    count = 1
    for obj in stocks_with_sectors:
        stock_tickers, sector = obj['stock_symbols'], obj['sector']
        for ticker in stock_tickers:
            print(f'Inserting Records for {ticker}. Current Count: {count}')
            insert_stock_records_to_db(ticker, sector, start_date, end_date)
            count += 1


def seed_stock_coint_pairs() -> None:
    """
    Orchestrates creation the database table.
    Manipulates the DataFrame representation of the stock_prices db table to be analyzed.
    Analyzes cointegration for same sector stocks.
    Inserts cointegrated values into the db.

    Parameters:
        None
    Returns:
        None
    """
    drop_stock_cointegration_table()
    create_stock_cointegration_table()

    full_date_range_df = get_stock_prices_from_db().groupby("ticker").filter(
        lambda x: len(x) == EXPECTED_DF_LEN).reset_index()

    start_date = date(*[int(n) for n in TRAINING_DATE_RANGE[0].split('-')])
    end_date = date(*[int(n) for n in TRAINING_DATE_RANGE[1].split('-')])
    training_df = full_date_range_df[(full_date_range_df['date'] >= start_date) & (
        full_date_range_df['date'] <= end_date)]

    training_full_date_range_df = training_df.groupby("ticker").filter(
        lambda x: len(x) == 756)

    training_prices_df = training_full_date_range_df.groupby("ticker")["price"]\
        .apply(lambda x: pd.Series(x.values))\
        .unstack()\
        .reset_index()\

    training_price_series_df = pd.DataFrame(
        data=training_prices_df.iloc[:, 1:].to_numpy(
        ).T, columns=training_prices_df.iloc[:, 0].to_numpy()
    )

    def get_stock_name_by_sector(
        sec): return training_full_date_range_df[training_full_date_range_df['sector'] == sec]['ticker'].unique()

    for sector in ['technology', 'healthcare', 'industrials']:
        sector_stocks_names = get_stock_name_by_sector(sector)
        sector_coint_pairs = find_cointegrated_pairs(
            training_price_series_df, sector_stocks_names, sector)
        insert_stock_coint_pairs_to_db(sector_coint_pairs)


def main() -> None:
    """
    Orchestrates program flow.

    Parameters:
        None
    Returns:
        None
    """
    print('CAUTION: Both scraping functions are commented out, calling these functions will alter the state of the database.')
    # seed_stock_info()
    # seed_stock_coint_pairs()


if __name__ == '__main__':
    main()
