from classes.grid_item import GridItem

import pygame
grid = [
    GridItem(pygame.Rect(0, 0, 300, 300), 0),
    GridItem(pygame.Rect(311, 0, 300, 300), 1),
    GridItem(pygame.Rect(611, 0, 300, 300),  2),
    GridItem(pygame.Rect(0, 311, 300, 300), 3),
    GridItem(pygame.Rect(311, 311, 300, 300), 4),
    GridItem(pygame.Rect(611, 311, 300, 300), 5),
    GridItem(pygame.Rect(0, 611, 300, 300), 6),
    GridItem(pygame.Rect(311, 611, 300, 300),  7),
    GridItem(pygame.Rect(611, 611, 300, 300), 8),
]


class Game():
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.grid = [
            GridItem(pygame.Rect(0, 0, 300, 300), 0),
            GridItem(pygame.Rect(311, 0, 300, 300), 1),
            GridItem(pygame.Rect(611, 0, 300, 300),  2),
            GridItem(pygame.Rect(0, 311, 300, 300), 3),
            GridItem(pygame.Rect(311, 311, 300, 300), 4),
            GridItem(pygame.Rect(611, 311, 300, 300), 5),
            GridItem(pygame.Rect(0, 611, 300, 300), 6),
            GridItem(pygame.Rect(311, 611, 300, 300),  7),
            GridItem(pygame.Rect(611, 611, 300, 300), 8),
        ]
        self.turn = 1
        self.winner = None

    def take_turn(self, pos):
        box = None
        for grid_element in self.grid:
            if grid_element.rect.collidepoint(pos):
                box = grid_element
                break
        # user going to click on screen
        # if box is checked, shake screen
        # else set box to checked and rerender screen
        # check winner, if winner show alert to reset with winner
        if box is None:
            pass
        if box.checked:
            print("Taken")
            pass
        else:
            box.set_checked(self.turn)
            image = pygame.image.load('./x.png') if self.turn == 1 else pygame.image.load('./o.png')
            self.screen.blit(pygame.transform.scale(image, box.rect[2:]), box.rect[:2])
            pygame.display.flip()
    def check_winner(self):
        return False
        winning_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
            0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

        # loops through all the squares and checks for winning combinaitions
    def change_turn(self):
        if self.turn == 1:
            self.turn = 2
            print("Changing to player 2")
        else:
            print("Changing to player 1")
            self.turn = 1
