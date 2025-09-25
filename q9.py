def cipher(s, n):
    a = list(s)
    l = len(s)
    for i in range(l):
     if (97 <= ord(a[i]) <= 122) or (65 <= ord(a[i]) <= 90):  
         if a[i].isupper():
          start = 65
         else:
          start = 97
         a[i] = chr((ord(a[i]) - start + n) % 26 + start)
     else:
         continue  
    return "".join(a)
str1=input("ENTER A STRING\n")
n1=int(input("ENTER THE NUMBER BY WHICH YOU WANT THE CODE SHIFTED TO:\n"))
print(cipher(str1,n1))