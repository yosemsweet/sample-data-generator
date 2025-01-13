import argparse


def options_parser() -> argparse.ArgumentParser:
    """Return an ArgumentParser object"""
    parser = argparse.ArgumentParser(
        description="Generate a csv with sample data matching a target schema"
    )
    parser.add_argument("positional_args", nargs="?")

    parser.add_argument(
        "--schema-file",
        type=str,
        help="path to a schema file describing the shape of data to generate",
        required=True,
    )
    parser.add_argument(
        "-n",
        "--number-of-rows",
        type=int,
        help="number of rows to generate",
        default=100,
    )
    parser.add_argument(
        "-o",
        "--output-file",
        type=str,
        help="the generated csv file path",
        default="./sample-data.csv",
    )

    return parser
