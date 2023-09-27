import matplotlib.pyplot as plt
import numpy as np
from helper_methods import *

def plot_stock_pair(series_one, label_one, series_two, label_two):
    _fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(series_one, label=label_one, color='gold')
    ax.plot(series_two, label=label_two, color='blue')
    ax.legend()
    ax.set_title("Stock Pair Prices")
    plt.show()

def plot_stock_one_adjusted_pair(series_one, label_one, series_two, label_two):
    series_one_adjusted = series_one / \
        (np.mean(series_one) / np.mean(series_two))
    plot_stock_pair(series_one_adjusted, label_one, series_two, label_two)

def plot_stock_pair_ratio(series_one, label_one, series_two, label_two):
    # Use ratios to calculate spread
    ratio = series_one / series_two

    # Normalize the series
    z_score = (ratio - ratio.mean()) / ratio.std()

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(z_score, label=f'Ratio ({label_one} / {label_two})')
    plt.axhline(z_score.mean(), color='black')

    # ~80% of the data lies within our threshold
    plt.axhline(trade_threshold(z_score), color = 'blue')
    plt.axhline(-trade_threshold(z_score), color = 'blue')

    ax.set_title("Stock Pair Ratio")
    ax.legend()
    plt.show()

def plot_mvg_avg_ratio(price_ratio_series, train_data):
    # Plot new graph based off moving avg
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(mvg_avg_z_score(price_ratio_series), label='mvg_avg ratio z_score')
    plt.axhline(0, color='black')
    plt.axhline(trade_threshold(mvg_avg_z_score(train_data)), color = 'blue')
    plt.axhline(-trade_threshold(mvg_avg_z_score(train_data)), color = 'blue')
    plt.legend()
    ax.set_title("Moving Averages")
    plt.show()

def plot_trade_signals(ratio_series, train_data):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(ratio_series, label='label')
    ax.scatter(ratio_series.index[trade_signals(ratio_series, train_data) == 1], ratio_series[trade_signals(ratio_series, train_data) == 1], color='green', marker='^', label='Buy (1)')
    ax.scatter(ratio_series.index[trade_signals(ratio_series, train_data) == -1], ratio_series[trade_signals(ratio_series, train_data) == -1], color='red', marker='v', label='Sell (-1)')
    ax.set_title("Buy/Sell Decision Points")
    plt.show()

def plot_trade_signals_no_stop_loss(ratio_series, train_data):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(ratio_series, label='label')
    ax.scatter(ratio_series.index[trade_signals_no_stop_loss(ratio_series, train_data) == 1], ratio_series[trade_signals_no_stop_loss(ratio_series, train_data) == 1], color='green', marker='^', label='Buy (1)')
    ax.scatter(ratio_series.index[trade_signals_no_stop_loss(ratio_series, train_data) == -1], ratio_series[trade_signals_no_stop_loss(ratio_series, train_data) == -1], color='red', marker='v', label='Sell (-1)')
    ax.set_title("Buy/Sell Decision Points - No Stop-Loss")
    plt.show()

def plot_heatmap(stationary_tickers, cointegration_scores):
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(cointegration_scores, cmap="cividis")
    ax.set_xticks(np.arange(len(stationary_tickers)), labels=stationary_tickers)
    ax.set_yticks(np.arange(len(stationary_tickers)), labels=stationary_tickers)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
            rotation_mode="anchor")
    for i in range(len(stationary_tickers)):
        for j in range(len(stationary_tickers)):
            text = ax.text(j, i, cointegration_scores[i, j],
                        ha="center", va="center", color="w", fontsize=10)
    ax.set_title("Cointegration of Stationary Assets")
    fig.tight_layout()
    plt.show()
















