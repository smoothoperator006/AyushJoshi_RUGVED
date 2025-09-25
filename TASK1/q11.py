def form(s):
    a=list(s)
    k=0#number of words
    b=0#number of letters
    c=0#number of sentences
    l=len(s)
    for i in range(0,l):
        if(a[i]==' '):
            k=k+1
        if(65<=ord(a[i])<=90 or 97<=ord(a[i])<=122):
            b=b+1
        if(a[i]=='.'or a[i]=='?' or a[i]=='!'):
            c=c+1
    k=k+1
    CLI=float(0.0588*((b/k)*100)-0.296*((c/k)*100)-15.8)
    print("THE CLI grade of the string is",CLI)
str=input("Enter a paragraph\n")
form(str)