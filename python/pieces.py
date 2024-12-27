import pickle
# from board import BitBoard

# values = [17, 16, 9, 8, 1, 0]
# moves = {}

# while values[0] < 64:
#     adding_set = {}
#     board_value = 0

#     skip = False
#     for val in values:
#         accept_value = val % 8
#         adding_set[accept_value] = adding_set.get(accept_value, 0) + 1
            
#         board_value += 2 ** val

#     sets = set()
#     for val in adding_set.values():
#         sets.add(val)
    
#     if len(sets) > 1:
#         skip = True

#     if skip:
#         for i in range(len(values)):
#             values[i] = values[i] + 1
#         continue

#     board = BitBoard(board_value)
#     print(board)
#     moves[values[0]] = board

#     for i in range(len(values)):
#         values[i] = values[i] + 1

# with open(f"piece_locations/3x2.pkl", "wb") as p_file:
#     pickle.dump(moves, p_file)

with open(f"piece_locations/3x2.pkl", "rb") as p_file:
    moves = pickle.load(p_file)


for key in moves:
    print(f"key: {key}")
    print(moves[key])




# drops = [56, 48, 40, 32, 24]

# for drp in drops:
#     del moves[drp]

# with open(f"piece_locations/3x2.pkl", "wb") as p_file:
#     pickle.dump(moves, p_file)

