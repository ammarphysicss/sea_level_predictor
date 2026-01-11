import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    df = df.dropna(subset=["CSIRO Adjusted Sea Level"])

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    res1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x1 = np.arange(int(df["Year"].min()), 2051)
    y1 = res1.slope * x1 + res1.intercept
    ax.plot(x1, y1)

    df_2000 = df[df["Year"] >= 2000]
    res2 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    x2 = np.arange(2000, 2051)
    y2 = res2.slope * x2 + res2.intercept
    ax.plot(x2, y2)

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    plt.savefig("sea_level_plot.png")
    return fig
