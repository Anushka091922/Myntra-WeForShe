# Myntra-WeForShe
# Myntra Hackathon Project

Welcome to the Myntra Hackathon project! This repository consists of three main use cases aimed at enhancing the search and classification functionalities for fashion-related content.

## Use Cases

### 1. Myntra Search Engine
Developed a search engine specifically for searching fashion-related items on Myntra. It uses a combination of keyword matching and vector search techniques to provide relevant results.

### 2. Advanced Query Option
Implemented an advanced query option to get more accurate and relevant results. This feature leverages advanced AI models to understand the context of the queries better.

### 3. Classification Model
Created a classification model to classify clothes into various categories. This helps in organizing and retrieving fashion items more efficiently.

## Features

- **Vector Embeddings**: Utilizes advanced AI models for converting images and text into searchable embeddings.
- **Multimodal Search**: Supports both text and image queries.
- **Detailed and Context-Aware Responses**: Provides detailed and contextually relevant responses using advanced AI.
- **Streamlit Integration**: Offers a user-friendly interface for interacting with the search and classification functionalities.
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

## How to Run the Project

### Prerequisites

Ensure you have the following installed:
- Python 3.8+
- Streamlit
- Required libraries specified in `requirements.txt`

### Setup Instructions

1. **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/myntra-hackathon-project.git
    cd myntra-hackathon-project
    ```

2. **Create and Activate Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate # For Linux/Mac
    .\venv\Scripts\activate # For Windows
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit Interface**
    ```bash
    streamlit run src/app.py
    ```

## Expected Directory Structure
Ensure your directory structure looks like this:


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

