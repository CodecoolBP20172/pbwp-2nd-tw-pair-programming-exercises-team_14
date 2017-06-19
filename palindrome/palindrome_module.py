def palindrome(str):
    string1=str.lower()
    string1=''.join(string1.split())
    string2=string1[::-1]
    if string1 == string2:
        return True
    else:
        return False    



def main():
    print("Welcome to the Palindrome Checker!")
    userinp=input("Enter a string to check: ")
    result=palindrome(userinp)
    
    if result == True:
        print("Hooray, this is a palindrome!")
    else:
        print("It's been an unsuccessful try, but don't give up!")    
    return


if __name__ == '__main__':
    main()


