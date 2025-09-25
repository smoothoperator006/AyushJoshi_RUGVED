def luhn_check(n):
    l=len(n)
    n=int(n)
    remt=[]
    sum1=0
    for i in range(0,l):
     rem=int(n%10)
     n=n//10
     if(i%2!=0):
        rem=rem*2
        if(rem>9):
         rem=rem-9
     remt.append(rem)
     sum1=sum1+rem
    return (sum1%10==0)
num=input("Enter a number\n")
if(luhn_check(num)):
  print("The number is a valid credit no\n")
else:
   print("The number is not a valid credit cars no\n")
