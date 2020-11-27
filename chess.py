def print_chess_board(k, l, m, n):
    board = [[0 for i in range(0, 8)] for j in range(0, 8)]

    for i in range(0, 8):
        if i % 2 == 0:
            for j in range(0, 8):
                if j % 2 == 0:
                    board[i][j] = "\033[0;37;47m  "
                else:
                    board[i][j] = "\033[0;37;48m  "
        else:
            for j in range(0, 8):
                if j % 2 == 0:
                    board[i][j] = "\033[0;37;48m  "
                else:
                    board[i][j] = "\033[0;37;47m  "
    
    k, l, m, n = map(lambda x: x - 1, (k, l, m, n))

    if (k + l) % 2 != 0:
        board[7-l][k] = "\033[1;31;47m 1"
    else:
        board[7-l][k] = "\033[1;31;40m 1"

    if (m + n) % 2 != 0:
        board[7-n][m] = "\033[1;31;47m 2"
    else:
        board[7-n][m] = "\033[1;31;40m 2"

    for i in range(0, 8):
        for j in range(0, 8):
            print(board[i][j], end='')
        print('\033[0;37;40m')
    

def compare_colors(k, l, m, n):
    if (k+l) % 2 == (m+n) % 2:
        print('a) Squares (k, l) and (m, n) have the same colour')
    else:
        print('a) Squares (k, l) and (m, n) have different colours')


def check_queen(k, l, m, n):
    print('b) Queen is located on the square (k, l). Does it threaten square (m, n)?')
    if (k == m) or (l == n) or abs(k - m) == abs(l - n):
        print("  Yes, it does")
    else:
        print("  No, it doesn't")


def check_knight():
    pass


def check_rook_move():
    pass


def check_queen_move():
    pass


def check_bishop_move():
    pass


def main():
    numbers = [str(i) for i in range(1, 9)]
    print("Hello. You need to enter indexes (k, l) and (m, n) for 2 chess squares. Be careful: numbers must be between 1 to 8 inclusively.")
    k = input("Enter value k: ")
    l = input("Enter value l: ")
    m = input("Enter value m: ")
    n = input("Enter value n: ")

    if k in numbers and l in numbers and m in numbers and n in numbers:
        if k == m and l == n:
            print("This is the same square! Try again \n")
            main()
        else:
            k, l, m, n = map(int, (k, l, m, n))
            print_chess_board(k, l, m, n)
            print('\033[0;37;40m')
            compare_colors(k, l, m, n)
            check_queen(k, l, m, n)

    else:
        print("Some of the values are incorrect! Let's try again \n")
        main()
    


if __name__ == '__main__':
    main()