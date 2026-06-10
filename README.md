# 🔍 Research Agent Using RAG

An intelligent **Retrieval-Augmented Generation (RAG)** system designed to assist researchers by enabling document-aware conversations with research papers. Users can upload PDF documents, generate concise summaries, and ask context-specific questions powered by Large Language Models (LLMs).

---

## ✨ Key Features

📄 **Research Paper Processing**
Extracts and processes text from uploaded PDF documents.

✂️ **Intelligent Text Chunking**
Splits large documents into meaningful chunks for efficient retrieval.

🧠 **Semantic Search with Vector Embeddings**
Stores document embeddings using **ChromaDB** for fast and relevant information retrieval.

❓ **Question Answering over Documents**
Allows users to ask natural language questions and receive context-aware answers.

📝 **Automatic Summarization**
Generates concise summaries of lengthy research papers.

🌐 **Interactive Web Interface**
Provides an easy-to-use Flask-based interface for document upload and interaction.

---

## 🏗️ System Architecture

```text
PDF Upload
     ↓
Text Extraction
     ↓
Chunking
     ↓
Embedding Generation
     ↓
ChromaDB Vector Store
     ↓
Retriever
     ↓
Gemini LLM
     ↓
Answers & Summaries
```

---

## 🛠️ Tech Stack

| Category            | Technologies               |
| ------------------- | -------------------------- |
| Backend             | Python, Flask              |
| LLM Framework       | LangChain                  |
| Vector Database     | ChromaDB                   |
| Language Model      | Google Gemini API          |
| Document Processing | PyPDF                      |
| Frontend            | HTML, CSS, Jinja Templates |

---

## 📂 Project Structure

```text
Research-Agent-Using-RAG/
│
├── backend/
│   ├── app.py
│   ├── main.py
│   ├── pdf_reader.py
│   ├── chunker.py
│   ├── vector_store.py
│   ├── qa.py
│   ├── summarizer.py
│   └── templates/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/BVIPD/Research-Agent-Using-RAG.git
cd Research-Agent-Using-RAG
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 4. Run the Application

```bash
python backend/app.py
```

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

---

## 🎯 Use Cases

* Academic research assistance
* Literature review support
* Research paper summarization
* Knowledge extraction from PDFs
* Context-aware document question answering

---

## 📌 Future Enhancements

* [ ] Multi-document querying
* [ ] Citation generation
* [ ] User authentication
* [ ] Research paper recommendation system
* [ ] Deployment on cloud platforms

---

## 👩‍💻 Author

**Indira Priyadarshini**
Computer Science Engineering Student | Cloud & AI Enthusiast

GitHub: https://github.com/BVIPD

---

⭐ If you found this project useful, consider giving it a star!
