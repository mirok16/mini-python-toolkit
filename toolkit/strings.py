# toolkit/strings.py
def to_upper(text):
    return text.upper()
def reverse(text):
    return text[::-1]
def length(text):
    return len(text)
from toolkit.strings import to_upper

def test_upper():
    assert to_upper("hi") == "HI"
