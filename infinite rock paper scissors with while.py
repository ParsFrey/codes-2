x = input('what will player 1 choose? ')
y = input('what will player 2 choose? ')

p1 = 'player 1 wins!'
p2 = 'player 2 wins!'
D = 'Draw.'

p = 'paper'
s = 'scissors'
r = 'rock'

while x == 's' and y == 'p':
    print(p1)
while x == 's' and y == 's':
    print(D)
while x == 's' and y == 'r':
    print(p2)
while x == 'r' and y == 'p':
    print(p2)
while x == 'r' and y == 's':
    print(p1)
while x == 'r' and y == 'r':
    print(D)
while x == 'p' and y == 'p':
    print(D)
while x == 'p' and y == 's':
    print(p2)
while x == 'p' and y == 'r':
    print(p1)

