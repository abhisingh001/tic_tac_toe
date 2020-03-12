# ''' @author Abhishek Singh
#  last update  10:25 PM 11/03/20 '''
from math import inf as infinity
from typing import Dict, Any, Union

players = ['X', 'O']


def play_move(board, player, block_num):

    if board[int((block_num - 1) / 3)][(block_num - 1) % 3] is ' ':
        board[int((block_num - 1) / 3)][(block_num - 1) % 3] = player
    else:
        block_num = int(input("Wrong move try again: "))
        play_move(board, player, block_num)


def print_board(board):
    print("-" * 15)
    for row in board:
        print("| ", end="")
        for x, cell in enumerate(row):
            print(cell, end="")
            if x != 2:
                print(" || ", end="")

        print("|")
    print("-" * 15)


def check_current_state(board):
    '''
    draw_flag = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] is ' ':
                draw_flag = 1
    if draw_flag is 0:
        return None, "Draw"
    '''
    # Check horizontals
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] is not ' ':
        return board[0][0], "Win"
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] is not ' ':
        return board[1][0], "Win"
    if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] is not ' ':
        return board[2][0], "Win"

    # Check verticals
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] is not ' ':
        return board[0][0], "Win"
    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] is not ' ':
        return board[0][1], "Win"
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] is not ' ':
        return board[0][2], "Win"

    # Check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] is not ' ':
        return board[1][1], "Win"
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] is not ' ':
        return board[1][1], "Win"
    draw_flag = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] is ' ':
                draw_flag = 1
    if draw_flag is 0:
        return None, "Draw"
    else:
        return None, "Running"


def copy_game(state):
    new_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    for i in range(3):
        for j in range(3):
            new_state[i][j] = state[i][j]
    return new_state


def getBestMove(board, player):
    winner_loser, current_state = check_current_state(board)
    if current_state == "Win" and winner_loser == 'O':  #ai
        return 1
    elif current_state == "Win" and winner_loser == 'X':
        return -1
    elif current_state == "Draw":
        return 0
    moves = []
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] is ' ':
                empty_cells.append(i * 3 + (j + 1))



    for empty_cell in empty_cells:
        move = {}
        move['index'] = empty_cell
        new_state = copy_game(board)
        play_move(new_state, player, empty_cell)
        if player == 'O':  # If AI
            result = getBestMove(new_state, 'X')  # make more depth tree for human
            move['score'] = result
        else:
            result = getBestMove(new_state, 'O')  # make more depth tree for AI
            move['score'] = result

        moves.append(move)

    best_move = None
    if player == 'O':
        best = -infinity
        for movee in moves:
            if movee['score'] > best:
                best = movee['score']
                best_move = movee['index']
    else:
        best = infinity
        for movee in moves:
            if movee['score'] < best:
                best = movee['score']
                best_move = movee['index']
    return best_move


def main(name):
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print("New Game\n")
    print_board(board)
    player_choice = input("Choose X if you wanna play first or O for AI first: ")
    winner = None
    current_state = "Running"

    if player_choice == "X" or player_choice == "x":
        player_id = 0
    else:
        player_id = 1

    while current_state == "Running":
        if player_id == 0:
            print("{} take your turn: ".format(name),end="")
            move_choice = int(input())
            play_move(board, players[player_id], move_choice)
        else:
            move_choice = getBestMove(board, players[player_id])
            play_move(board, players[player_id], move_choice)
            print("Computer plays move: " + str(move_choice))
        print_board(board)
        winner, current_state = check_current_state(board)
        if winner is not None:
            if winner is 'X':
                print(name + " Won! ")
            else:
                print("Computer Won!")
        else:
            player_id = (player_id + 1) % 2

        if current_state is "Draw":
            print("Draw")


if __name__ == '__main__':
    wanna_play = "Y"
    name = input("Enter your name : ")
    while wanna_play == "Y" or wanna_play == "y":
        print("*" * 15)
        print("TIC TAC TOE".center(15, " "))
        print("*" * 15)
        main(name)
        wanna_play = input("You wanna try again ?(Y/N): ")


    print_board("Have a nice day ******")