import pyfiglet
while True:
    T = input("Enter Text you want to convert to ASCII art : ")
    result = pyfiglet.figlet_format(T, font = 'cli8x8' ) 
    print(result) 
