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

def solve_n_queens_bfs(n):
    # inisialisasi queue dengan board kosong dan baris pertama
    queue = Queue()
    queue.put(([], 0))
    
    # iterasi dari queue
    while not queue.empty():
        board, row = queue.get()
        
        # jika semua Queen sudah ditempatkan, return board
        if row == n:
            return board
        
        # menempatkan Queen pada kolom dari baris saat ini
        for col in range(n):
            if is_valid(board, row, col):
                queue.put((board + [col], row + 1))
    
    # jika tidak ada solusi ditemukan, return none
    return None

# solusi
solution = solve_n_queens_bfs(8)

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