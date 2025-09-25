n = int(input("Enter size of matrix: \n"))
matrix = []
print("Enter matrix row by row:\n")
for i in range(n):
    row = input().split()
    row = [int(x) for x in row] 
    matrix.append(row)

print("Rotated Matrix:\n")
for j in range(n):
    for i in range(n-1,-1, -1): 
     print(matrix[i][j], end=" ")
    print()
