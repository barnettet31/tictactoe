import pygame
class GridItem:
    def __init__(self, rect:pygame.Rect, number):
        self.rect = rect
        self.number = number
        self.checked = False
        self.player = 0

    def set_checked(self, player_number):
        if self.checked:
            return False
        self.checked = True
        self.player = player_number
        
        return True
    def return_number(self):
        return self.number
    def return_player(self):
        return self.player
