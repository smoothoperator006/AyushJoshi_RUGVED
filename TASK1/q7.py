def fibo(n):
 if n==0 or n==1:
  return int(n)
 else:
  return fibo(n-1)+fibo(n-2)
num=int(input("Enter a number upto which the fibonacci series will be displayed\n"))
print("the fibonacci terms are:\n")
for i in range(0,num+1):
 print(fibo(i))