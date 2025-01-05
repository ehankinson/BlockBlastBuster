import random
import pickle

pieces = [
    "2_diagonal_left",
    "2_diagonal_right",
    "2x2",
    "2x3",
    "3_diagonal_left",
    "3_diagonal_right",
    "3x2",
    "3x3",
    "horizontal_2",
    "horizontal_3",
    "horizontal_4",
    "horizontal_5",
    "lazy_L_bottom_left",
    "lazy_L_bottom_right",
    "lazy_L_top_left",
    "lazy_L_top_right",
    "long_L_bottom_left"
    "long_L_bottom_right"
    "long_L_top_left",
    "long_L_top_right",
    "short_L_bottom_left",
    "short_L_bottom_right",
    "short_L_top_left",
    "short_L_top_right",
    "single",
    "t_down",
    "t_up",
    "t_left",
    "t_right",
    "vertical_2",
    "vertical_3",
    "vertical_4",
    "vertical_5",
    "z_down",
    "z_left",
    "z_right",
    "z_up"
]




def get_random_pieces(pieces: list[str]):
    return random.choice(pieces)



def draw_square():

if __name__ == '__main__':
    a = 5
