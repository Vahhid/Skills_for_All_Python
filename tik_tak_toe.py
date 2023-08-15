def display_board(board):
    return None




def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    wrong_user_input = True
    while wrong_user_input:
        try:
            message = "Enter your move unoccupied location are: \n" \
                +str(make_list_of_free_fields(board))
            user_move = int(input(message))
            if user_move in make_list_of_free_fields(board):
                #find the indexs of the valid selection 
                # and update the piece matrix with "O"
                if user_move < 4:
                    i = 0
                    j = user_move - 1
                elif user_move < 7:
                    i = 1
                    j = user_move - 4
                else:
                    i = 2
                    j = user_move - 7
            #check of the index locations
            #print("The index selected is ", i, " , ", j)
            
            board[i][j] = "O"
            moves.append(board)
            wrong_user_input = False
        except:
            print("Please enter a valid move from the list "\
                  ,str(make_list_of_free_fields(board)) )

    draw_move(moves[-1])




def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    legal_moves = ()
    for i in range(3):
        for j in range(3):
            if type(board[i][j]) is int:
                legal_moves += board[i][j],
    return legal_moves
 


def victory_for(board, sign = "X"):
    lst = board[-1] 
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    game_over = False
    for i in range(3):
        for j in range(3):
            if lst[i][j] == sign:
                if ( i == j):
                    if ((lst[i][0] == lst[i][1] and lst[i][1] == lst[i][2]) \
                    or (lst[0][j] == lst[1][j] and lst[1][j] == lst[2][j])) \
                    or ((lst[0][0] == lst[1][1] and lst[1][1] == lst[2][2]) \
                    or  (lst[2][0] == lst[1][1] and lst[1][1] == lst[0][2])):    
                        game_over = True                    
                else:
                    if (lst[i][0] == lst[i][1] and lst[i][1] == lst[i][2]) \
                    or (lst[0][j] == lst[1][j] and lst[1][j] == lst[2][j]):
                        game_over = True
                        
    
    return game_over, sign


def draw_move(board):
    # The function draws the computer's move and updates the board.
        # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    def vertical():
        print("|", " " *6,"|", " " *6,"|", " " *6,"|")
    def horizontal():
        print("+","-" * 6,"+","-" * 6,"+","-" * 6,"+")
    def vertical_with_piece(x,y,z):
        print("|", " " *2,x, " " *1,"|"," " *2,y, " " *1,"|"," " *2,z, " " *1,"|")

    for i in range(3):
        horizontal()
        for z in range(3):
            if z == 2:
                vertical_with_piece(board[i][0],board[i][1],board[i][2])
            vertical()
        
    horizontal() 
    print("\n" *2)

#This is the status of the board before any move to be passed for clearing the board 
start_board = [[1,2,3],[4,5,6],[7,8,9]]

#This will be used to record legal moves for record and display. 
#The first element is empty board
moves = [start_board]

#Display an empy board
print("\n The empty board is ...\n")
draw_move(start_board)
print("First move belongs to the computer. \n")
#Start by taking the middle position in the first move of the computer
next_move = moves[0]
next_move[1][1] = "X"
moves.append(next_move)
draw_move(moves[-1])
#print("Your turn. You can choose between the following "\
# ,make_list_of_free_fields(moves[-1]))
enter_move(moves[-1])




