from random import choice
print("                     Clash Of Legends")
l1=["Snake","Water","Gun"]
while True:
    ch=choice(l1)
    y=input("\nEnter Your Option\n1:Snake\n2:Water\n3:Gun\n")
    if(y=="1"):
        x="Snake"
    elif(y=="2"):
        x="Water"
    elif(y=="3"):
        x="Gun"
    else:
        print("Invalid Command")
        k=input("\nEnter q to Quit or other key To Continue :")
        if(k=="q"):
            break
        else:
            continue 
    if(x=="Gun" and ch=="Gun"):
        print(x,"VS",ch)
        print("Match Draw")
        k=input("\nEnter q to Quit or other key To Continue :")
        if(k=="q"):
            break
        else:
            continue
    elif(x=="Snake" and ch=="Snake"):
        print(x,"VS",ch)
        print("Match Draw")
        k=input("\nEnter q to Quit or other key To Continue :")
        if(k=="q"):
            break
        else:
            continue
    elif(x=="Water" and ch=="Water"):
        print(x,"VS",ch)
        print("Match Draw")
        k=input("\nEnter q to Quit or other key To Continue :")
        if(k=="q"):
            break
        else:
            continue
    elif(x=="Gun" and ch=="Snake"):
        print(x,"VS",ch)
        print("You Won")
        k=input("\nEnter q to Quit or other key To Continue :")
        if(k=="q"):
            break
        else:
            continue
    elif(x=="Gun" and ch=="Water"):
        print(x,"VS",ch)
        print("You Loose")
        k=input("\nEnter q to Quit or other key To Continue :")
        if(k=="q"):
            break
        else:
            continue
    elif(x=="Water" and ch=="Gun"):
        print(x,"VS",ch)
        print("You Won")
        k=input("\nEnter q to Quit or other key To Continue :")
        if(k=="q"):
            break
        else:
            continue
    elif(x=="Water" and ch=="Snake"):
        print(x,"VS",ch)
        print("You Loose")
        k=input("\nEnter q to Quit or other key To Continue :")
        if(k=="q"):
            break
        else:
            continue
    elif(x=="Snake" and ch=="Water"):
        print(x,"VS",ch)
        print("You Won")
        k=input("\nEnter q to Quit or other key To Continue :")
        if(k=="q"):
            break
        else:
            continue
    elif(x=="Snake" and ch=="Gun"):
        print(x,"VS",ch)
        print("You Loose")
        k=input("\nEnter q to Quit or other key To Continue :")
        if(k=="q"):
            break
        else:
            continue
    else:
        print("Error")
        break