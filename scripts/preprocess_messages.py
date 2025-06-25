import re

def clean_amharic_message(text):
    if not text or not isinstance(text, str):
        return ""

    # Normalize whitespace and remove emojis/symbols (except allowed punctuation)
    text = re.sub(r'[^\u1200-\u137F\u0041-\u005A\u0061-\u007A0-9\s.,:-]', '', text)

    # Collapse multiple spaces into one
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def tokenize_amharic_text(text):
    if not text or not isinstance(text, str):
        return []

    # Tokenize by space
    return text.split()