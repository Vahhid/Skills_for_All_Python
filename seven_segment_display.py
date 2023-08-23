#This program will request the user to provide a number and display as a seven segment
decimals = list(range(10))
print(decimals)
#Function for displaying individual decimals
def draw(decimal):
    #pattern for eight
    """
    ########
    #      #
    #      #
    #      #
    ########
    #      #
    #      #
    #      #
    ########
    """
    def horizontal():
        print(8*"#")
    def vertical():
        for i in range(3):
            print("#",4*" ","#")
    horizontal()
    vertical()
    horizontal()
    vertical()
    horizontal()
draw(8)

