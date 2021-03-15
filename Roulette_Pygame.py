import pygame
import sys
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

GRIDSIZE = 50
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_surface = pygame.Surface([900, 750])
game_surface.fill(color="grey")

direction = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
GREEN = "#006600"
BLACK = "#000000"
RED = "#FF0000"
class Board(object):
    pass
class Wheel(object):
    def __init__(self):
        self.image = pygame.image.load(r"C:\Users\Josh\PycharmProjects\pythonProject\Roulette_wheel.png")
    def draw(self, screen):
        screen.blit(self.image, [10, 10])

def draw_grid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            case1_columns = [0, 2, 5, 8, 9, 11]  # case 1: columns [0,2,5,8,9,11] are all red -> black -> red going up
            case2_columns = [1, 4, 7, 10]  # case 2: columns [1,4,7,10] are all black -> red -> black
            case3_columns = [3, 6]  # case 3: columns [3,6] are all black -> black -> red
            if (x + y) % 2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, GREEN, r)
            else:
                rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, RED, rr)
wheel = Wheel()
def main():
    #draw_grid(game_surface)
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    wheel.draw(game_surface)
    while True:
        screen.fill("white")
        screen.blit(game_surface, (10, 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        clock.tick(10)
        pygame.display.update()

main()