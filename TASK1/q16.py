def pattern(n):
    for i in range(n,0,-1):
        k=1
        for j in range(0,n-1):
          print(i*" ",k)
          k=k+1
    for i in range(0,n-1):
        a=n-1
        for j in range(n,0):
         print(a)
         a=a-1
n=int(input("enter a number\n"))
pattern(n)
