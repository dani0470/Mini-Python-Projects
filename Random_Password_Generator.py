from random import choice
alp="""abcdefghijklm67890nopqrstuvwxyz
ABCDEF12345GHIJKLMNO@~:!^&*_+PQRSTUVWXYZ"""
#alp variable contains all Capital and small characters all digits(0-9) and some symbols 
while True:
    try:
        x=int(input("Enter the password length (number) :"))
        break
    except Exception as e:
            print(e)
            continue
if (x>=4):
    pasw=""
    for i in range(x):
        pasw = pasw + choice(alp)
    print("Password Generated :",pasw)
else:
     print("Password must have length greater than 3 characters")

input()