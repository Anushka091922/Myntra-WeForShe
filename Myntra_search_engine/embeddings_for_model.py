from typing import Any
from lancedb.embeddings import EmbeddingFunctionRegistry

def register_model(model_name: str) -> Any:
    """
    Register a model with the given name using LanceDB's EmbeddingFunctionRegistry.

    This function retrieves a model from the LanceDB's embedding function registry
    by its name and creates an instance of the model.

    Args:
        model_name (str): The name of the model to register. This should match
                          a registered model name in the EmbeddingFunctionRegistry.

    Returns:
        Any: The registered model instance. The specific type will depend on the 
             model being registered.

    Usage:
    >>> model = register_model("open-clip")
    """
    # Retrieve the singleton instance of the EmbeddingFunctionRegistry
    registry = EmbeddingFunctionRegistry.get_instance()
    
    # Fetch the embedding function corresponding to the provided model name
    model_function = registry.get(model_name)
    
    # Create an instance of the model using the fetched embedding function
    model = model_function.create()
    
    # Return the created model instance
    return model
