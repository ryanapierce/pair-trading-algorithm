import web_scraper
from helper_methods import EXPECTED_DF_LEN, create_stock_cointegration_table, drop_stock_cointegration_table, drop_stock_prices_table, create_stock_price_table, find_cointegrated_pairs, get_stock_prices_from_db, insert_stock_coint_pairs_to_db, insert_stock_records_to_db
import pandas as pd


def seed_stock_info():
    START_DATE = '2019-08-31'
    END_DATE = '2023-08-31'

    stocks_with_sectors = web_scraper.scrape_stock_symbols()

    drop_stock_prices_table()
    create_stock_price_table()

    count = 1
    for obj in stocks_with_sectors:
        stock_tickers, sector = obj['stock_symbols'], obj['sector']
        for ticker in stock_tickers:
            print(f'Inserting Records for {ticker}. Current Count: {count}')
            insert_stock_records_to_db(ticker, sector, START_DATE, END_DATE)
            count += 1


def seed_stock_coint_pairs():
    drop_stock_cointegration_table()
    create_stock_cointegration_table()

    df = get_stock_prices_from_db()
    full_date_range_df = df.groupby("ticker").filter(
        lambda x: len(x) == EXPECTED_DF_LEN)
    prices_df = full_date_range_df.groupby("ticker")["price"]\
        .apply(lambda x: pd.Series(x.values))\
        .unstack()\
        .reset_index()\

    price_series_df = pd.DataFrame(
        data=prices_df.iloc[:, 1:].to_numpy(
        ).T, columns=prices_df.iloc[:, 0].to_numpy()
    )

    def get_stock_name_by_sector(
        sec): return full_date_range_df[full_date_range_df['sector'] == sec]['ticker'].unique()

    tech_stocks = get_stock_name_by_sector('technology')

    tech_coint_pairs_set = find_cointegrated_pairs(
        price_series_df, tech_stocks, 'technology')
    insert_stock_coint_pairs_to_db(tech_coint_pairs_set)
    healthcare_stocks = get_stock_name_by_sector('healthcare')
    healthcare_coint_pairs_set = find_cointegrated_pairs(
        price_series_df, healthcare_stocks, 'healthcare')
    insert_stock_coint_pairs_to_db(healthcare_coint_pairs_set)
    industrials_stocks = get_stock_name_by_sector('industrials')
    industrials_coint_pairs_set = find_cointegrated_pairs(
        price_series_df, industrials_stocks, 'industrials')
    insert_stock_coint_pairs_to_db(industrials_coint_pairs_set)
