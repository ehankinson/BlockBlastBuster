import pickle
from board import BitBoard

# t = 18
# v = 17
# c = 16
# n = 10
# l = 9
# m = 8
# a = 2
# r = 1
# b = 0
# values = [18, 17, 16, 10, 9, 8, 2, 1, 0]

# possible_moves = {}


# while values[0] < 64:
#     a = 0
#     for val in values:
#         a += 2 ** val

#     board = BitBoard(a)
#     print(board)
#     possible_moves[values[0]] = board
    
#     for i in range(len(values)):
#         values[i] = values[i] + 1
        

# with open("piece_locations/3x3.pkl", "wb") as p_file:
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
