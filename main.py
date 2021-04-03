from time import sleep
import os


board = [' ' for x in range(10)]

def insert_letter(letter, pos):
    global board
    board[pos] = letter

def space_is_free(pos):
    return board[pos] == ' '

def print_board(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def is_winner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def player_move():
    run = True
    while run:
        move = input('Please select a position to place an "x" (1-9): ')

        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('x', move)
                else:
                    print('Sorry, this space is occupied')
            else:
                print('Please type a number within the range!')

        except:
            print('Please type a number!')


def comp_move():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['o', 'x']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if is_winner(boardCopy, let):
                move = i
                return move

    open_corners = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            open_corners.append(i)
    if len(open_corners) > 0:
        move = select_random(open_corners)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    open_edges = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            open_edges.append(i)
    if len(open_edges) > 0:
        move = select_random(open_edges)
        return move


def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]



def main():
    print('Welcome to Tic Tac Toe!')
    print_board(board)

    while not(is_board_full(board)):
        if not(is_winner(board, 'o')):
            player_move()
            os.system('cls')
            print_board(board)
        else:
            print("You Lost!")
            break

        
        if not(is_winner(board, 'x')):
            move = comp_move()

            if move == 0 or move == None:
                print('Tie Game!')
                break
                sleep(3)
            else:
                insert_letter('o', move)
                
                os.system('cls')
                print(f'Computer placed an "o" in position {move}: ')
                print_board(board)
        else:
            print("You Won!")
            break

        
play = True
while play:
    main()
    board = [' ' for x in range(10)]
    play_again = input("Do you want to play again?(y/n) ")
    play_again = play_again.upper()
    if play_again == "Y":
        play = True
    elif play_again == "N":
        print("Bye, I enjoyed playing with you!")
        play = False
    else:
        print("Please enter Y or N only")
    sleep(3)