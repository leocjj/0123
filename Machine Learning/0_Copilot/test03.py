"""
Try to guess the output of the following code:
y = 1
def f(x):
    return x * y
print(f(1))
y = 2
print(f(1))
y = None
print(f(1))

Create a test for the following code:
def calculate_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:   
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def test_calculate_fibonacci():
    assert calculate_fibonacci(0) == 0
    assert calculate_fibonacci(1) == 1
    assert calculate_fibonacci(2) == 1
    assert calculate_fibonacci(3) == 2
    assert calculate_fibonacci(4) == 3
    assert calculate_fibonacci(5) == 5
    assert calculate_fibonacci(6) == 8
    assert calculate_fibonacci(7) == 13
    assert calculate_fibonacci(8) == 21

"""