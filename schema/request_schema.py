from marshmallow import Schema, fields

class CakeRequestSchema(Schema):
    Radius = fields.Integer(required=True)
    Layers = fields.Integer(required=True)
    Topping = fields.String(required=True)

