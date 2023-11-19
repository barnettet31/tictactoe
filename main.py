import pygame
import time
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 900 , 900

# set screen width/height
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# game name
pygame.display.set_caption("Travis' TicTacToe")

# background color && grid
color = (255, 255, 255)


lines = [pygame.Rect(300, 0, 10, 920),
         pygame.Rect(600, 0, 10, 920),
         pygame.Rect(0, 300, 920, 10),
         pygame.Rect(0, 600, 920, 10)]
WINDOW.fill(color)
for line in lines:
    pygame.draw.rect(WINDOW, (0, 0, 0), line)
# Drawing Rectangle
pygame.display.flip()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()


if __name__ == "__main__":
    main()
