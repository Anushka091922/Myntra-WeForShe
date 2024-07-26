# Myntra-WeForShe
This project demonstrates the simplicity and effectiveness of using vector embeddings, specifically with OpenAI's CLIP model, to create a multimodal search engine capable of understanding and processing both text and image queries.
# Myntra Fashion Search Engine

The **Myntra Fashion Search Engine** makes it easier to find fashion items using the LanceDB vector database. By turning images into searchable embeddings and providing a simple interface with Streamlit, this project shows how to create effective search features for online fashion stores.

## Features
- **Vector Embeddings**: Uses OpenAI's CLIP model to convert images into searchable formats.
- **Multimodal Search**: Allows users to search for fashion items using either text or images.
- **Easy Data Setup**: Simplifies how to define data structures in LanceDB, making it easy to set up and manage the database.
- **Streamlit Integration**: Offers a user-friendly interface for entering search queries through Streamlit.
- **Fast and Accurate Searches**: Handles large amounts of data quickly, providing precise search results.

## How It Works
The project involves a few main steps:
1. **Setting Up CLIP Embeddings**: Configures the CLIP model in LanceDB to convert images into vectors.
2. **Defining Data Structure**: Sets up the structure of the database table, including vector and source fields.
3. **Creating and Managing Tables**: Shows how to create and fill tables in LanceDB.
4. **Running Searches**: Implements features for searching with text and images.
5. **Building a Streamlit App**: Guides you through creating a Streamlit app for user interaction.

## Getting Started
To begin using the Myntra Fashion Search Engine, follow these steps:

### Prerequisites
Make sure you have the following installed:
- Python 3.8 or higher
- LanceDB
- Streamlit
- open-clip-torch

### Installation
First, clone the repository:
```bash
git clone https://github.com/ishandutta0098/lancedb-multimodal-myntra-fashion-search-engine.git

