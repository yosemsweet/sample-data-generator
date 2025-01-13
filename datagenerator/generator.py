import string
from collections import defaultdict
from faker import Faker
from faker.providers import internet, person, date_time, company, misc, lorem


fake = Faker()
fake.add_provider(internet)
fake.add_provider(person)
fake.add_provider(date_time)
fake.add_provider(company)
fake.add_provider(misc)
fake.add_provider(lorem)


def generate_column(column_specification: dict, num_rows: int) -> dict:
    # generator = type_generator[column_specification["type"]]

    generator = getattr(fake, column_specification["type"])
    generator_args = column_specification.get("constraints", {})

    return [generator(**generator_args) for _ in range(num_rows)]


def generate_columns(schema, num_rows):
    return {column["name"]: generate_column(column, num_rows) for column in schema}
