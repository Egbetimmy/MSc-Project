from itertools import combinations
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Lasso
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neural_network import MLPRegressor
from sklearn.compose import ColumnTransformer
import pandas as pd
import numpy as np
import time
import joblib
import pickle


def train_gbr(X_train, X_test, y_train, y_test):
    """
    Trains a Gradient Boosting Regressor model on the given dataset and saves it to disk.
    Returns the evaluation parameters.

    Args:
    - df: pandas DataFrame containing the data
    - x: list of column names for the features
    - y: column name for the target variable

    Returns:
    - a dictionary containing the evaluation parameters
    """

    gbr = GradientBoostingRegressor()
    gbr.fit(X_train, y_train)

    joblib.dump(gbr, 'model/gbr_model.joblib')

    y_pred = gbr.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = gbr.score(X_test, y_test)

    return {'MSE': mse, 'RMSE': rmse, 'R-squared': r2}


def train_dtr(X_train, X_test, y_train, y_test):
    """
    Trains a Decision Tree Regressor model on the given dataset and saves it to disk.
    Returns the evaluation parameters.

    Args:
    - df: pandas DataFrame containing the data
    - x: list of column names for the features
    - y: column name for the target variable

    Returns:
    - a dictionary containing the evaluation parameters
    """
    pipeline = Pipeline([('scaler', StandardScaler()), ('model', DecisionTreeRegressor())])

    pipeline.fit(X_train, y_train)

    joblib.dump(pipeline, 'model/dtr_model.joblib')

    y_pred = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = pipeline.score(X_test, y_test)

    return {'MSE': mse, 'RMSE': rmse, 'R-squared': r2}


def train_rfr(X_train, X_test, y_train, y_test):
    """
    Trains a Random Forest Regressor model on the given dataset and saves it to disk.
    Returns the evaluation parameters.

    Args:
    - df: pandas DataFrame containing the data
    - x: list of column names for the features
    - y: column name for the target variable

    Returns:
    - a dictionary containing the evaluation parameters
    """
    pipeline = Pipeline([('scaler', StandardScaler()), ('model', RandomForestRegressor())])

    pipeline.fit(X_train, y_train)

    joblib.dump(pipeline, 'model/rfr_model.joblib')

    y_pred = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = pipeline.score(X_test, y_test)

    return {'MSE': mse, 'RMSE': rmse, 'R-squared': r2}


def train_test_save_lasso(X_train, X_test, y_train, y_test):
    model = Lasso()
    model.fit(X_train, y_train)
    joblib.dump(model, 'model/lasso_model.pkl')
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2


def train_test_save_ridge(X_train, X_test, y_train, y_test):
    model = Ridge()
    model.fit(X_train, y_train)
    joblib.dump(model, 'model/ridge_model.pkl')
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2


def train_test_save_linear_regression(X_train, X_test, y_train, y_test):
    # Create a pipeline with a StandardScaler and a LinearRegression model
    pipeline = Pipeline([('scaler', StandardScaler()), ('model', LinearRegression())])

    # Fit the pipeline on the training data
    pipeline.fit(X_train, y_train)

    # Save the pipeline as a pickle file
    with open('models/linear_regression_model.pkl', 'wb') as f:
        pickle.dump(pipeline, f)

    # Evaluate the pipeline on the testing data
    y_pred = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return {'MSE': mse, 'R2': r2}


def train_test_save_support_vector_regression(X_train, X_test, y_train, y_test):
    # Create a pipeline with a StandardScaler and an SVR model
    pipeline = Pipeline([('scaler', StandardScaler()), ('model', SVR())])

    # Fit the pipeline on the training data
    pipeline.fit(X_train, y_train)

    # Save the pipeline as a pickle file
    with open('models/support_vector_regression_model.pkl', 'wb') as f:
        pickle.dump(pipeline, f)

    # Evaluate the pipeline on the testing data
    y_pred = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return {'MSE': mse, 'R2': r2}


def train_ann(X_train, X_test, y_train, y_test, save_path):
    # Define the numeric features to be scaled
    numeric_features = list(X_train.select_dtypes(include=['int64', 'float64']).columns)

    # Define the preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
        ])

    # Set up the neural network model as a step in the pipeline
    model = MLPRegressor(hidden_layer_sizes=(12,), activation='relu',
                         solver='lbfgs', learning_rate_init=0.001, alpha=0.001)
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('model', model)])

    # Train the pipeline on the training data
    pipeline.fit(X_train, y_train)

    # Make predictions on the test data and calculate RMSE
    y_pred = pipeline.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    # Save the trained model
    joblib.dump(pipeline, save_path)

    # Return the evaluation metrics
    return {'RMSE': rmse}


def get_column_combinations(x_cols):
    column_combinations = []
    for r in range(2, len(x_cols) + 1):
        for combo in combinations(x_cols, r):
            column_combinations.append(list(combo))
    return column_combinations


def train_models(df, x_cols, y_col):
    """
    Trains and evaluates models on all possible combinations of x columns.
    Returns the best-performing combination and its evaluation parameters.

    Args:
    - df: pandas DataFrame containing the data
    - x_cols: list of column names for the features
    - y_col: column name for the target variable

    Returns:
    - a DataFrame containing the evaluation metrics for each model and feature combination
    """

    X_train, X_test, y_train, y_test = train_test_split(df[x_cols], df[y_col], test_size=0.2)

    train_path = "data/train.csv"
    test_path = "data/test.csv"

    X_train.to_csv(train_path, index=False)
    X_test.to_csv(test_path, index=False)
    y_train.to_csv(train_path, mode='a', index=False, header=False)
    y_test.to_csv(test_path, mode='a', index=False, header=False)

    combination = get_column_combinations(x_cols)
    eval_list = []
    model_types = ['svr', 'ann', 'gbr', 'dtr', 'rfr']
    model_times = {model_type: [] for model_type in model_types}

    for combo in combination:
        print(f"Training model with columns: {combo}")
        X_train_combo = X_train[combo]
        X_test_combo = X_test[combo]

        y_train_combo = y_train[combo]
        y_test_combo = y_test[combo]

        # Train and time each model
        eval_params = {}
        for model_type in model_types:
            start_time = time.time()
            if model_type == 'svr':
                eval_params[model_type] = train_test_save_support_vector_regression(X_train_combo, X_test, y_train,
                                                                                    y_test_combo)
            elif model_type == 'ann':
                eval_params[model_type] = train_ann(X_train_combo, X_test_combo, y_train_combo, y_test_combo,
                                                    'models/trained_model.joblib')
            elif model_type == 'gbr':
                eval_params[model_type] = train_gbr(X_train_combo, X_test_combo, y_train_combo, y_test_combo)
            elif model_type == 'dtr':
                eval_params[model_type] = train_dtr(X_train_combo, X_test_combo, y_train_combo, y_test_combo)
            elif model_type == 'rfr':
                eval_params[model_type] = train_rfr(X_train_combo, X_test_combo, y_train_combo, y_test_combo)
            end_time = time.time()
            model_times[model_type].append(end_time - start_time)

        # Save the evaluation parameters for this combination
        eval_dict = {'columns': combo, 'eval_params': eval_params}
        eval_list.append(eval_dict)

    # Convert the list of dictionaries to a DataFrame
    df_eval = pd.DataFrame(eval_list)

    # Compute the average time for each model
    avg_times = {model_type: np.mean(model_times[model_type]) for model_type in model_types}
    df_times = pd.DataFrame.from_dict(avg_times, orient='index', columns=['average_time'])

    # Return the evaluation metrics DataFrame and the model time DataFrame
    return df_eval, df_times
