def greet():
    print("i love coding")

greet()

scope_out = "outside"

def test_scope():
    print(scope_out)

test_scope()

def test_scope1():
    scope_in = "inside"

print()