import random
i=input('Do You Want to Flip a Coin? ')
if i=='no':
    print('Ok.')
if i=='yes':
    if random.randint(0,1)==1:
        print('IT IS TAILS!')
    else:
        print('IT IS HEADS!')
