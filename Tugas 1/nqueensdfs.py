from queue import Queue

# memeriksa apakah penempatan Queen berada di kolom atau baris yang tepat atau tidak
def is_valid(board, row, col):
    # memeriksa apakah ada queen yang terletak di kolom yg sama
    for i in range(row):
        if board[i] == col:
            return False
    
    # periksa diagonal atas sebelah kiri
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False
    
    # periksa diagonal atas sebelah kanan
    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i] == j:
            return False
    
    return True

def solve_n_queens_dfs(n):
    # fungsi rekursif untuk menempatkan Queen pada setiap baris
    def place_queen(board, row):
        # jika semua Queen sudah ditempatkan, return board
        if row == n:
            return board
        
        # menempatkan Queen pada setiap kolom pada baris saat ini
        for col in range(n):
            if is_valid(board, row, col):
                # menambahkan Queen ke board dan memanggil fungsi rekursif pada baris selanjutnya
                board.append(col)
                result = place_queen(board, row + 1)
                # jika solusi ditemukan, return board
                if result:
                    return result
                # jika tidak, hapus Queen yang telah ditambahkan dari board
                board.pop()
    
    # panggil fungsi rekursif dengan board kosong dan baris pertama
    return place_queen([], 0)


# solusi
solution = solve_n_queens_dfs(8)

if solution:
    for row in range(len(solution)):
        line = ""
        for col in range(len(solution)):
            if solution[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
else:
    print("Solusi tidak dapat ditemukan.")