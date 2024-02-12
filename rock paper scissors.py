x = input('what will player 1 choose? ')
y = input('what will player 2 choose? ')

p1 = 'player 1 wins!'
p2 = 'player 2 wins!'
D = 'Draw.'

if x == 'scissors' and y == 'paper':
    print(p1)
if x == 'scissors' and y == 'scissors':
    print(D)
if x == 'scissors' and y == 'rock':
    print(p2)
if x == 'rock' and y == 'paper':
    print(p2)
if x == 'rock' and y == 'scissors':
    print(p1)
if x == 'rock' and y == 'rock':
    print(D)
if x == 'paper' and y == 'paper':
    print(D)
if x == 'paper' and y == 'scissors':
    print(p2)
if x == 'paper' and y == 'rock':
    print(p1)
