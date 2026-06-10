from pdf_reader import extract_text
from chunker import chunk_text
from vector_store import create_vector_db
from summarizer import summarize
from qa import ask_question


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


def run_pipeline(file_path):
    print("📄 Reading PDF...")
    text = extract_text(file_path)

    title = extract_title(text)
    print("\n📌 TITLE:", title)

    print("\n✂️ Chunking...")
    chunks = chunk_text(text)

    print("🧠 Creating vector DB...")
    db = create_vector_db(chunks)

    print("🤖 Generating summary...")
    summary = summarize(chunks)

    print("\n===== FINAL SUMMARY =====\n")
    print(summary)

    while True:
        query = input("\nAsk something (or type 'exit'): ")
        if query.lower() == "exit":
            break
        answer = ask_question(query, db, title)
        print("\n🤖 Answer:\n", answer)


if __name__ == "__main__":
    run_pipeline("data/Research_DSS.pdf")
