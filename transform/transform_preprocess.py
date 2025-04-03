import pickle
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

class TransformPreprocess:

    def __init__(self, config):
        self.config = config
        with open(config.ONE_HOT_ENCODED_PATH, 'rb') as f:
            self.one_hot_encoded: OneHotEncoder = pickle.load(f)

    def transform(self, dataset):
        df = dataset[self.config.DATA_SET_FEATURES]

        new_encoded_array = self.one_hot_encoded.transform(df[self.config.ONE_HOT_ENCODED_FEATURE])
        print(new_encoded_array)
        encoded_df = pd.DataFrame(
            new_encoded_array,
            columns=self.one_hot_encoded.get_feature_names_out(),
            index=df.index
        )
        print(encoded_df)

        new_data = pd.concat([df.drop('Topping', axis=1), encoded_df], axis=1)
        print(new_data)
        return new_data

