# MSc-Project
Pore pressure prediction
    data collection
    data cleaning
    feature engineering
        dealing with outliers
    ML model
Permeability prediction
    data collection
    data cleaning
    feature engineering
        dealing with outliers
    ML model
Anisotropy automation
    calculations
    plots

## saving model using pickle
import pickle
with open('model_pickle', 'wb') as file:
    pickle.dump(model,file)
### loading model
with open('model_pickle', 'rb') as file:
    mp = pickle.load(file)
mp.predict([[5000]])

## saving model using joblib
import joblib
joblib.dump(model, 'model_joblib')
### loading model
mj = joblib.load('model_joblib')
mj.predict([[5000]])

# export column information
import json
columns = {
    'data_columns' : [col.lower() for col in X.columns]
}
with open("columns.json","w") as f:
    f.write(json.dumps(columns))

# class format
def original_function(arg1, arg2, arg3):
    # original code here
    return result

def refactored_function(self, arg1_name, arg2_name, arg3_name):
    """
    Brief description of the function.

    Parameters
    ----------
    arg1_name : arg1_type
        Description of arg1.
    arg2_name : arg2_type
        Description of arg2.
    arg3_name : arg3_type
        Description of arg3.

    Returns
    -------
    result_type
        Description of the result.
    """
    # refactored code here
    return result

## Deployment if possible
    firebase
    github
    netlify


# Anisotropy Automation

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

