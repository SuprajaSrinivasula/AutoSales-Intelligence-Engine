import numpy as np

def make_prediction(model, input_data):
    features = np.array(list(input_data.values())).reshape(1, -1)
    return model.predict(features)[0]