def sort(s):
 chars=list(s)
 n=len(s)
 for i in range (n-1):
  low=i
  for j in range(i+1,n):
   if(ord(chars[j])<ord(chars[low])):
    low=j
  temp=chars[low]
  chars[low]=chars[i]
  chars[i]=temp
 return ''.join(chars)
def anagram(a,b):
 l1=int(len(a))
 l2=int(len(b))
 if(l1!=l2):
  return False
 return (sort(a)==sort(b))
str1=input("enter 1st string\n")
str2=input("enter 2nd string\n")
if(anagram(str1,str2)):
 print("the strings are anagrams\n")
else:
 print("the strings arent anagrams\n")
