import pytest
from src.preprocessing.clean import clean_text, remove_html_tags, normalize_whitespace, batch_clean

def test_removes_html():
    assert remove_html_tags("<b>hello</b>") == "hello"

def test_lowercase():
    assert clean_text("HELLO") == "hello"

def test_empty_string():
    assert clean_text("") == ""

def test_whitespace_only():
    assert clean_text("   ") == ""

def test_type_error():
    with pytest.raises(TypeError):
        clean_text(123)

def test_batch_clean():
    assert batch_clean(["HELLO", "<b>world</b>"]) == ["hello", "world"]

def test_normalize_whitespace():
    assert normalize_whitespace("too  many   spaces") == "too many spaces"
 