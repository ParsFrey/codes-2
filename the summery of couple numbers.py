import ast

a = input('the list of noombers: ')
a = ast.literal_eval(a)
x = sum(a)/len(a)
print(x)
