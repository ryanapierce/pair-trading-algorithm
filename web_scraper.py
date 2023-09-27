from typing import List, Dict
import requests
from bs4 import BeautifulSoup

sector_pages = [
    {'url': 'https://stockanalysis.com/stocks/sector/healthcare/', 'sector': 'healthcare'},
    {'url': 'https://stockanalysis.com/stocks/sector/industrials/',
        'sector': 'industrials'},
    {'url': 'https://stockanalysis.com/stocks/sector/technology/', 'sector': 'technology'},
]


def scrape_stock_symbols(arr: List[Dict[str, str]] = sector_pages, top_n: int = 100) -> List[Dict[List[str], str]]:
    """
    Orchestrates scraping of StockAnalysis.
    Takes a list of pages to scrape.
    Utilizes requests lib to send GET Requests to the pages.
    Parses response with beautifulsoup4.
    Extracts the stock symbols

    Parameters:
        arr (List[Dict[str, str]]): = sector_pages this is the list of dictionaries, 
                                    the keys of each dictionary are the 
                                    url to scrape and the sector
        top_n (int): this is the number of tickers the function should scrape

    Returns:
        List[Dict[List[str], str]]: returns a list of dictionaries, the keys of each dictionary are the 
                                    stock symbols and the sector
    """
    stocks = []
    for d in arr:
        url, sector = d['url'], d['sector']
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        main_table = soup.find(id='main-table')
        rows = main_table.find_all("td", class_="sym svelte-1tv1ofl")[:top_n]
        stock_symbols = list(map(lambda x: x.a.text, rows))
        stocks.append({'stock_symbols': stock_symbols, 'sector': sector})
    return stocks
