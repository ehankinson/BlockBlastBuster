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

with open("piece_locations/3x3.pkl", "rb") as p_file:
    moves = pickle.load(p_file)


for move in moves:
    print(moves)






