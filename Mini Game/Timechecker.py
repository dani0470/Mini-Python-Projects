import time
timest=time.strftime('%H : %M : %S')
print(timest) # the time is stored as a string in "timest" variable
timest=time.strftime('%H hours')
print(timest)
timest=time.strftime('%M minutes')
print(timest)
timest=time.strftime('%S seconds')
print(timest)
hou=time.strftime('%H')
timest=int(hou)
if(timest>=6 and timest<=11):
    print("Good Morning")
elif(timest>=12 and timest<=15):
    print("Good AfterNoon")
elif(timest>=16 and timest<=19):
    print("Good Eveninng")
elif((timest>=20 and timest<=24) and (timest>=0 and timest<=5)):
    print("Good Night")
else:
    print("Invalid Command")
input()