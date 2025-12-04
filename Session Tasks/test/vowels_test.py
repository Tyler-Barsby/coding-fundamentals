import pytest
from scripts import vowels

def test_simple_word():
    assert vowels.vowels("hello") == 2

def test_mixed_case():
    assert vowels.vowels("Orange") == 3

def test_all_vowels():
    assert vowels.vowels("aeiou") == 5

def test_no_vowels():
    assert vowels.vowels("sky") == 0

def test_empty_string():
    assert vowels.vowels("") == 0

def test_sentence_with_punctuation():
    assert vowels.vowels("Hi!") == 1

def test_invalid_input_number():
    with pytest.raises(AttributeError):
        vowels.vowels(123)