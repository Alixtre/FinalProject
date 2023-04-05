from random import randrange


def display_board(board):
    print(f'''
    +-------+-------+-------+
    |       |       |       |
    |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
    |       |       |       |
    +-------+-------+-------+
    ''')


def enter_move(board):
    while True:
        try:
            inp = int(input("Введіть номер клітинки, в яку ви хочете поставити O:"))
            i = 0
            for subls in board:
                j = 0
                for square in subls:
                    if square == inp:
                        board[i][j] = "O"
                        return
                    j += 1
                i += 1
            continue
        except:
            continue


def make_list_of_free_fields(board):
    ls = []
    i = 0
    for subls in board:
        j = 0
        for square in subls:
            if (square != "O") & (square != "X"):
                ls.append((i, j))
            j += 1
        i += 1
    return ls


def victory_for(board, sign):
    if ((board[0][0] == sign) & (board[0][1] == sign) & (board[0][2] == sign)) | \
            ((board[1][0] == sign) & (board[1][1] == sign) & (board[1][2] == sign)) | \
            ((board[2][0] == sign) & (board[2][1] == sign) & (board[2][2] == sign)) | \
            ((board[0][0] == sign) & (board[1][0] == sign) & (board[2][0] == sign)) | \
            ((board[0][1] == sign) & (board[1][1] == sign) & (board[2][1] == sign)) | \
            ((board[0][2] == sign) & (board[1][2] == sign) & (board[2][2] == sign)) | \
            ((board[0][0] == sign) & (board[1][1] == sign) & (board[2][2] == sign)) | \
            ((board[0][2] == sign) & (board[1][1] == sign) & (board[2][0] == sign)):
        print(f"{sign} виграли!")
        return True
    else:
        return False


def draw_move(board):
    ls = make_list_of_free_fields(board)
    chosen = randrange(len(ls))
    board[ls[chosen][0]][ls[chosen][1]] = "X"


board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

while True:
    display_board(board)
    if victory_for(board, "X") | victory_for(board, "O"):
        break
    if len(make_list_of_free_fields(board)) == 0:
        print("Нічия!")
        break
    enter_move(board)
    display_board(board)
    if victory_for(board, "X") | victory_for(board, "O"):
        break
    if len(make_list_of_free_fields(board)) == 0:
        print("Нічия!")
        break
    draw_move(board)