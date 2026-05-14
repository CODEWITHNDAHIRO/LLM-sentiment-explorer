import re

def clean_text(text: str) -> str:
    """
    Basic text cleaning for NLP.
    - Removes HTML tags
    - Removes special characters
    - Lowercases the text
    """
    text = re.sub(r'<.*?>', '', text)  # Remove HTML
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alpha
    return text.lower().strip()

if __name__ == "__main__":
    sample = "Hello! This is a <b>Sample</b> text for the LLM project."
    print(f"Original: {sample}")
    print(f"Cleaned: {clean_text(sample)}")