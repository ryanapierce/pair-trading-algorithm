import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import date
from typing import List, Tuple
from helper_methods import *


def plot_stock_pair(
    series_one: np.ndarray, label_one: str, series_two: np.ndarray, label_two: str
) -> None:
    """Plot a pair of stock price series on the same graph

    Parameters:
        series_one (np.ndarray): An array containing the prices of first stock
        label_one (str): Label for the first stock
        series_two (np.ndarray): An array containing the prices of second stock
        label_two (str): Label for the second stock

    Returns:
        None: The function displays the stock pair prices as a plot
    """
    _fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(series_one, label=label_one, color="gold")
    ax.plot(series_two, label=label_two, color="blue")

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%y"))
    plt.xticks(rotation=45)
    ax.yaxis.set_major_formatter("${:.2f}".format)

    ax.legend()
    ax.set_title("Stock Pair Prices")
    plt.grid()
    plt.show()


def plot_stock_one_adjusted_pair(
    series_one: np.ndarray, label_one: str, series_two: np.ndarray, label_two: str
) -> None:
    """Plot a pair of stock price series on the same graph

    Parameters:
        series_one (np.ndarray): An array containing the prices of first stock
        label_one (str): Label for the first stock
        series_two (np.ndarray): An array containing the prices of second stock
        label_two (str): Label for the second stock

    Returns:
        None: The function displays the stock pair prices as a plot
    """
    series_one_adjusted = series_one / (np.mean(series_one) / np.mean(series_two))
    plot_stock_pair(series_one_adjusted, label_one, series_two, label_two)


def plot_stock_pair_ratio(series_one, label_one, series_two, label_two) -> None:
    """Plot the ratio and z-score of two stock price series, along with threshold lines

    Parameters:
        series_one: An array of prices of the first stock
        label_one (str): Label for the first stock series
        series_two: An array of prices of the second stock
        label_two (str): Label for the second stock series

    Returns:
        None: The function displays the stock pair ratio, z-score, and threshold lines as a plot
    """
    # Use ratios to calculate spread
    ratio = series_one / series_two

    # Normalize the series
    z_score = (ratio - ratio.mean()) / ratio.std()

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(z_score, label=f"Ratio ({label_one} / {label_two})")
    plt.axhline(z_score.mean(), color="black")

    # ~80% of the data lies within our threshold
    plt.axhline(trade_threshold(z_score), color="blue")
    plt.axhline(-trade_threshold(z_score), color="blue")

    high_point = z_score.idxmax()
    low_point = z_score.idxmin()

    ax.scatter(high_point, z_score[high_point], color="red", marker="v", label="Sell")
    ax.scatter(low_point, z_score[low_point], color="green", marker="^", label="Buy")

    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%y"))

    ax.set_title("Stock Pair Ratio")
    ax.legend()
    plt.show()


def plot_mvg_avg_ratio(price_ratio_series: np.ndarray, train_data: np.ndarray) -> None:
    """Plot a graph based on the moving average ratio z-score and threshold lines

    Parameters:
        price_ratio_series (np.ndarray): An array of the price ratio series
        train_data (np.ndarray): An array of training data for threshold

    Returns:
        None: The function displays the moving average ratio z-score, threshold lines, and legend as a plot
    """
    # Plot new graph based off moving avg
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(mvg_avg_z_score(price_ratio_series), label="mvg_avg ratio z_score")
    plt.axhline(0, color="black")
    plt.axhline(trade_threshold(mvg_avg_z_score(train_data)), color="blue")
    plt.axhline(-trade_threshold(mvg_avg_z_score(train_data)), color="blue")
    plt.legend()
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%y"))
    ax.set_title("Moving Averages")
    plt.show()


def plot_trade_signals(ratio_series: np.ndarray, train_data: np.ndarray) -> None:
    """Plot buy and sell trade signals on a graph of the given ratio series

    Parameters:
        ratio_series (np.ndarray): An array of the ratio series
        train_data (np.ndarray): An array of training data for trade signals

    Returns:
        None: The function displays buy and sell trade signals along with the ratio series as a plot
    """
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(ratio_series, label="label")
    ax.scatter(
        ratio_series.index[trade_signals(ratio_series, train_data) == 1],
        ratio_series[trade_signals(ratio_series, train_data) == 1],
        color="green",
        marker="^",
        label="Buy (1)",
    )
    ax.scatter(
        ratio_series.index[trade_signals(ratio_series, train_data) == -1],
        ratio_series[trade_signals(ratio_series, train_data) == -1],
        color="red",
        marker="v",
        label="Sell (-1)",
    )
    ax.set_title("Buy/Sell Decision Points")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%y"))
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()


def plot_trade_signals_no_stop_loss(
    ratio_series: np.ndarray, train_data: np.ndarray
) -> None:
    """Plot buy and sell trade signals on a graph of the given ratio series for no stop-loss

    Parameters:
        ratio_series (np.ndarray): An array of the ratio series
        train_data (np.ndarray): An array of training data for trade signals

    Returns:
        None: The function displays buy and sell trade signals along with the ratio series as a plot
    """
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(ratio_series, label="label")
    ax.scatter(
        ratio_series.index[trade_signals_no_stop_loss(ratio_series, train_data) == 1],
        ratio_series[trade_signals_no_stop_loss(ratio_series, train_data) == 1],
        color="green",
        marker="^",
        label="Buy (1)",
    )
    ax.scatter(
        ratio_series.index[trade_signals_no_stop_loss(ratio_series, train_data) == -1],
        ratio_series[trade_signals_no_stop_loss(ratio_series, train_data) == -1],
        color="red",
        marker="v",
        label="Sell (-1)",
    )
    ax.set_title("Buy/Sell Decision Points - No Stop-Loss")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%y"))
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()


def create_cointegration_heatmap(
    top_pairs: List[str], training_date_range: Tuple[str, str]
) -> None:
    """Create a cointegration heatmap for a list of top stock pairs

    Parameters:
        top_pairs (List[str]): List of stock pairs
        training_date_range (Tuple[str, str]): A tuple containing the start and end dates ("YYYY-MM-DD", "YYYY-MM-DD")

    Returns:
        None: The function displays the heatmap
    """
    p_value_matrix = np.zeros((len(top_pairs), len(top_pairs)))

    start_date = date(*[int(n) for n in training_date_range[0].split("-")])
    end_date = date(*[int(n) for n in training_date_range[1].split("-")])

    for i in range(len(top_pairs)):
        for j in range(i + 1, len(top_pairs)):
            stock_one = get_stock_prices(top_pairs[i], start_date, end_date)["Close"]
            stock_two = get_stock_prices(top_pairs[j], start_date, end_date)["Close"]

            is_cointegrated, result = test_stock_cointegration(stock_one, stock_two)
            p_value = result[1]

            p_value_matrix[i][j] = p_value
            p_value_matrix[j][i] = p_value

    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(p_value_matrix, cmap="cividis")

    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel("P-Value", rotation=-90, va="bottom")

    ax.set_xticks(np.arange(len(top_pairs)))
    ax.set_yticks(np.arange(len(top_pairs)))
    ax.set_xticklabels(top_pairs)
    ax.set_yticklabels(top_pairs)

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    for i in range(len(top_pairs)):
        for j in range(len(top_pairs)):
            value = p_value_matrix[i, j]
            ax.text(
                j, i, f"{value:.5f}", ha="center", va="center", color="w", fontsize=8
            )

    ax.set_title("Cointegration P-Value Heatmap")
    plt.show()
