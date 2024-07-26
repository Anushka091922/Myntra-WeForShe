from typing import Any  # Importing Any for type hinting to indicate any data type
from lancedb.pydantic import LanceModel, Vector  # Importing necessary classes from lancedb.pydantic for defining models
from PIL import Image  # Importing Image from PIL for image handling

from embedding_model import register_model  # Importing the function to register embedding models

# Register the OpenAI CLIP model using the register_model function
clip = register_model("open-clip")  # This creates an instance of the OpenAI CLIP model for embedding

class Myntra(LanceModel):
    """
    Represents a Myntra Schema for items in the database.

    Attributes:
        vector (Vector): The vector representation of the item.
        image_uri (str): The URI of the item's image.
    """

    # Define the vector field using the registered CLIP model's dimensionality
    vector: Vector(clip.ndims()) = clip.VectorField()  # This initializes a vector field with dimensions defined by the CLIP model
    # Define the image URI field, which stores the path to the item's image
    image_uri: str = clip.SourceField()  # This initializes a source field for image URI

    @property
    def image(self) -> Image:
        """
        Loads the image from the image URI.

        Returns:
            Image: The loaded image object.

        Usage:
        >>> item = Myntra(image_uri="path/to/image.jpg")
        >>> img = item.image  # Loads the image corresponding to the URI
        """
        return Image.open(self.image_uri)  # Opens and returns the image at the specified URI

# Function to map schema name to schema class
def get_schema_by_name(schema_name: str) -> Any:
    """
    Retrieves the schema object based on the given schema name.

    Args:
        schema_name (str): The name of the schema.

    Returns:
        object: The schema object corresponding to the given schema name, or None if not found.

    Usage:
    >>> schema = get_schema_by_name("Myntra")  # Example of retrieving the Myntra schema class
    """
    # Mapping schema names to their corresponding schema classes
    schema_map = {
        "Myntra": Myntra,  # Mapping the string "Myntra" to the Myntra class
    }
    return schema_map.get(schema_name)  # Return the corresponding schema class or None if not found
