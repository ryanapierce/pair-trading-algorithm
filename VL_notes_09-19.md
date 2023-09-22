Notes:

-How do we know that mean reversion holds?
If two stocks are cointegrated, they can be linear combined to form a stationary series. By definition, a stationary series has a constant mean over time. Our algorithm fails if this mean reversion does not hold, so it is important to constantly check if the two stocks remain cointegrated if we are trying to run this model in real time.

Cointegration is not correlation:
Two series can be correlated without being cointegrated, and two series can be cointegrated without being correlated. For example, you can have two series A and B that both increase, so they are correlated, but if A always increases faster than B, then they will never converge. Thus, A and B are not cointegrated.

With hypothesis testing in statistics, there is always a chance that you will be wrong. How do we minimize the chance that our cointegration will be incorrect?
Our first precaution is that we are only looking for pairs in the same industry. This is a "common sense" test based on economic fundamentals.
In addition to this funamental analysis, we then use technical analysis in the form of the Augmented Dickey-Fuller (ADF) test and the Engle Granger test
ADF test on ratio between 2 stocks
Again, there is always a chance that we are wrong, and we determine that two stocks are cointegrated when they are not in reality. There is also a chance that we correctly determine cointegration, but we get unlucky and the pair is no longer cointegrated 1 month from now. These are potential points of failure for our algorithm that could cause us to lose money, but as they say on Wall Street, there's no such thing as a "free lunch".

Avoiding look-ahead bias:
With time series data, look ahead bias is a form of data leakage. It happens if you use data that happened after a certain time to inform decisions that previous time. With pairs trading, this can happen if we test Z-scores on the entire time series. This will lead to backtesting results that are very good, fooling us into thinking the predictive power of our model is much better than it actually is. To avoid look-ahead bias, we will calculate spread based off the 30 day moving average.

Difference vs Ratio for calculating difference:
Difference is more appropriate when we are comparing linear series with the same units or when we are interested in absolute differences. Ratio is more appropriate when comparing series on logarithmic or multiplicative scales, or if we are interested in relative differences. With this specific data, stock prices are in the same units ($), but prices are almost always multiplicative (Ex. PEP is approx 2.5x KO). Thus, we will use ratio to calculate spread.

Train vs Test Split:
In order to validate our model, we will save 20% of our data as our test set and 80% as our train set. Because we are analyzing 5 years of data, our train set will be 1 year and our test set will be 4 years. Note that for this type of data, we don't want gaps in each data set, so we will not randomly split the data into train and test. Instead, we will use the most recent year as our test set and the 4 years before that as the train set.