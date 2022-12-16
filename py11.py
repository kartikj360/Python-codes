def reverse(a):
    str=""
    for i in(a):
        str=i+str
    return str


def palin(a):
    c=reverse(a)
    if c==a:
        return True
    else:
        return False

a=input("Enter the word to be checked: ")
print("Is the string a palindrome?? :",palin(a))            