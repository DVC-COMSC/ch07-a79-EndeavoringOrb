
numbers = [     [99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24],
               [33, 77, 32, 33, 34]]


rnum = len(numbers)
greatest_sum = -1
greatest_row = -1

#print row sum
print("Sum of rows: ", end = "")
for i in range(rnum):
    if i != 2:
        print(sum(numbers[i]), end = " ")
    if i == 2:
        print(sum(numbers[i]), end = "\n")
    if sum(numbers[i]) > greatest_sum:
        greatest_sum = sum(numbers[i])
        greatest_row = i

#print column sum
print("Sum of columns: ", end = "")
for i in range(rnum):
    if i != 2:
        print(numbers[i][0] + numbers[i][1] + numbers[i][2], end = " ")
    if i == 2:
        print(numbers[i][0] + numbers[i][1] + numbers[i][2], end = "\n")

#print row with greatest sum
print(f"The row that has the greatest sum: {greatest_row}", end = "\n")
greatest_num = -1

#print greatest value in array
for i in range(rnum):
    cnum = len(numbers[i])
    for j in range(cnum):
        if numbers[i][j] > greatest_num:
            greatest_num = numbers[i][j]
print(f"The greatest number: {greatest_num}")