

def add(a,b):
    return a+b
def sub(a,b,):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def test_add():
    assert add(2,3)==5
    assert add(10,9)==19
    assert add(5,5)==10
    
def test_sub():
    assert sub(5,3)==2
    assert sub(10,9)==1
    assert sub(5,5)==0
def test_mul():
    assert mul(5,3)==15
    assert mul(10,9)==90
    assert mul(5,5)==25
    
def test_div():
    assert div(6,3)==2
    assert div(10,5)==2
    assert div(5,5)==1