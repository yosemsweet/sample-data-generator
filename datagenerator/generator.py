from faker import Faker
from faker.providers import address, company, date_time, internet, lorem, misc, person


fake = Faker()
fake.add_provider(address)
fake.add_provider(company)
fake.add_provider(date_time)
fake.add_provider(internet)
fake.add_provider(lorem)
fake.add_provider(misc)
fake.add_provider(person)


def generate_column(column_specification: dict, num_rows: int) -> list:
    generator = getattr(fake, column_specification["type"])
    generator_args = column_specification.get("constraints", {})

    return [generator(**generator_args) for _ in range(num_rows)]


def generate_columns(schema, num_rows) -> dict:
    return {column["name"]: generate_column(column, num_rows) for column in schema}
