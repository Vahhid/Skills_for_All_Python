#This program will request the user to provide a number and display as a seven segment
#decimals = list(range(10))
#print(decimals)
#Function for displaying individual decimals
def draw(decimal):
    def horizontal(side):
        if side =="solid":
            print(8*"#")
        elif side == "both":
            print("#"," "*4 , "#")
        elif side == "right":
            print(" "," "*4 , "#")
    def vertical(side):
        if side == "both":
            for i in range(3):
                print("#",4*" ","#")
        elif side == "right":
            for i in range(3):
                print(" ",4*" ","#")
        elif side == "left":
            for i in range(3):
                print("#",4*" "," ")
        else:
             for i in range(3):
                print(" ",4*" "," ")           
    if decimal == 1:
        horizontal("right")
        vertical("right")
        horizontal("right")
        vertical("right")
        horizontal("right")
        print(" ")
    elif decimal == 0:
        horizontal("solid")
        vertical("both")
        horizontal("both")
        vertical("both")
        horizontal("solid")
        print(" ")

    elif decimal == 8:
        horizontal("solid")
        vertical("both")
        horizontal("solid")
        vertical("both")
        horizontal("solid")
        print(" ")
        
    elif decimal == 2:
        horizontal("solid")
        vertical("right")
        horizontal("solid")
        vertical("left")
        horizontal("solid")
        print(" ")

    elif decimal == 3:
        horizontal("solid")
        vertical("right")
        horizontal("solid")
        vertical("right")
        horizontal("solid")
        print(" ")

    elif decimal == 4:
        horizontal("both")
        vertical("both")
        horizontal("solid")
        vertical("right")
        horizontal("right")
        print(" ")

    elif decimal == 5:
        horizontal("solid")
        vertical("left")
        horizontal("solid")
        vertical("right")
        horizontal("solid")
        print(" ")

    elif decimal == 6:
        horizontal("solid")
        vertical("right")
        horizontal("solid")
        vertical("both")
        horizontal("solid")
        print(" ")

    elif decimal == 7:
        horizontal("solid")
        vertical("right")
        horizontal("right")
        vertical("right")
        horizontal("right")
        print(" ")




