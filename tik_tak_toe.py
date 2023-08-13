def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    def vertical():
        print("|", " " *20,"|", " " *20,"|", " " *20,"|")
    def horizontal():
        print("+","-" * 20,"+","-" * 20,"+","-" * 20,"+")
    def vertical_with_piece(x,y,z):
        print("|", " " *7,x, " " *10,"|"," " *7,y, " " *10,"|"," " *7,z, " " *10,"|")

    for i in range(3):
        horizontal()
        for z in range(11):
            if z == 6:
                vertical_with_piece(board[i][0],board[i][1]\
                                    ,board[i][2])
            vertical()
        
    horizontal() 
    print("\n" *2)


"""
def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    # The function draws the computer's move and updates the board.
"""

#This is the status of the board before any move to be passed for clearing the board 
start_board = [[1,2,3],[4,5,6],[7,8,9]]

#This will be used to record legal moves for record and display. 
#The first element is empty board
moves = [start_board]

#Display an empy board
print("\n The empty board is ...\n")
display_board(start_board)
print("First move belongs to the computer. \n")
#Start by taking the middle position in the first move of the computer
next_move = moves[0]
next_move[1][1] = "X"
moves.append(next_move)
display_board(moves[-1])