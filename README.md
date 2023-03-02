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

