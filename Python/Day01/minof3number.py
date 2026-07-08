a = int(input('first num '))
b = int(input('second num '))
c = int(input('third num '))

if a < b and b < c:
    print("smallest is: ", a)
elif b < c:
    print("smallest is: ", b)
else:
    print("smallest: ", c)