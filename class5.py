import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import r2_score
import joblib


def calculate_r2(actual_values, predicted_values):
    """
    Calculates R-squared values for multiple predicted value columns given an actual value column.

    Parameters
    ----------
    actual_values : pandas.Series
        A series containing the actual values.
    predicted_values : pandas.DataFrame
        A DataFrame containing the predicted value columns.

    Returns
    -------
    dict
        A dictionary containing the R-squared values for each predicted value column.
    """
    r2_values = {}
    for column in predicted_values.columns:
        mean_actual = np.mean(actual_values)
        ss_total = np.sum((actual_values - mean_actual) ** 2)
        ss_residual = np.sum((actual_values - predicted_values[column]) ** 2)
        r2 = 1 - (ss_residual / ss_total)
        r2_values[column] = r2
    return r2_values


def evaluate_models(models, model_names, new_data, target):
    """
    Evaluates a list of saved models on a new dataframe and returns a dataframe containing the model names
    and their corresponding R-squared values on the new data.

    Parameters
    ----------
    models : list
        A list of saved models.
    model_names : list
        A list of model names corresponding to the saved models.
    new_data : pandas.DataFrame
        A new dataframe to evaluate the models on.
    target : str
        The name of the target variable in the new dataframe.

    Returns
    -------
    pandas.DataFrame
        A dataframe containing the model names and their corresponding R-squared values on the new data.
    """

    # Initialize an empty list to store results
    results = []

    # Loop through each model and evaluate it on the new data
    for i, model in enumerate(models):
        # Load the model from disk
        model = joblib.load(model)

        # Make predictions on the new data
        y_pred = model.predict(new_data.drop(columns=[target]))

        # Calculate R-squared on the new data
        r2 = r2_score(new_data[target], y_pred)

        # Add model name and R-squared to the results list
        results.append([model_names[i], r2])

    # Create a dataframe from the results list
    results_df = pd.DataFrame(results, columns=['Model', 'R-squared'])

    return results_df


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


def plot_predictions(df, model_columns, target):
    # Set the figure size
    plt.figure(figsize=(12, 6))

    # Plot the actual values
    sns.lineplot(data=df, x=df.index, y=target, label='Actual')

    # Plot the predicted values for each model
    for column in model_columns:
        # Get the predicted values for the model
        y_pred = df[column]

        # Plot the predicted values as a scatter plot with a dotted line style
        sns.lineplot(data=df, x=df.index, y=y_pred, label=column, linestyle='dotted')

    # Set the plot title and axis labels
    plt.title('Actual vs Predicted Values')
    plt.xlabel('Date')
    plt.ylabel(target)

    # Show the legend
    plt.legend()



'''
# Define a list of saved model paths
model_paths = [
    'models/decision_tree_best_model.pkl', 'models/gradient_boosting_best_model.pkl', 'models/random_forest_best_model.pkl'
]

# Define a list of model names
model_names = ['decision_tree', 'gradient_boosting', 'random_forest']

# Evaluate the models on the new data
results_df = evaluate_models(model_paths, model_names, X, 'Actual Permeability')

# Print the results
print(results_df)
'''