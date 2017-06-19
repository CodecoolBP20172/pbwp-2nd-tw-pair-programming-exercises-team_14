import string
import random

def passwordgen():
    chars=string.printable
    chars=list(chars)
    length=len(string.printable[:-7])
    password=[]
    i=0
    while i != 8:
        randomnum=random.randint(1,length)
        password.append(chars[randomnum])
        i+=1    
    password.extend(["A","k","3","%"])     
    password = ''.join(password)
    return(password)


def main():
    print("Password Generator")
    while True:
        input("Press enter to get a new password!")
        print(passwordgen())

if __name__ == '__main__':
    main()


