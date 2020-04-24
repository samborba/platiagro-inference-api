import logging
import os
import pickle
import numpy as np
import pandas as pd

_ISOLATION_FOREST_MODEL = os.path.abspath(os.getcwd() + '/src/lib/anomaly_model.pickle')
_LOGISTIC_REGRESSION_MODEL = os.path.abspath(os.getcwd() + '/src/lib/failure_model.pickle')


def isolation_forest_inference(input_data: list) -> pd.DataFrame:
    array_data = np.array([input_data])
    event = pd.DataFrame(array_data, columns=['Temperatura', 'Pressao', 'Vibracao'])

    x_event = event.to_numpy()

    with open (_ISOLATION_FOREST_MODEL, 'rb') as file:
        loaded_model = pickle.load(file, encoding='latin1')

    event['AnomalyScore'] = loaded_model.score_samples(x_event)
    return event


def logistic_regression_inference(anomaly_dataframe: pd.DataFrame, rpm: list) -> dict:
    x_anomaly_dataframe = anomaly_dataframe.to_numpy()

    with open(_LOGISTIC_REGRESSION_MODEL, 'rb') as file:
        loaded_model = pickle.load(file, encoding='latin1')

    predict_result = loaded_model.predict_proba(x_anomaly_dataframe)
    anomaly_dataframe[rpm[0]] = rpm[1] # rpm[0] -> label and rpm[1] -> value
    anomaly_dataframe['FailureProbability'] = predict_result[:, [1]]

    return anomaly_dataframe.to_dict('list')
