# app.py
# This is a test commit
def add(a, b):
    return a + b

print('hello github actions')

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
