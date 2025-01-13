import datagenerator
import json
import sys
from optionsparser import options_parser
from pathlib import Path


def main() -> int:
    options = options_parser().parse_args(sys.argv)
    print(options)

    with open(options.schema_file, "r") as schema_file:
        data_generation_schema = json.loads(schema_file.read())

    if data_generation_schema is None:
        print("Invalid schema file")
        return 1

    generated_data = datagenerator.generate(
        data_generation_schema, options.number_of_rows
    )

    # make sure the directory to the output file exists
    filepath = Path(options.output_file)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    # write the CSV
    generated_data.to_csv(options.output_file, index=False)

    return 0


if __name__ == "__main__":
    sys.exit(main())  # next section explains the use of sys.exit
