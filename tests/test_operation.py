from src.math_operations import addition,substraction

def test_addition():
    assert addition(2,3)==5
    assert addition(-1,4)==3
    
def test_substraction():
    assert substraction(5,3)==2
    assert substraction(-1,5)==-6