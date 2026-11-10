#what makes a good password - length, letters, lowercase, uppercase, numbers, special characters
print("your password should: ",end = "")
print("be greater than 8 characters and less than 15 characters ")
print("have at least one upper case and at least one lower case letter ")
print("have at least one number and ", end = '')
print("have at least one of the following special characters ",end='')
print("*, @, %,&")
pw = input("enter your choice for a password: ")
length = len(pw)
lgth = False
if length >= 8 and length <= 15:
    lgth = True
uppcase = False
lowcase = False
num = False
spChar = False
for char in pw:
    print("letter is "+ char)
    if char.isdigit():
        num = True
    if char.isupper():
        uppcase = True
    if char.islower():
        lowcase = True
    if char == '*' or char == '&' or char == '%' or char == '@':
        spChar = True
if not lgth:
    print("password fails because of length ",length)
elif not uppcase:
    print("password does not have an upper case letter")
elif not lowcase:
    print("password does not have a lower case letter")
elif not num:
    print("password does not have a number")
elif not spChar:
    print("password does not a required special character")
else:
    print("your password passes")
