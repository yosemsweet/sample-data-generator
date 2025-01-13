import random
import string
from collections import defaultdict


type_generator = defaultdict(
    lambda: lambda: "Unknown",
    [
        ("int", lambda: random.randint(0, 100)),
        ("float", lambda: random.uniform(0, 100)),
        ("str", lambda: "".join(random.choices(string.ascii_letters, k=10))),
    ],
)


def generate_column(column_specification: dict, num_rows: int) -> dict:
    generator = type_generator[column_specification["type"]]
    return [generator() for _ in range(num_rows)]


def generate_columns(schema, num_rows):
    return {column["name"]: generate_column(column, num_rows) for column in schema}
