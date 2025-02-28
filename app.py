import requests
from bs4 import BeautifulSoup
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
from transformers import T5Tokenizer, T5ForConditionalGeneration
from flask import Flask, request, jsonify, send_from_directory

# CDP documentation URLs
CDP_URLS = {
    "Segment": "https://segment.com/docs/",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

# Fetch and parse documentation
def fetch_and_parse(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    sections = []
    current_section = None
    for element in soup.find_all(['h1', 'h2', 'h3', 'p', 'ul', 'ol']):
        if element.name in ['h1', 'h2', 'h3']:
            if current_section:
                sections.append(current_section)
            current_section = {'title': element.get_text().strip(), 'content': ''}
        elif current_section and element.name in ['p', 'ul', 'ol']:
            current_section['content'] += element.get_text().strip() + '\n'
    if current_section:
        sections.append(current_section)
    return sections

# Build document index
def build_index():
    documents = []
    for cdp, url in CDP_URLS.items():
        sections = fetch_and_parse(url)
        for section in sections:
            documents.append({'cdp': cdp, 'title': section['title'], 'content': section['content']})
    return documents

# Initialize RAG components
embedder = SentenceTransformer('all-MiniLM-L6-v2')
tokenizer = T5Tokenizer.from_pretrained('t5-small')
model = T5ForConditionalGeneration.from_pretrained('t5-small')
documents = build_index()
contents = [doc['content'] for doc in documents]
embeddings = embedder.encode(contents)
embeddings = np.array(embeddings)
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Detect CDPs in query
def detect_cdps(query):
    return [cdp for cdp in CDP_URLS.keys() if cdp.lower() in query.lower()]

# Generate response with T5
def generate_response(query, passages):
    context = " ".join(passages)
    input_text = f"question: {query} context: {context}"
    input_ids = tokenizer.encode(input_text, return_tensors='pt', max_length=512, truncation=True)
    output = model.generate(input_ids, max_length=200)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Flask app
app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/ask', methods=['POST'])
def ask():
    query = request.json['query']
    cdps = detect_cdps(query)
    if not cdps:
        return jsonify({"response": "Please specify a CDP (Segment, mParticle, Lytics, or Zeotap) in your question."})
    query_embedding = embedder.encode([query])
    D, I = index.search(query_embedding, 100)  # Retrieve top-100 candidates
    if len(cdps) == 1:
        cdp = cdps[0]
        relevant_indices = [i for i in I[0] if documents[i]['cdp'] == cdp]
        top_k_indices = relevant_indices[:3]  # Top-3 relevant sections
        passages = [documents[i]['content'] for i in top_k_indices]
        response = generate_response(query, passages)
        return jsonify({"response": f"For {cdp}: {response}"})
    else:
        responses = []
        for cdp in cdps:
            relevant_indices = [i for i in I[0] if documents[i]['cdp'] == cdp]
            top_k_indices = relevant_indices[:3]
            passages = [documents[i]['content'] for i in top_k_indices]
            response = generate_response(query, passages)
            responses.append(f"For {cdp}: {response}")
        return jsonify({"response": "\n".join(responses)})

if __name__ == '__main__':
    app.run(debug=True)