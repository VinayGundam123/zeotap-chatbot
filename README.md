# CDP Support Agent Chatbot

This project implements a chatbot designed to answer "how-to" questions related to four Customer Data Platforms (CDPs): Segment, mParticle, Lytics, and Zeotap. The chatbot extracts relevant information from the official documentation of these CDPs to guide users on how to perform tasks or achieve specific outcomes within each platform.

## Requirements

To run this project, you need:

- Python 3.6+
- pip (Python package installer)

The main dependencies are:

- Flask: For creating the web application
- BeautifulSoup: For web scraping
- NumPy: For numerical operations
- sentence-transformers: For text embedding
- faiss-cpu: For efficient similarity search
- transformers: For text generation using T5 model

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv cdp_chatbot_env
   ```
3. Activate the virtual environment
4. Install the required packages:
   ```
   pip install requests beautifulsoup4 numpy sentence-transformers faiss-cpu transformers flask torch
   ```

## Code Flow

The main.py file follows this flow:

1. **Import and Setup**: 
   - Import necessary libraries
   - Define CDP documentation URLs

2. **Web Scraping**:
   - `fetch_and_parse` function scrapes content from CDP documentation

3. **Document Indexing**:
   - `build_index` function creates a searchable index of scraped content

4. **Embedding and Indexing**:
   - Initialize SentenceTransformer for text embedding
   - Create FAISS index for efficient similarity search

5. **Query Processing**:
   - `detect_cdps` function identifies mentioned CDPs in user queries
   - `generate_response` function uses T5 model to generate answers

6. **Flask Web Application**:
   - Set up routes for serving the HTML interface and handling API requests
   - `/ask` endpoint processes user queries and returns chatbot responses

7. **Main Workflow**:
   - User submits a query
   - System detects mentioned CDPs
   - Retrieves relevant passages using FAISS
   - Generates response using T5 model
   - Returns response to user

This implementation demonstrates a complete pipeline from data ingestion (web scraping) to user interaction (web interface), showcasing skills in web development, natural language processing, and information retrieval.

## Usage

Run the application:
```
python main.py
```
Access the chatbot interface at `http://localhost:5000` in your web browser.
