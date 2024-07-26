import argparse
from pathlib import Path
from random import sample
from typing import Any

import lancedb
import pandas as pd

from schema import Myntra

def create_table(
    database: str,
    table_name: str,
    data_path: str,
    schema: Any = Myntra,
    mode: str = "overwrite",
    num_samples: int = 1000,
) -> None:
    """
    Create a table in the specified vector database and add data to it.

    Args:
        database (str): The name of the database to connect to.
        table_name (str): The name of the table to create.
        data_path (str): The path to the data directory.
        schema (Any, optional): The schema to use for the table. Defaults to Myntra.
        mode (str, optional): The mode for creating the table. Defaults to "overwrite".
        num_samples (int, optional): The number of image samples to be added to the database. Defaults to 1000.

    Returns:
        None

    Usage:
    >>> create_table(database="~/.lancedb", table_name="myntra", data_path="input")
    """
    
    # Connect to the lancedb database
    db = lancedb.connect(database)

    # Check if the table already exists in the database
    if table_name in db:
        print(f"Table {table_name} already exists in the database")
        table = db[table_name]

    # If it does not exist, create a new table
    else:
        print(f"Creating table {table_name} in the database")

        # Create the table with the given schema
        table = db.create_table(table_name, schema=schema, mode=mode)

        # Define the path of the images and obtain the image URIs
        p = Path(data_path).expanduser()
        uris = [str(f) for f in p.glob("*.jpg")]
        print(f"Found {len(uris)} images in {p}")

        # Sample a specified number of images from the data
        # Increase this value for more accurate results, but it will take more time to process embeddings
        uris = sample(uris, num_samples)

        # Add the data to the table
        print(f"Adding {len(uris)} images to the table")
        table.add(pd.DataFrame({"image_uri": uris}))
        print(f"Added {len(uris)} images to the table")

if __name__ == "__main__":
    # Set up the argument parser for command-line interface
    parser = argparse.ArgumentParser(
        description="Create a table in lancedb with Myntra data"
    )
    # Add arguments for the database path
    parser.add_argument(
        "--database", help="Path to the lancedb database", default="path/to/database"
    )
    # Add arguments for the table name
    parser.add_argument(
        "--table_name", help="Name of the table to be created", default="my_table"
    )
    # Add arguments for the path to the image data
    parser.add_argument(
        "--data_path", help="Path to the Myntra data images", default="path/to/data"
    )
    # Add arguments for the schema to use (default is Myntra)
    parser.add_argument(
        "--schema",
        help="Schema to use for the table. Defaults to Myntra",
        default=Myntra,
    )
    # Add arguments for the mode of table creation
    parser.add_argument(
        "--mode",
        help="Mode for creating the table. Defaults to 'overwrite'",
        default="overwrite",
    )
    # Add arguments for the number of samples to add
    parser.add_argument(
        "--num_samples",
        help="Number of image samples to be added to the table",
        type=int,
        default=1000,
    )
    # Parse the command-line arguments
    args = parser.parse_args()

    # Call the create_table function with parsed arguments
    create_table(
        args.database,
        args.table_name,
        args.data_path,
        args.schema,
        args.mode,
        args.num_samples,
    )
