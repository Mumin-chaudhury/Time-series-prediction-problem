from typing import Set
import re

def tokenize(text: str) -> Set[str]:
    text = text.lower()
    all_words = re.findall(r'\b\w+\b', text)
    return set(all_words)

assert tokenize("Data Science is Science") == {"data", "science", "is"}

