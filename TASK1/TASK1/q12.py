def diamond(n):
    for i in range(1, n+1):
        print(" "*(n-i) + "* " * i)
    for i in range(n-1, 0, -1):
        print(" "*(n-i) + "* " * i)

def butterfly(n):
    for i in range(1, n+1):
        print("*"*i + " "*(2*(n-i)) + "*"*i)
    for i in range(n, 0, -1):
        print("*"*i + " "*(2*(n-i)) + "*"*i)

n = int(input("enter n: "))
n1 = int(input("enter 1 for diamond\nenter 2 for butterfly pattern\n"))
if n1 == 1:
    diamond(n)
else:
    butterfly(n)
