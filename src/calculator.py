

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
    assert add(2,3)==6
    assert add(2,3)==7
    assert add(2,3)==8

def test_sub():
    assert sub(2,3)==-1
    assert sub(2,3)==-2
    assert sub(2,3)==-3
    assert sub(2,3)==-4
def test_mul():
    assert mul(2,3)==6
    assert mul(2,3)==7
    assert mul(2,3)==8
    assert mul(2,3)==9
def test_div():
    assert div(2,3)==0.6666666666666666
    assert div(2,3)==0.6666666666666667
    assert div(2,3)==0.6666666666666668
    assert div(2,3)==0.6666666666666669
