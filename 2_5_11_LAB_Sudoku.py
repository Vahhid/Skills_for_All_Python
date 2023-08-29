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

yes:
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672

no: 
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671

"""
"""
soduk = []

valid_out = list(range(1,9))
count = 0
while count < 9:
    line = []
    outString = "Enter your soduk row "+ str(count+1) + " \n"
    row = input(outString)
    for i in range(9):
        try:
            line.append(int(row[i]))
        except:
            print("Please enter valid row")
            break
    count +=1
    soduk.append(line)
"""    
inOne = """295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672"""
inTwo = """195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
"""
def str_to_soduk(test1Str1):
    test1 = []
    for i in range(len(test1Str1)):
        if (i+1) % 10 != 0:
            #st = test1Str1[i],i
            test1.append(int(test1Str1[i]))
    count = 0
    sodukk1 = [] 
    while count < len(test1):
        row = []
        for i in range(9):
            row.append(test1[count+i])
        sodukk1.append(row)
        count+=9
    return sodukk1

gong1 = str_to_soduk(inOne)
print("________________________________________")
gong2 = str_to_soduk(inTwo)



    