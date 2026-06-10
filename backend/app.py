from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from pdf_reader import extract_text
from chunker import chunk_text
from vector_store import create_vector_db
from summarizer import summarize
from qa import ask_question

app = Flask(__name__)
CORS(app)

DB = None
TITLE = ""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(BASE_DIR, "..", "data")
os.makedirs(DATA_FOLDER, exist_ok=True)


def extract_title(text):
    lines = [l.strip() for l in text.split("\n") if l.strip()]
    candidate_parts = []
    for line in lines[:15]:
        if any(skip in line.lower() for skip in ["abstract", "introduction", "keywords", "doi", "http", "@", "vol.", "issn"]):
            continue
        if len(line) < 5 or len(line) > 200:
            continue
        candidate_parts.append(line)
        if len(candidate_parts) >= 2:
            break
    if candidate_parts:
        full_title = " ".join(candidate_parts)
        if len(full_title) < 250:
            return full_title
        return candidate_parts[0]
    return "Title not found"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_pdf():
    global DB, TITLE
    try:
        file = request.files["file"]
        save_path = os.path.join(DATA_FOLDER, file.filename)
        file.save(save_path)

        text = extract_text(save_path)
        TITLE = extract_title(text)
        chunks = chunk_text(text)

        # Reset DB completely on every new upload
        DB = create_vector_db(chunks, reset=True)

        summary = summarize(chunks)
        return jsonify({"title": TITLE, "summary": summary})

    except Exception as e:
        print("UPLOAD ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


@app.route("/ask", methods=["POST"])
def ask():
    global DB, TITLE
    try:
        if DB is None:
            return jsonify({"answer": "Please upload a PDF first."})
        data = request.json
        question = data["question"]
        answer = ask_question(question, DB, TITLE)
        return jsonify({"answer": answer})
    except Exception as e:
        print("QUESTION ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
