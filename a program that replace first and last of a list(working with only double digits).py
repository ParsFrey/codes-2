x = input("enter just the numbers, no ',' (for example= 12345): ") #
b = list(x)
print('The original List: ',b)
b.append(b[0])
b.insert(0,b[-2])
del b[1]
del b[-2]
print('The changed List: ',b)
