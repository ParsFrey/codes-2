x = input('enter your email address:')
if x.count('@') and x[-4:] == '.com':
    print('It is a valid Email address.')
else:
    print('IT IS NOT a correct Email address!')
