import numpy as np
import pandas as pd
import joblib

model = joblib.load('models/TMBDpred_rf.joblib')

def get_form_data(data):
    feature_values = {
       'budget' : 10000000,
       'popularity' : 10,
       'cast_size' : 10,
       'runtime' : 120,
       'has_collection' : 0,
       'crew_size' : 30,
       'has_homepage' : 0,
       'us_production' : 1,
       'is_en_original_language' : 1
    }

    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]

    return feature_values


def predict(data, debug=False):
    
    #Getting values
    values = get_form_data(data)

    if debug:
        print(f'Feature values: {values}\n')

    column_order = [
       'budget',
       'popularity',
       'cast_size',
       'runtime',
       'has_collection',
       'crew_size',
       'has_homepage',
       'us_production',
       'is_en_original_language']

    values = np.array([values[feature] for feature in column_order], dtype=object)


    if debug:
        print('Ordered feature values: ')
        print(list(zip(column_order, values)))

    pred = model.predict(values.reshape(1,-1))
    return str(pred[0])