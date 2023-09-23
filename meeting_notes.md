# 09/18/2023

- Vincent has been having issues getting data from yfinance
  - troubleshooting
- Needs dataframe

- Pick 3 stock sectors

  - we will pick the top 100 out of these
  - Date Range: 08/31/2019 - 08/31/2023
  - Healthcare
  - Industrials
  - Technology
  - will pull from: https://stockanalysis.com/stocks/industry/sectors/

- Vincent thinking about doing p-ratios for testing mean reversion
- engel grainger tests for mean reversion

- we will use the closing price for stock prices
- Which Risk free rate do we want to use?
  - we will use the 5 year T-bill
- What moving average time frame are we going to use?
  - 6 months
- We will discuss more about how we will handle the project slides
- Raul will try to setup a google colab env for vincent
- Coke and Pepsi

# 09/22/2023

- Ryan

  - updating slide deck theme
  - working on visualizations
  - looking for data for visualizations
  - suggested idea for cointegrated pairs to perform early stoppage
  - heatmap for cointegrated pairs

- Vincent

  - has been working on data for visualizations
  - working on notes for adf testings
  - researching for buy and sell signals
  - we will the use ratio for the spread
    - aka stock a divided by stock b
  - Engel granger method for stationarity
    - coint method for statsmodel uses this
  - working on a profit function
  - visualization of algo profit vs S&P 500

- Raul

  - add analysis write up for cointegration
  - rerun cointegration
    - by sector
    - for cointegrated assets
    - from those ensure the spread is stationary
  - push those pairs into a table in the database
  - might possibly take too long to run because of O(n^2)

- next steps
- profit/loss - Vincent
- rerun cointegration - Raul
- visualizations - Ryan
- Sync Monday @8pm, Thursday @8pm
