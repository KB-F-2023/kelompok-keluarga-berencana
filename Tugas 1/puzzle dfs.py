from queue import Queue

def dfs(initial_state, goal_state):
    stack = [initial_state]
    visited = set()
    path = {tuple(initial_state): None}

    while stack:
        current_state = stack.pop()

        if current_state == goal_state:
            solution_path = []
            while current_state is not None:
                solution_path.append(current_state)
                current_state = path.get(tuple(current_state))
            solution_path.reverse()
            return solution_path

        visited.add(tuple(current_state))

        for move in legal_moves(current_state):
            new_state = make_move(current_state, move)
            if tuple(new_state) not in visited:
                stack.append(new_state)
                path[tuple(new_state)] = current_state

    return None


def legal_moves(state):
    moves = []
    index = state.index(0)
    if index not in [0, 1, 2]:
        moves.append(-3)  # up
    if index not in [6, 7, 8]:
        moves.append(3)   # down
    if index not in [0, 3, 6]:
        moves.append(-1)  # left
    if index not in [2, 5, 8]:
        moves.append(1)   # right
    return moves

def make_move(state, move):
    new_state = state[:]
    index = new_state.index(0)
    new_index = index + move
    new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
    return new_state

# Penggunaan kode dengan input dari pengguna
initial_state = [int(i) for i in input("Masukkan initial state: ").split()]
goal_state = [int(i) for i in input("Masukkan goal state: ").split()]
solution_path = dfs(initial_state, goal_state)
if solution_path is not None:
    for state in solution_path:
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("Tidak ada solusi yang ditemukan.")
