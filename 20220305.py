def multi_iter(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result
c = multi_iter(1, 3)
print(c)

def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a,b-1)
d = mult(1, 3)
print(d)