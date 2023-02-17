from matplotlib.ticker import FuncFormatter
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import FuncFormatter


def plot(df):
    fig, ax = plt.subplots()

    ax.axis([0, 40, 0.01, 100000])
    ax.plot(df['CPOR'], df['CKHG'], 'bo')
    ax.set_yscale('log')
    ax.grid(True)
    ax.set_ylabel('Core Perm (mD)')
    ax.set_xlabel('Core Porosity (%)')

    # Format the axes so that they show whole numbers
    for axis in [ax.yaxis, ax.xaxis]:
        formatter = FuncFormatter(lambda y, _: '{:.16g}'.format(y))
        axis.set_major_formatter(formatter)

    plt.savefig('11-xplot-semi-log-fixed.png', dpi=300)
