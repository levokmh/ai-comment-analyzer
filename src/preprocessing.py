import re
import unicodedata


def clean_text(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = text.strip()

    text = unicodedata.normalize("NFKD", text)
    text = "".join(char for char in text if not unicodedata.combining(char))

    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s']", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text