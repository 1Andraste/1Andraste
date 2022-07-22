def collumn_checker(board):
    for q in board:
        if q[0] == q[1] == q[2]:
            if q[0] == 1:
                return 1
            else:
                return 2
    return 3


def diag_checker(board):
    if board[0][0] == board[1][1] == board[2][2] != 0:
        if board[0][0] == 1:
            return 1
        else:
            return 2
    return 3


def is_solved(board):
    r_board = list(zip(board[0], board[1], board[2]))
    win = collumn_checker(board)
    win2 = collumn_checker(r_board)
    if win2 != 3 or win != 3:
        if win < win2:
            return win
        else:
            return win2
    else:
        d_win = diag_checker(board)
        d_win2 = diag_checker(r_board)
        print(d_win, d_win2)
        if d_win != 3 or d_win2 != 3:
            if d_win < d_win2:
                return d_win
            else:
                return d_win2
        else:
            for i in board:
                if 0 in i:
                    return -1
            return 0




