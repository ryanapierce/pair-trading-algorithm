import requests
from bs4 import BeautifulSoup

sector_pages = [
    {'url': 'https://stockanalysis.com/stocks/sector/healthcare/', 'sector': 'healthcare'},
    {'url': 'https://stockanalysis.com/stocks/sector/industrials/',
        'sector': 'industrials'},
    {'url': 'https://stockanalysis.com/stocks/sector/technology/', 'sector': 'technology'},
]


def scrape_stock_symbols(arr=sector_pages, top_n=100):
    stock_list = []
    for d in arr:
        url, sector = d['url'], d['sector']
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        main_table = soup.find(id='main-table')
        rows = main_table.find_all("td", class_="sym svelte-1tv1ofl")[:top_n]
        stock_symbols = list(map(lambda x: x.a.text, rows))
        stock_list.append({'stock_symbols': stock_symbols, 'sector': sector})
    return stock_list
