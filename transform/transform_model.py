import pickle
from sklearn.linear_model import LinearRegression

class TransformModel:

    def __init__(self, config):
        self.config = config
        with open(config.MODEL_PATH, 'rb') as f:
            self.model: LinearRegression = pickle.load(f)

    def predict(self, df):
        return self.model.predict(df)

