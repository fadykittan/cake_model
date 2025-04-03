import pandas as pd
from flask_restx import Resource
from marshmallow import ValidationError
import config
from schema.request_schema import CakeRequestSchema
from transform.transform_model import TransformModel
from transform.transform_preprocess import TransformPreprocess
from flask import jsonify
from datetime import datetime

cake_schema = CakeRequestSchema()
transform = TransformPreprocess(config)
model = TransformModel(config)

class PredictResource(Resource):
    """Resource for Price Predict"""

    # Define file upload parser (needs to be class variable)
    upload_parser = None

    def __init__(self, api, models, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api = api
        self.models = models

        # Initialize parser if not already done
        if self.upload_parser is None:
            self.upload_parser = api.parser()
            self.upload_parser.add_argument('Topping', type=str, required=True, help='Topping is required')
            self.upload_parser.add_argument('Layers', type=int, required=True, help='Topping is required')
            self.upload_parser.add_argument('Radius', type=int, required=True, help='Topping is required')

    def post(self):
        """Predict the price"""

        args = self.upload_parser.parse_args()

        try:
            print(args)
            request_body = cake_schema.load(args)
        except ValidationError as err:
            self.api.abort(400, err.messages)

        dataset = pd.DataFrame([[
            request_body['Radius'],
            request_body['Layers'],
            request_body['Topping'],
        ]], columns=config.DATA_SET_FEATURES)

        # Transform Dataset
        dataset_transformed = transform.transform(dataset)

        # Predict
        result = model.predict(dataset_transformed)

        result_vale = int(result[0])

        return jsonify(
            {
                'prediction': result_vale,
                'created_at': datetime.utcnow()
            }, 200)
