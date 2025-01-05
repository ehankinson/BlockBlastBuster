# Example file showing a circle moving on screen
import pygame
from square import draw_box

pygame.init()
screen = pygame.display.set_mode((720, 780))



############################################################ 
#                       CONSTANTS                          #
############################################################
WIDTH = screen.get_width()
HEIGHT = screen.get_height()

SQUARE_SIZE = 45
BORDER_THICKNESS = 2

START_X = (WIDTH / 2) - ((SQUARE_SIZE * 8) / 2)
START_Y = HEIGHT / 6.24

P_Y = (525 + HEIGHT) / 2

P1_X = WIDTH / 6
P2_X = WIDTH / 2
P3_X = WIDTH * (5 / 6)


OXFORD_BLUE = (108, 105, 119)
LAPIS = (51, 101, 138)
DIM_GRAY = (108, 105, 119)
LIGHT_PURPLE = (109, 55, 100)
VIOLET = (81, 41, 71)        
    


clock = pygame.time.Clock()
running = True
dt = 0

############################################################ 
#                       Game Loop                          #
############################################################

while running:
    screen.fill(DIM_GRAY)
    
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # building the game grid
    draw_box(screen, 8, START_X, START_Y, SQUARE_SIZE, BORDER_THICKNESS, LIGHT_PURPLE, VIOLET)

    pygame.draw.line(screen, LIGHT_PURPLE, (0,525), (800,525), width=2)

    for i in range(1, 3):  # Only draw at 1/3 and 2/3
        x_position = i * (WIDTH // 3)
        pygame.draw.line(screen, (0, 0, 0), (x_position, 0), (x_position, HEIGHT), width=BORDER_THICKNESS)


    pygame.draw.circle(screen, 'red', (P1_X, P_Y), 5)
    pygame.draw.circle(screen, 'red', (P2_X, P_Y), 5)
    pygame.draw.circle(screen, 'red', (P3_X, P_Y), 5)

    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()