import argparse  # Importing argparse for command line argument parsing
import os  # Importing os for interacting with the operating system
from typing import Any  # Importing Any for flexible type hinting
from PIL import Image  # Importing Image from PIL for image handling

import lancedb  # Importing LanceDB for database operations

from schema import Myntra, get_schema_by_name  # Importing schema definitions and retrieval function


def run_vector_search(
    database: str,
    table_name: str,
    schema: Any,
    search_query: Any,
    limit: int = 6,
    output_folder: str = "output",
) -> None:
    """
    This function performs a vector search on the specified database and table using the provided search query.
    The search can be performed on either text or image data. The function retrieves the top 'limit' number of results
    and saves the corresponding images in the 'output_folder' directory. The function assumes if the search query ends 
    with '.jpg' or '.png', it is an image search, otherwise it is a text search.

    Args:
        database (str): The path to the database.
        table_name (str): The name of the table.
        schema (Schema): The schema to use for converting search results to Pydantic models.
        search_query (Any): The search query, can be text or image.
        limit (int, optional): The maximum number of results to return. Defaults to 6.
        output_folder (str, optional): The folder to save the output images. Defaults to "output".

    Returns:
        None

    Usage:
    >>> run_vector_search(database="~/.lancedb", table_name="myntra", schema=Myntra, search_query="Black Kurta")
    """

    # Create the output folder if it does not exist
    if os.path.exists(output_folder):  # Check if the output folder already exists
        # If it exists, remove all files in the output folder
        for file in os.listdir(output_folder):
            os.remove(os.path.join(output_folder, file))
    else:
        os.makedirs(output_folder)  # Create the output folder if it does not exist

    # Connect to the lancedb database
    db = lancedb.connect(database)

    # Open the specified table in the database
    table = db.open_table(table_name)

    # Check if the search query is an image or text based on file extension
    try:
        if search_query.endswith(".jpg") or search_query.endswith(".png"):
            search_query = Image.open(search_query)  # Open the image if it's a file
        else:
            search_query = search_query  # Otherwise, keep it as text
    except AttributeError as e:
        # Handle the case where the search query is already an image object
        if str(e) == "'JpegImageFile' object has no attribute 'endswith'":
            print("Running via Streamlit, search query is already an array so skipping opening image using Pillow")
        else:
            raise  # Raise any other unexpected exceptions

    # Perform the vector search on the table using the search query and retrieve the results
    rs = table.search(search_query).limit(limit).to_pydantic(schema)

    # Save the retrieved images to the output folder
    for i in range(limit):
        image_path = os.path.join(output_folder, f"image_{i}.jpg")  # Define the output image path
        rs[i].image.save(image_path, "JPEG")  # Save the image using JPEG format


if __name__ == "__main__":
    # Initialize argument parser
    parser = argparse.ArgumentParser(description="Vector Search")
    
    # Define command line arguments
    parser.add_argument("--database", type=str, help="Path to the database")  # Path to the database
    parser.add_argument("--table_name", type=str, help="Name of the table")  # Name of the table in the database
    parser.add_argument(
        "--schema", type=str, help="Schema of the table", default="Myntra"  # Schema for the table (default: Myntra)
    )
    parser.add_argument("--search_query", type=str, help="Search query")  # Search query (text or image path)
    parser.add_argument(
        "--limit", type=int, default=6, help="Limit the number of results (default: 6)"  # Limit for search results
    )
    parser.add_argument(
        "--output_folder", type=str, default="output", help="Output folder path"  # Path for saving output images
    )

    # Parse the command line arguments
    args = parser.parse_args()

    # Retrieve the schema class based on the provided schema name
    schema = get_schema_by_name(args.schema)
    if schema is None:
        raise ValueError(f"Unknown schema: {args.schema}")  # Raise error if schema is unknown

    # Run the vector search with the provided arguments
    run_vector_search(
        args.database,
        args.table_name,
        schema,
        args.search_query,
        args.limit,
        args.output_folder,
    )
