import pickle
from board import BitBoard

values = [16, 8, 0, 2, 1]
moves = {}

while values[0] < 64:
    board_value = 0

    horizontal = set()
    vertical = set()

    vertical.add(values[0] % 8)
    vertical.add(values[1] % 8)
    vertical.add(values[2] % 8)

    horizontal.add(values[2] // 8)
    horizontal.add(values[3] // 8)
    horizontal.add(values[4] // 8)

    if len(horizontal) > 1 or len(vertical) > 1:
        for i in range(len(values)):
            values[i] = values[i] + 1
        continue

    for val in values: 
        board_value += 2 ** val

    board = BitBoard(board_value)
    print(board)
    moves[values[0]] = board

    for i in range(len(values)):
        values[i] = values[i] + 1

with open(f"piece_locations/long_L_bottom_right.pkl", "wb") as p_file:
    pickle.dump(moves, p_file)

# drops = [63, 62, 55, 54, 47, 46, 39, 38, 31, 30, 23, 22, ]

# for drp in drops:
#     del moves[drp]

# with open(f"piece_locations/long_L_top_right.pkl", "wb") as p_file:
#     pickle.dump(moves, p_file)

# with open(f"piece_locations/long_L_top_right.pkl", "rb") as p_file:
#     moves = pickle.load(p_file)

# for key in moves:
#     print(f"key: {key}")
#     print(moves[key])

