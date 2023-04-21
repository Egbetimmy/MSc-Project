import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def scatter_plot(y_true, y_pred, title):
    # Take the natural log of both arrays
    y_true_log = np.log(y_true)
    y_pred_log = np.log(y_pred)

    # Create scatter plot of y_true_log vs. y_pred_log
    sns.scatterplot(x=y_true_log, y=y_pred_log, alpha=0.5)
    plt.xlabel('Actual Values (log)')
    plt.ylabel('Predicted Values (log)')
    plt.title(title)

    plt.show()


def line_plot(y_true, y_pred, title):
    # Take the natural log of both arrays
    y_true_log = np.log(y_true)
    y_pred_log = np.log(y_pred)

    # Create line plot of y_true_log vs. y_pred_log
    sns.lineplot(data=pd.DataFrame({'Actual': y_true_log, 'Predicted': y_pred_log}))
    plt.xlabel('Sample Index')
    plt.ylabel('Target Variable (log)')
    plt.title(title)

    plt.show()
