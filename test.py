import pytest
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

# Load test data
test_data = pd.DataFrame(
    {'Log_ILD': [2.0], 'RHOB': [2.2], 'velocity': [3.0], 'GR': [50], 'Facies': [0], 'Depth': [3000]})
expected_output = 50.443


# Define test function
def test_model_prediction():
    # Load well log data
    data = pd.read_csv('well_log_data.csv')

    # Define input features and target variable
    X = data[['Log_ILD', 'RHOB', 'velocity', 'GR', 'Facies', 'Depth']]
    y = data['PERM']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a random forest regressor model
    with open('models/model_pickle', 'rb') as file:
        rf = pickle.load(file)

    # Make predictions on test data
    y_pred = rf.predict(X_test)

    # Check that the predicted output is a numpy array
    assert isinstance(y_pred, np.ndarray)

    # Check that the predicted output is not empty
    assert len(y_pred) > 0

    # Check that the predicted output is a one-dimensional array
    assert y_pred.ndim == 1

    # Check that the predicted output has the same length as the test data
    assert len(y_pred) == len(y_test)

    # Calculate model performance metrics
    mae = np.mean(abs(y_test - y_pred))
    mse = np.mean((y_test - y_pred) ** 2)
    rmse = np.sqrt(mse)
    r2 = rf.score(X_test, y_test)

    # Check that the mean absolute error is reasonable
    assert mae < 10

    # Check that the root mean squared error is reasonable
    assert rmse < 50

    assert r2 > 0.8, "R^2 is too low"

    # Make a prediction for new well log data
    new_data = pd.DataFrame(
        {'Log_ILD': [2.5], 'RHOB': [2.3], 'velocity': [3.5], 'GR': [40], 'Facies': [1], 'Depth': [2000]})
    new_pp = rf.predict(new_data)

    # Check that the predicted permeability is within an acceptable range
    assert np.isclose(new_pp[0], expected_output, rtol=0.1)


# Run the test function
test_model_prediction()


# Define test function for the neural network model
def test_neural_network():
    # Load well log data
    df = pd.read_csv('well_log_data.csv')

    # Define input features and target variable
    X = df[['Log_ILD', 'RHOB', 'velocity', 'GR', 'Facies', 'Depth', 'vs', 'PHI']]
    y = df['Pore_pressure']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Load the trained neural network model
    with open('models/model_pickle', 'rb') as file:
        nn = pickle.load(file)

    # Make predictions on the test data
    y_pred = nn.predict(X_test)

    # Check that the predicted values are within a reasonable range
    assert np.all(y_pred >= 0), "Predicted values are negative"
    assert np.all(y_pred <= 1), "Predicted values are greater than 1"

    # Calculate model performance metrics
    mae = np.mean(abs(y_test - y_pred))
    mse = np.mean((y_test - y_pred) ** 2)
    rmse = np.sqrt(mse)
    r2 = nn.score(X_test, y_test)

    # Check that the model performance metrics are within a reasonable range
    assert mae < 0.1, "MAE is too high"
    assert mse < 0.01, "MSE is too high"
    assert rmse < 0.1, "RMSE is too high"
    assert r2 > 0.8, "R^2 is too low"


"""
To run this test using pytest, 
save the code as a file called test_my_model.py in the same directory as your model code, 
and then run pytest in the command line.
"""