"""
As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. 
The player has to fill the board in a very specific way:

-each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
-each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
-each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
-If you need more details, you can find them here.

Your task is to write a program which:

reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.
Test your code using the data we've provided.

"""
soduk = []

valid_out = list(range(1,9))
count = 0
while count < 9:
    line = []
    outString = "Enter your soduk row ", count+1," \n"
    row = input(outString)
    for i in range(9):
        try:
            line.append(int(row[i]))
        except:
            print("Please enter valid row")
            break
    count +=1
    soduk.append(line)

print(soduk)
print(valid_out)
