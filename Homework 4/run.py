# TODO:
# Write code to compute the answers to the questions below and print the answers.
# Feel free to modify this file and the other files as much as you like and need.
# Document your code if you'd like to receive any partial credit.
# Pay special attention to the formatting requirements.

# You probably want to start with importing classes and functions from the games file: from games import ...
import games

def findTurn(brd):
    numX = 0
    numO = 0
    for row in brd:
        for val in row:
            if val == 'X':
                numX += 1
            elif val == 'O':
                numO += 1
            else:
                pass
    if numX == numO:
        turn = 'X'
    else:
        turn = 'O'
    return turn

def buildBoard(brd):
    board = {}
    mv = []
    x = 1
    y = 1
    for row in brd:
        for val in row:
            if val != '-':
                board[(x, y)] = val
                y += 1
            else:
                mv.append((x, y))
                y += 1
        x += 1
        y = 1
    return board, mv

def checkForTerminal(brd, mv):
    """This Functions checks to see if the state inputed already has a winning result.
    If X won returns 1, -1 if O won, else returns 0. Returns 1 if the input is a draw."""
    player = ['X', 'O']
    sols = [[(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 1)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)]]

    for p in player:
        for sol in sols:
            count = 0
            for x, y in sol:
                if brd[x][y] == p:
                    count += 1
            if count == 3 and p == 'X':
                return 1
            elif count == 3 and p == 'O':
                return -1
    if len(mv) == 0:
        return 1
    else:
        return 0 # the board is not in a terminal state.

def buildGame(brd):
    ttt = games.TicTacToe()
    gBoard, mv = buildBoard(brd)
    turn = findTurn(brd)
    util = checkForTerminal(brd, mv)
    my_state = games.GameState(
        to_move = turn,
        utility = util,
        board = gBoard,
        moves = mv
    )
    return ttt, my_state

def main():
    rows = []
    brd = []
    count_ab = 0
    print("Enter the first row.")
    # TODO - Implement. Write code to get the first line from the user.
    # An example input line: X - O
    # In this example, the first entry is X, the second entry is -, indicating blank, and the third entry is O
    rows.append(input())
    print("Enter the second row.")
    # TODO - Implement
    rows.append(input())

    print("Enter the third row.")
    # TODO - Implement
    rows.append(input())

    #compiling the rows.
    for x in range(3):
         brd.append(rows[x].split())
    # For the following questions, you can implement everything here or under the questions or you can do a mix.
    # It's totally up to you where to put your implemention in this file.
    # However, please pay special attention to the instructions regarding the format of the answers.

    print("Whose turn is it now?")
    # TODO - Implement. Compute and print the answer.
    # The answer should a single letter: either X or O. No punctuation. No other text.
    ttt, my_state = buildGame(brd)
    #print((my_state.utility))
    print(my_state.to_move)

    print("What is the value of the current state from the perspective of X?")
    # TODO - Implement. Compute and print the answer.
    # The answer should a single number: either -1 or 1 or 0. No punctuation. No other text.
    # Important: this is always from the perspective of X; *not* from the perspective of whose turn it is.
    if my_state.utility != 0:
        print(str(my_state.utility))
    else:
        decision, count_ab = games.alphabeta_search(my_state, ttt)
        comp = ttt.compute_utility(my_state.board, decision, my_state.to_move)
        print(str(comp))

    print("How many states did the minimax algorithm evaluate?")
    # TODO - Implement. Compute and print the answer.
    # The answer should a single number. No punctuation. No other text.
    # You probably need to modify games.py to compute this.
    decision, count = games.minimax_decision(my_state, ttt)
    print(str(count))

    print("How many states did the alpha-beta pruning algorithm evaluate?")
    # TODO - Implement. Compute and print the answer.
    # The answer should a single number. No punctuation. No other text.
    # You probably need to modify games.py to compute this.

    print(str(count_ab))

    print("Assuming both X and O play optimally, does X have a guaranteed win? Is it a tie? Is it a guaranteed loss for X?")
    # TODO - Implement. Compute and print the answer.
    # The answer should be either of "X will win.", or "It is a tie." or "X will lose."
    # Note: you already computed this somewhere above.
    if comp == 1:
        print("X will win.")
    elif comp == -1:
        print("X will lose.")
    else:
        print("It is a tie.")

    print("Assuming both X and O would play optimally, how would they play till the game ends?")
    # TODO - Implement. Compute.
    # Display the states one at a time, using the display method of the Game class (or its subclasses, whichever is appropriate).
    # Print a single blank line between the states. That is, use print(). Do not print any additional info.
    ttt.display(my_state)
    print()
    if my_state.utility == 0:
        ttt.play_game(my_state, games.alphabeta_player, games.alphabeta_player)

main()
