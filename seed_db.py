# import web_scraper
# from helper_methods import drop_stock_prices_table, create_stock_price_table, insert_stock_records_to_db

# START_DATE = '2019-08-31'
# END_DATE = '2023-08-31'

# stocks_with_sectors = web_scraper.scrape_stock_symbols()

# drop_stock_prices_table()
# create_stock_price_table()

# count = 1
# for obj in stocks_with_sectors:
#     stock_tickers, sector = obj['stock_symbols'], obj['sector']
#     for ticker in stock_tickers:
#         print(f'Inserting Records for {ticker}. Current Count: {count}')
#         insert_stock_records_to_db(ticker, sector, START_DATE, END_DATE)
#         count += 1
