def fibo(n):
 if n==0 or n==1:
  return int(n)
 else:
  return fibo(n-1)+fibo(n-2)
num=int(input("enter a number\n"))
print("the fibo term of the number is",fibo(num))