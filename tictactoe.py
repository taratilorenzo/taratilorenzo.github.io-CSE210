"""
Tic Tac Toe by Lorenzo Tarati
"""

"""main function"""
from operator import truediv


def main():

    #Decalring the variable player
    player = next_player("")

    #initiating the board game of Tic Tac Toe
    tictactoe_board = create_board()

    """
    while the game has no winner or one of the 9 positions
    is still empty the game loop and we still playing
    """
    while not (winner(tictactoe_board) or is_a_draw(tictactoe_board)):
        #Display our Tic Tac Toe board
        display_board(tictactoe_board) 

        #player make a move and choses a position 
        play(player, tictactoe_board)
        player = next_player(player)

    #Final display of our board
    display_board(tictactoe_board)

    #End of the game
    print("Hope you enjoy the game, Thanks for playing")

"""create_board() function will create the board as a list"""
def create_board():
    #Tic Tac Toe board declared as a list
    tictactoe_board = []

    #Using a for loop to initiate our list from 1 to 9
    for position in range(9):
        tictactoe_board.append(position + 1)
    
    #Return the completed and updated board
    return tictactoe_board

"""
display_board() will print out the board according to the
set up below
"""
def display_board(board):
    #using print to display the board
    print()
    
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("__________")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("__________")
    print(f"{board[6]} | {board[7]} | {board[8]}")

"""winner() function return true if at least one possibilities appear"""
def winner(board):
    #return all the possibility of a winning sequence
    return (#the 3 horizontal possibilities
            board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            #the 3 vertical possibilities
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            #the 2 diagonal possibilities
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

"""is_a_draw() function check if all postion have been chosen"""
def is_a_draw(board):
    #using for loop to check if all postion is used we return true if not  return false
    for position in range(9):
        if board[position] != "x" and board[position] != "o":
            return False
    return True

"""next_player() give a turn to each player"""
def next_player(player):
    if player == "" or player == "o":
        return "x"
    elif player == "x":
        return "o"

"""play() give the turn to either x or o"""
def play(player, board):
    #prompt user to chose a postion
    position = int(input(f"{player}'s turn chose a position: "))
    
    #using recursive
    if is_empty(board, position):
        board[position - 1] = player
    else: 
        print("This position is already used. Pick another one.")
        play(player, board)

"""is_empty() check if the postion is still free to place x or o"""
def is_empty(board, position):
    if board[position - 1] == "x" or board[position - 1] == "o":
        return False
    else: return True

"""call the main() function"""
if __name__ == "__main__":
    main()