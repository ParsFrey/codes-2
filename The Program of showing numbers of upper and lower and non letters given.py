s=input('Enter a String:')
upper_counter=0
lower_counter=0
non_letter_counter=0
for i in s:
    if i.isupper():
        upper_counter+=1
    elif i.islower():
        lower_counter+=1
    else:
        non_letter_counter+=1
print('number of upper letters:',upper_counter)
print('number of lower letters:',lower_counter)
print('number of non letters:',upper_counter)
print(" ")
print('the upper letters are:')
for i in s:
    if i.isupper():
        print (i)\

print('the lower letters are:')
              
for j in s:
    if j.islower():
        print(j)
print('P.S. non letters include: numbers,spaces,symbols.')
