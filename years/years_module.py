import datetime



def years(age):
    result =datetime.date.today().year + (99 - age)
    return(result)


def main():
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    date100=years(age)
    print("Dear {0}, you are going to be 100 years old in {1}!".format(name,date100))
    
    return


if __name__ == '__main__':
    main()
