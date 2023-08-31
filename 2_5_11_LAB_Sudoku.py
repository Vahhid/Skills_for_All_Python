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
gong2 = str_to_soduk(inTwo)
valid_out = list(range(1,10))
#print(valid_out)
#print("Valid")
def check_rows(sodu):
    for i in range(9):
        #print(sorted(sodu[i]))
        if sorted(sodu[i]) != valid_out:
            return False
    return True

def check_columns(sodu):
    for i in range(9):
        chk = []
        for j in range(9):
            chk.append(sodu[j][i])
        #print(sorted(chk))
        if sorted(chk) != valid_out:
            return False    
    return True

def check_sqrs(sodu):
    start_1 = 0
    start_2 = 0
    count = 0
    re = []
    for z in range(3):
        for k in range(3):    
                
            row = []    
            for j in range(start_2, start_2+3):    
                for i in range(start_1, start_1+3):
                    row.append(sodu[j][i])
            re.append(row)
            start_2 +=3
        start_2 = 0
        start_1 +=3
    for x in range(len(re)):
        if sorted(re[x]) != valid_out:
            return False

               
    return True

def all_check(sodu):
    return  check_rows(sodu) and check_columns(sodu) and check_sqrs(sodu)
print("Gong")
print(all_check(gong1))
print(all_check(gong2))






    