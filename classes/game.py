from classes.grid_item import GridItem
import pygame
grid = [
    GridItem(pygame.Rect(0, 0, 300, 300), "top left"),
    GridItem(pygame.Rect(311, 0, 300, 300), "top middle"),
    GridItem(pygame.Rect(611, 0, 300, 300),  "top right"),
    GridItem(pygame.Rect(0, 311, 300, 300), "middle left"),
    GridItem(pygame.Rect(311, 311, 300, 300), "middle middle"),
    GridItem(pygame.Rect(611, 311, 300, 300), "middle right"),
    GridItem(pygame.Rect(0, 611, 300, 300), "bottom left"),
    GridItem(pygame.Rect(311, 611, 300, 300),  "bottom middle"),
    GridItem(pygame.Rect(611, 611, 300, 300), "bottom right"),
]


class Game():
    def __init__(self, screen):
        self.screen = screen
        self.grid = grid
        self.is_game_over = False
        self.turn = 1