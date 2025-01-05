import pygame

# Drawing Functions
def draw_square(screen, x: int, y: int, square_size: int, color: tuple):
    pygame.draw.rect(screen, color, pygame.Rect(x, y, square_size, square_size))



def draw_border(screen, x: int, y: int, square_size: int, border_color: tuple, border_thickness: int):
    pygame.draw.rect(screen, border_color, pygame.Rect(x, y, square_size, square_size), width=border_thickness)



def draw_horizontal_line(screen, length: int, origin_x: int, origin_y: int, square_size: int, border_thickness: int, square_color: tuple, border_color: tuple):
    for i in range(length):
        multiple_h = i > 0
        draw_square(screen, origin_x, origin_y, square_size, square_color)
        draw_border(screen, origin_x, origin_y, square_size, border_color, border_thickness)
        origin_x += square_size - border_thickness



def draw_box(screen, length: int, origin_x: int, origin_y: int, square_size: int, border_thickness: int, square_color: tuple, border_color: tuple):
    for _ in range(length):
        for _ in range(length):
            draw_horizontal_line(screen, length, origin_x, origin_y, square_size, border_thickness, square_color, border_color)
        origin_y += square_size - border_thickness