a = 1
b = a
print(a)
print(b)

warm = ['red', 'yellow', 'orange']
hot = warm
hot.append('pink')
print(hot)
print(warm)

cool = ['blue', 'green', 'grey']
chill = cool[:]
chill.append('black')
print(chill)
print(cool)

warm = ['red', 'yellow', 'orange']
sortedwarm = warm.sort()
print(warm)
print(sortedwarm)

cool = ['grey', 'green', 'blue']
sortedcool = sorted(cool)
print(cool)
print(sortedcool)

L1 = [1,2,3,4]
L2 = [1,2,5,6]

def remove_dups(L1,L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
print(L1)
print(L2)

def remove_dups(L1,L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)
print(L1)
print(L2)

for e in L2:
    print(e)