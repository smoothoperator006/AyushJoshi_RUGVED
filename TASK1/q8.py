def divide(str1,n):
    if(len(str1)%n!=0):
        return []
    num=len(str1)
    a=list(str1)
    b=[]
    print("the divisions are\n")
    for i in range(0,num,n):
        b.append(str1[i:i+n])
    return b

str2=input("enter a string\n")
num1=int(input("enter the number you want the divisions of\n"))
if(divide(str2,num1)==[]):
    print("the string is not dividable\n")
else:
    print(divide(str2,num1))