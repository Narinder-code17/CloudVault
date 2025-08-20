def printBoard(xState, oState):
    board = []
    for i in range(9):
        if xState[i]:
            board.append('X')
        elif oState[i]:
            board.append('O')
        else:
            board.append(str(i))
    
    print(f"\n {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}\n")

def checkWin(state):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for cond in win_conditions:
        if sum([state[i] for i in cond]) == 3:
            return True
    return False

def isFull(xState, oState):
    return all([x or o for x, o in zip(xState, oState)])

if __name__ == "__main__":
    xState = [0] * 9
    oState = [0] * 9
    turn = 1  # 1 for X, 0 for O

    print("🎮 Welcome to Tic Tac Toe!")
    print("Position guide (choose numbers 0 to 8):")
    printBoard([0]*9, [0]*9)

    while True:
        printBoard(xState, oState)
        if turn == 1:
            print("X's Turn")
        else:
            print("O's Turn")

        try:
            pos = int(input("Enter position (0-8): "))
            if pos < 0 or pos > 8:
                print("⚠️ Invalid position. Try again.")
                continue
            if xState[pos] or oState[pos]:
                print("⚠️ Position already taken. Try again.")
                continue
        except ValueError:
            print("⚠️ Please enter a number between 0 and 8.")
            continue

        if turn == 1:
            xState[pos] = 1
            if checkWin(xState):
                printBoard(xState, oState)
                print("🏆 X wins the game!")
                break
        else:
            oState[pos] = 1
            if checkWin(oState):
                printBoard(xState, oState)
                print("🏆 O wins the game!")
                break

        if isFull(xState, oState):
            printBoard(xState, oState)
            print("🤝 It's a draw!")
            break

        turn = 1 - turn  # switch turn
