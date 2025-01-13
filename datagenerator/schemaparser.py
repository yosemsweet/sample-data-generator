import jsonschema


class SchemaParser:
    def __init__(self, schema):
        self.schema = schema

        jsonschema.validate(schema, schema_validator)

    def parse(self):
        return self.schema


schema_validator = {
    "type": "array",
    "items": {
        "type": "object",
        "required": ["name", "type"],
        "properties": {
            "name": {"type": "string", "description": "The name of the column."},
            "type": {
                "type": "string",
                "description": "the type of data - used to identify the faker provider.",
            },
            "constraints": {"type": "array"},
        },
    },
}
