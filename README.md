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

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.



# Coffee Shop Full Stack

## Full Stack Nano - IAM Final Project

Udacity has decided to open a new digitally enabled cafe for students to order drinks, socialize, and study hard. But they need help setting up their menu experience.

You have been called on to demonstrate your newly learned skills to create a full stack drink menu application. The application must:

1. Display graphics representing the ratios of ingredients in each drink.
2. Allow public users to view drink names and graphics.
3. Allow the shop baristas to see the recipe information.
4. Allow the shop managers to create new drinks and edit existing drinks.
