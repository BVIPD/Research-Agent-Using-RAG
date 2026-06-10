def ask_question(query, db, title):
    q = query.lower()

    if "title" in q:
        return title

    if "who am i" in q or "who are you" in q:
        return "I am a research paper assistant. Ask me about the paper!"

    docs = db.similarity_search(query, k=5)
    context = " ".join([doc.page_content for doc in docs])

    if not context.strip():
        return "Not found in document."

    keywords = [w for w in query.lower().split() if len(w) > 2]
    if not any(word in context.lower() for word in keywords):
        return "This topic was not found in the document."

    sentences = []
    for doc in docs:
        for sent in doc.page_content.split("."):
            sent = sent.strip()
            if len(sent) > 20:
                sentences.append(sent)

    scored = []
    for sent in sentences:
        score = sum(1 for w in keywords if w in sent.lower())
        if score > 0:
            scored.append((score, sent))

    if not scored:
        return "Found related content but couldn't extract a specific answer. Try rephrasing."

    scored.sort(reverse=True)
    top = [s for _, s in scored[:2]]
    return " ".join(top)