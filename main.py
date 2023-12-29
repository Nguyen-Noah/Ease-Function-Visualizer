import pygame, sys
from pygame.locals import *
from ease_functions import *

WIDTH = 360
HEIGHT = 50
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Easing Function Visualizer")
clock = pygame.time.Clock()

rect_obj = pygame.Rect(0, 0, 50, 50)

# the current value of the transition [0, target]
curr = 0

# the target value
target = WIDTH - rect_obj.width

# the speed of the ease function
speed = 1

# the starting value of the function
value = 0

# Game loop
while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == 27):
            pygame.quit()
            sys.exit()

    # example usage
    if curr < target:
        curr += speed
        curr = min(target, curr)
        value = linear(curr / target)  ## change the function call to any in the ease functions to change the visualizer
        rect_obj.x = value * target
        pygame.draw.rect(screen, RED, rect_obj)
    else:
        pygame.draw.rect(screen, GREEN, rect_obj)
    
    clock.tick(FPS)
    pygame.display.update()