from flask_restx import fields


def create_models(api):

    timestamp_model = api.model('Timestamp', {
        'created_at': fields.DateTime(description='Creation time'),
    })

    price_model = api.model('Price', {
        'price': fields.Float(description='The Price of the Cake'),
    })

    cake_model = api.model('Cake', {
        'Radius': fields.Integer(description='Radius of the Cake'),
        'Layers': fields.Integer(description='Number of Layers'),
        'Topping': fields.String(description='Topping of the Cake'),
    })

    model_info_model = api.model('ModelInfo', {
        'model_version': fields.Float(description='Model Version'),
        'last_train': fields.String(description='Last Train Date/time'),
        'avg_run_time': fields.Float(description='model run time in sec'),
        'created_at': fields.Nested(timestamp_model, many=False),
    })

    return {
        'timestamp_model': timestamp_model,
        'price_model': price_model,
        'cake_model': cake_model,
        'model_info_model': model_info_model
    }
