
numbers = [     [99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24],
               [33, 77, 32, 33, 34]]


rnum = len(numbers)
cnum = len(numbers[0])
greatest_sum = -1
greatest_row = -1

#print row sum
#print("Sum of rows: ", end = "")
for i in range(rnum):
    if i != 2:
        print(sum(numbers[i]), end = " ")
    if i == 2:
        print(sum(numbers[i]), end = "\n")
    if sum(numbers[i]) > greatest_sum:
        greatest_sum = sum(numbers[i])
        greatest_row = i

#print column sum
#print("Sum of columns: ", end = "")
for i in range(cnum):
    col_tot = 0
    for j in range(rnum):
        col_tot += numbers[j][i]
    print(col_tot,end = " ")

#print row with greatest sum
#print(f"The row that has the greatest sum: {greatest_row}", end = "\n")
print(f"\n{greatest_row}")
greatest_num = -1

#print greatest value in array
for i in range(rnum):
    cnum = len(numbers[i])
    for j in range(cnum):
        if numbers[i][j] > greatest_num:
            greatest_num = numbers[i][j]
print(f"{greatest_num}")