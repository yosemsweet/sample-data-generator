import pandas as pd
from datagenerator.generator import generate_columns
from datagenerator.schemaparser import SchemaParser


def generate(schema: dict, number_of_rows: int) -> pd.DataFrame:
    schema = SchemaParser(schema)

    data = generate_columns(schema.parse(), number_of_rows)

    print(data)

    df = pd.DataFrame.from_dict(data=data)

    return df
