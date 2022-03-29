def average(grades):
    assert grades == 0
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print("Can't divide by zero")
"""language = [[['John', 'parker'], [90, 80, 70, 60, 50]], [['Bob', 'Rose'], []]]
for i in range(len(language)):
    l = []
    l = language[i]
    a = average(l[1])
    print(a)"""
grades = []
average(grades)