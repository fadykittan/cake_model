from api.endpoints.predict_endpoint import PredictResource


def register_routes(api, models):
    """
    Register all API routes

    Args:
        api: Flask-RESTX API instance
        repository: Database repository
        models: Swagger models
    """

    # Create namespace
    ns_cake = api.namespace('cake', description='Cake Price Prediction endpoints')

    # Register predict endpoint
    @ns_cake.route('/predict')
    @ns_cake.expect(models['cake_model'])
    @ns_cake.response(200, 'Success',models['cake_model'])
    @ns_cake.response(400, 'Bad Request')
    @ns_cake.response(500, 'Internal Server Error')
    @ns_cake.doc(models['model_info_model'])
    class CakePredictionRoute(PredictResource):
        def __init__(self, *args, **kwargs):
            super().__init__(api, models, *args, **kwargs)
