# Sample data generator

What is this?
A python script you can use to rapidly generate sample data that matches a schema.
You give it a json file representing the schema of the csv you would like to generate, and it will use [Faker](https://faker.readthedocs.io/en/stable/index.html) to generate a csv that matches the input schema.

Example usage:

```
$ python3 main.py --schema-file schemas/user-schema.json -n 200 -o data/users.csv
```

## Installing

1. Clone from github
2. Set up your python venv for this project `python3 -m venv /path/to/new/virtual/environment`. Don't forget to activate this venv.
3. Install requirements using `pip install -r requirements.txt`

Done!


## Creating a schema file

All schemas have to match the schema_validator json schema in `datagenerator/schemaparser.py`. If your schema doesn't match, the data generator will raise an error.

The general structure for a schema is:

```
[ // A list of column specifications
    { // column specificaation
        "name": "A column name",
        "type": "A faker provider method to generate this data",
        "constraints": { // Any constraints for this column - these get passed to the faker provider method.
            KEYWORD_ARG_NAME: KEYWORD_ARG_VALUE
        }
    }
]
```
You can find sample schemas in the `schemas` directory.
