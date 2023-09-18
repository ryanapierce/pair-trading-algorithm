import yfinance
from statsmodels.tsa.stattools import adfuller, coint


# use date format YYYY-MM-DD
def get_stock_prices(ticker, start_date, end_date):
    prices_df = yfinance.Ticker(ticker).history(
        start=start_date, end=end_date)
    prices_df['Ticker'] = ticker
    return prices_df

# The Null hypothesis is that there is no cointegration,
# the alternative hypothesis is that there is cointegrating relationship.
# If the pvalue is small, below a critical size, then we can reject the
# hypothesis that there is no cointegrating relationship.


def test_stock_cointegration(stock_one, stock_two):
    res = coint(stock_one, stock_two)
    p_value = res[1]
    signifigance_level = .05
    return p_value < signifigance_level


# The null hypothesis of the Augmented Dickey-Fuller is
# that there is a unit root, with the alternative that
# there is no unit root. If the pvalue is above a critical
# size, then we cannot reject that there is a unit root.


def adf_test(series):
    res = adfuller(series)
    p_value = res[1]
    signifigance_level = .05
    return p_value < signifigance_level
