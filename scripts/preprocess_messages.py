import re

def normalize_amharic_text(text):
    if not text:
        return ""
    text = re.sub(r'[^\u1200-\u137F\s]', '', text)  # Keep only Amharic characters and spaces
    text = re.sub(r'\s+', ' ', text).strip()        # Normalize whitespace
    return text