from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from unstructured.documents.plain_text import PlainTextDocument
from unstructured.partition.auto import partition

app = Flask(_name_)
CORS(app)  # Enable CORS for frontend-backend interaction

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_document():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Parse the document using unstructured.io
    document = PlainTextDocument()
    with open(filepath, 'rb') as f:
        content = partition(f.read())
    document.content = content

    # Return document ID (in a real application, store this in a DB)
    return jsonify({'message': 'File uploaded successfully', 'document': document.content})

@app.route('/query', methods=['POST'])
def query_document():
    data = request.get_json()
    question = data.get('question')
    document_text = data.get('document')

    # Sample NLP processing (using a hypothetical RAG function for demo)
    response = rag_agent(document_text, question)
    return jsonify({'response': response})

# Dummy function simulating RAG Agent querying
def rag_agent(document, question):
    # Here we would typically query a language model or use RAG approach.
    return f"Simulated answer for '{question}' based on document context."

if _name_ == '_main_':
    app.run(debug=True)
