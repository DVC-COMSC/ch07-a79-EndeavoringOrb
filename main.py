
numbers = [     [99, 11, 66, 86, 55],
               [44, 21, 65, 88, 24],
               [33, 77, 32, 33, 34]]


rnum = len(numbers)
greatest_sum = -1
greatest_row = -1

#print row sum
for i in range(rnum):
    #print("Sum of rows: ", end = "")
    print(sum(numbers[i]), end = " ")
    if sum(numbers[i]) > greatest_sum:
        greatest_sum = sum(numbers[i])
        greatest_row = i
print("\n")


#print column sum
for i in range(rnum):
    #print("Sum of columns: ", end = "")
    print(numbers[i][0] + numbers[i][1] + numbers[i][2], end = " ")

print("\n")

#print row with greatest sum
#print(f"The row that has the greatest sum: {greatest_row}")
print(greatest_row, end = " ")
print("\n")
greatest_num = -1

#print greatest value in array
for i in range(rnum):
    cnum = len(numbers[i])
    for j in range(cnum):
        if numbers[i][j] > greatest_num:
            greatest_num = numbers[i][j]
print(greatest_num)