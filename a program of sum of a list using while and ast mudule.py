import ast

x = input('enter your chosen list that contains number: ')
x = ast.literal_eval(x)
while True:
    print(sum(x))
