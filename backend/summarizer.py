from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "facebook/bart-large-cnn"

tokenizer = None
model = None


def load_model():
    global tokenizer, model
    if tokenizer is None:
        print("🔄 Loading summarization model...")
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


def summarize(chunks):
    load_model()
    text = " ".join(chunks[1:6])
    words = text.split()
    if len(words) > 900:
        text = " ".join(words[:900])
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=1024)
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=150,
        min_length=60,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True,
        forced_bos_token_id=0
    )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)