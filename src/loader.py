# src/loader.py

import re

def load_document(path: str) -> str:
    """
    Load text file and return cleaned string.
    """

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Clean excessive whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()
