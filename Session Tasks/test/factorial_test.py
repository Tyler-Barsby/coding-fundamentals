import pytest
from scripts import factorial

def test_fact_zero():
    assert factorial.fact(0) == 1
    
def test_fact_one():
    assert factorial.fact(1) == 1
    
def test_fact_ten():
    assert factorial.fact(10) == 3628800
    
def test_fact_string():
    with pytest.raises(TypeError):
        factorial.fact("1")

def test_fact_negative():
    with pytest.raises(ValueError):
        factorial.fact(-1)