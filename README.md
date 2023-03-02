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


