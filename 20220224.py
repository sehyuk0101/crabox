def mult_iter(a, b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result
a = 1
b = 2
c = mult_iter(a, b)
print(c)

def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b - 1)
a = 2
b = 3
c = mult(a, b)
print(c)

def fact(a):
    if a == 1:
        return 1
    else:
        return a*fact(a - 1)
a = 4
print(fact(a))