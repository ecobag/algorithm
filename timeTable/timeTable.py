# Using 2 dimensional list

table_list = [[0 for i in range(9)] for j in range (9)]

# Make timetable
for i in range(9):
    for j in range(9):
        table_list[i][j] = (i+1) * (j+1)
    


# Print list
for i in range(1,9):
    for j in range(9):
        print(table_list[i][j])
    print()