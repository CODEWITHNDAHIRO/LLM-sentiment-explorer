"""
Text preprocessing module for NLP sentiment analysis.
Provides cleaning, normalization, and tokenization utilities.
"""

import re
import string
from typing import List, Optional


def remove_html_tags(text: str) -> str:
    """Remove HTML tags from text."""
    return re.sub(r'<.*?>', '', text)


def remove_special_characters(text: str, keep_punctuation: bool = False) -> str:
    """Remove special characters, optionally keeping punctuation."""
    if keep_punctuation:
        return re.sub(r'[^a-zA-Z0-9\s\.,!?]', '', text)
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)


def normalize_whitespace(text: str) -> str:
    """Collapse multiple spaces and strip leading/trailing whitespace."""
    return re.sub(r'\s+', ' ', text).strip()


def clean_text(
    text: str,
    lowercase: bool = True,
    remove_html: bool = True,
    remove_special: bool = True,
    keep_punctuation: bool = False,
) -> str:
    """
    Full text cleaning pipeline for NLP preprocessing.

    Args:
        text: Raw input text
        lowercase: Convert to lowercase (default True)
        remove_html: Strip HTML tags (default True)
        remove_special: Remove special characters (default True)
        keep_punctuation: Preserve .,!? when removing specials

    Returns:
        Cleaned text string

    Example:
        >>> clean_text("Hello! <b>World</b> 123")
        'hello world 123'
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")
    if not text.strip():
        return ""

    if remove_html:
        text = remove_html_tags(text)
    if lowercase:
        text = text.lower()
    if remove_special:
        text = remove_special_characters(text, keep_punctuation)

    text = normalize_whitespace(text)
    return text


def batch_clean(texts: List[str], **kwargs) -> List[str]:
    """
    Apply clean_text to a list of texts.

    Args:
        texts: List of raw text strings
        **kwargs: Passed to clean_text

    Returns:
        List of cleaned strings
    """
    return [clean_text(t, **kwargs) for t in texts]


if __name__ == "__main__":
    # Quick smoke test
    samples = [
        "Hello! <b>This is a test</b>",
        "  Multiple   spaces   here  ",
        "Special @#$ chars & symbols!",
        "",
    ]
    for s in samples:
        print(f"IN:  {repr(s)}")
        print(f"OUT: {repr(clean_text(s))}")
        print()