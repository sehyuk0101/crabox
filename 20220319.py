"""try:
    a = int(input("Tell me your number:"))
    b = int(input("Tell me another number:"))
    print(a/b)
except:
    print("Bug in user input.")

try:
    a = int(input("Tell me your number:"))
    b = int(input("Tell me another number:"))
    print("a/b =",a/b)
    print("a+b =",a+b)
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Cant divide by zero.")
except:
    print("Something went very wrong.")"""

def get_ratios(L1, L2):
    ratios = []
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError('get_ratios called with bad arg')
        else:
            print("success")
        finally:
            print("executed no matter what!")
    return ratios
get_ratios([1,1], [1,1])