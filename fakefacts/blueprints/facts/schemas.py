from marshmallow import fields, validate

from fakefacts.extensions import marshmallow


class FactSchema(marshmallow.Schema):
    class Meta:
        fields = ('created_on', 'id', 'message')


class AddFactSchema(marshmallow.Schema):
    message = fields.Str(required=True,
                         validate=validate.Length(min=1, max=200))


fact_schema = FactSchema()
facts_schema = FactSchema(many=True)
add_fact_schema = AddFactSchema()
