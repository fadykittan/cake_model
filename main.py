import pandas as pd
import config
from transform.transform_model import TransformModel
from transform.transform_preprocess import TransformPreprocess


def main():
    df = pd.DataFrame({
    'Radius [cm]': [16],
    'Layers': [1],
    'Topping': ['Writing'],
    'Price': [311]
    })

    transform: TransformPreprocess = TransformPreprocess(config)
    df = transform.transform(df)

    model: TransformModel = TransformModel(config)
    result = model.predict(df)
    print(f"price: {result}")

if __name__ == '__main__':
    main()

