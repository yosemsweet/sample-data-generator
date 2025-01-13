import string
from collections import defaultdict
from faker import Faker
from faker.providers import internet, person


fake = Faker()
fake.add_provider(internet)
fake.add_provider(person)


# type_generator = defaultdict(
#     lambda: lambda: "Unknown",
#     [
#         ("email", fake.email),
#         ("first_name", fake.first_name),
#         ("last_name", fake.last_name),
#         ("user_id", fake.uuid4),
#         (
#             "permission_type",
#             fake.random_element(
#                 elements=[
#                     "Resourcing Administrator",
#                     "Portfolio Editor",
#                     "People Scheduler",
#                     "Portfolio Reporter",
#                     "Portfolio Viewer",
#                     "Project Editor",
#                     "Contractor",
#                 ]
#             ),
#         ),
#         (
#             "license_type",
#             fake.random_element(
#                 elements=[
#                     "licensed",
#                     "managed_resource",
#                 ]
#             ),
#         ),
#     ],
# )


def generate_column(column_specification: dict, num_rows: int) -> dict:
    # generator = type_generator[column_specification["type"]]

    generator = getattr(fake, column_specification["type"])
    generator_args = column_specification.get("constraints", {})

    return [generator(**generator_args) for _ in range(num_rows)]


def generate_columns(schema, num_rows):
    return {column["name"]: generate_column(column, num_rows) for column in schema}
