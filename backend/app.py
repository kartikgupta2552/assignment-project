from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS
import docx
import PyPDF2
import io

app = Flask(__name__)
CORS(app)

summarizer = pipeline("summarization")

def extract_text_from_pdf(content):
    reader = PyPDF2.PdfReader(io.BytesIO(content))
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(content):
    doc = docx.Document(io.BytesIO(content))
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return text

def summarize_document(content, filename):
    if filename.endswith('.pdf'):
        text = extract_text_from_pdf(content)
    elif filename.endswith('.docx'):
        text = extract_text_from_docx(content)
    elif filename.endswith('.txt'):
        text = content.decode('utf-8')
    else:
        return "Unsupported file type"

    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# POST API for doc upload
@app.route('/upload/', methods=['POST'])
def upload_file():
    file = request.files['file']
    content = file.read()
    filename = file.filename

    summary = summarize_document(content, filename)

    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True)
