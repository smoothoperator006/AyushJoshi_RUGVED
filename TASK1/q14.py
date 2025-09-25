def arr_rep():
    n = int(input("Enter size of array: \n"))
    arr = []
    k=0
    for i in range(n):
        num = int(input("Enter element: \n"))
        arr.append(num)
    rep=-1  
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] == arr[j]):
                rep = arr[i]
                break
        if rep != -1:
            break

    if (rep != -1):
        print("First repeating element is:", rep)
    else:
        print("Repeating element not found in array")
        
arr_rep()