from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

summarizer = pipeline("summarization")

def summarize_document(content):
    text = content.decode('utf-8')
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']


# POST api for doc upload
@app.route('/upload/', methods=['POST'])
def upload_file():
    file = request.files['file']
    content = file.read()
    
    summary = summarize_document(content)
    
    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True)
