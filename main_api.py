from flask import Flask, request, jsonify
from marshmallow import ValidationError

import config
from schema.request_schema import CakeRequestSchema
from transform.transform_model import TransformModel
from transform.transform_preprocess import TransformPreprocess
import pandas as pd

app = Flask(__name__)

transform: TransformPreprocess = TransformPreprocess(config)
model: TransformModel = TransformModel(config)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    print(data)

    cake_schema = CakeRequestSchema()

    try:
        cake = cake_schema.load(data)
    except ValidationError as e:
        return jsonify(e.messages), 400

    df = pd.DataFrame({
        'Radius [cm]': [cake['Radius']],
        'Layers': [cake['Layers']],
        'Topping': [cake['Topping']]
    })

    print(df)
    df = transform.transform(df)
    result = model.predict(df)
    print(f"price: {result}")

    return jsonify({"price": str(result[0])})

if __name__ == '__main__':
    app.run(port=8080, debug=True)

