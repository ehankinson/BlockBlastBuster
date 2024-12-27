import pickle
from board import BitBoard

# l = 10
# m = 9
# r = 8
# b = 1

# possible_moves = {}

# while l < 64:
#     a = 2 ** l + 2 ** m + 2 ** r + 2 ** b
#     board = BitBoard(a)
#     print(board)
#     possible_moves[l] = board
#     l += 1
#     m += 1
#     r += 1
#     b += 1

# with open("piece_locations/t_down.pkl", "wb") as p_file:
#     pickle.dump(possible_moves, p_file)

# with open("piece_locations/t_down.pkl", "rb") as p_file:
#     moves = pickle.load(p_file)


# print(moves[58])

# l = 9
# m = 2
# r = 1
# b = 0

# possible_moves = {}

# # while l < 64:
# #     a = 2 ** l + 2 ** m + 2 ** r + 2 ** b
# #     board = BitBoard(a)
# #     print(board)
# #     possible_moves[l] = board
# #     l += 1
# #     m += 1
# #     r += 1
# #     b += 1


l = 17
m = 9
r = 8
b = 1

possible_moves = {}

while l < 64:
    a = 2 ** l + 2 ** m + 2 ** r + 2 ** b
    board = BitBoard(a)
    print(board)
    possible_moves[l] = board
    l += 1
    m += 1
    r += 1
    b += 1


with open("piece_locations/t_right.pkl", "rb") as p_file:
    moves = pickle.load(p_file)

print(moves[25])