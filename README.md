# CDP Chatbot

This project implements a chatbot that answers questions about Customer Data Platforms (CDPs) using a Retrieval-Augmented Generation (RAG) approach. The chatbot can provide information about Segment, mParticle, Lytics, and Zeotap.

## Installation

To run this project, you need Python 3.6+ installed on your system. Follow these steps to set up the environment:

1. Create a virtual environment:
   ```
   python -m venv cdp_chatbot_env
   ```

2. Activate the virtual environment:
   - On Windows: `cdp_chatbot_env\Scripts\activate`
   - On macOS and Linux: `source cdp_chatbot_env/bin/activate`

3. Install the required packages:
   ```
   pip install requests beautifulsoup4 numpy sentence-transformers faiss-cpu transformers flask torch
   ```

## Code Explanation

The code consists of several components:

1. **Web Scraping**: The `fetch_and_parse` function uses `requests` and `BeautifulSoup` to scrape and parse documentation from CDP websites.

2. **Document Indexing**: The `build_index` function creates a list of documents from the scraped content.

3. **Embedding**: The code uses the `sentence-transformers` library to create embeddings for the documents and queries.

4. **Similarity Search**: FAISS is used to perform efficient similarity searches on the document embeddings.

5. **Text Generation**: The T5 model from the `transformers` library generates responses based on the retrieved relevant passages.

6. **Flask Web Application**: A simple web interface is provided using Flask, allowing users to interact with the chatbot.

The main workflow is as follows:
- The application builds an index of CDP documentation on startup.
- When a user submits a query, the code detects mentioned CDPs.
- It then retrieves relevant passages using FAISS.
- The T5 model generates a response based on the query and retrieved passages.
- The response is sent back to the user through the web interface.

## Running the Application

To run the application, execute the following command in your terminal:

```
python app.py
```

Then, open a web browser and navigate to `http://localhost:5000` to interact with the chatbot.

## Note

This implementation is a basic example and may require additional error handling and optimizations for production use. Also, ensure you have the necessary permissions to scrape content from the CDP documentation websites.

Citations:
[1] https://mimo.org/glossary/python/requests-library
[2] https://www.firecrawl.dev/blog/how-to-quickly-install-beautifulsoup-with-python
[3] https://pypi.org/project/numpy/
[4] https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
[5] https://engineering.fb.com/2017/03/29/data-infrastructure/faiss-a-library-for-efficient-similarity-search/
[6] https://realpython.com/huggingface-transformers/
[7] https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
[8] https://www.youtube.com/watch?v=ov3RgPLETrM
[9] https://phoenixnap.com/kb/install-numpy
[10] https://sbert.net/docs/installation.html
[11] https://myscale.com/blog/simple-steps-to-install-faiss-using-pip/
[12] https://www.restack.io/p/transformers-answer-install-python-cat-ai
[13] https://phoenixnap.com/kb/install-flask
[14] https://beautiful-soup-4.readthedocs.io/en/latest/
[15] https://en.wikipedia.org/wiki/NumPy
[16] https://pypi.org/project/sentence-transformers/
[17] https://huggingface.co/docs/transformers/en/installation
[18] https://flask.palletsprojects.com/en/stable/patterns/packages/
[19] https://pypi.org/project/requests/
[20] https://pypi.org/project/beautifulsoup4/
[21] https://www.w3schools.com/python/numpy/numpy_intro.asp
[22] https://github.com/UKPLab/sentence-transformers/blob/master/sentence_transformers/SentenceTransformer.py
[23] https://myscale.com/blog/install-faiss-pip-step-by-step-guide/
[24] https://pypi.org/project/transformers/
[25] https://stackoverflow.com/questions/73430167/i-cant-install-or-run-beautifulsoup
[26] https://www.w3schools.com/python/numpy/numpy_getting_started.asp
[27] https://github.com/UKPLab/sentence-transformers/releases
[28] https://ultahost.com/knowledge-base/install-flask-python/
[29] https://github.com/psf/requests/blob/main/docs/user/install.rst
[30] https://stackoverflow.com/questions/67563547/how-to-install-numpy-using-official-python-idle
[31] https://pypi.org/project/faiss-cpu/
[32] https://pypi.org/project/transformers/4.2.0/
[33] https://www.w3schools.com/python/module_requests.asp
[34] https://www.activestate.com/resources/quick-reads/how-to-pip-install-requests-python-package/
