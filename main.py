import pygame
# from classes.square import Square
from classes.game import Game
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 900

# set screen width/height
WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# game name
pygame.display.set_caption("Travis' TicTacToe")

# background color && grid
color = (255, 255, 255)

# left top width height
lines = [pygame.Rect(300, 0, 10, 920),
         pygame.Rect(600, 0, 10, 920),
         pygame.Rect(0, 300, 920, 10),
         pygame.Rect(0, 600, 920, 10)]


WINDOW.fill(color)
for line in lines:
    pygame.draw.rect(WINDOW, (0, 0, 0), line)
# trigger render
pygame.display.flip()


def main():
    run = True
    while run:
        game = Game(WINDOW)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos
                game.take_turn(mouse_position)
                game_over = game.check_winner()
                if game_over:
                    print(game.winner)
                else:
                    game.change_turn()

                
                        
    pygame.quit()


if __name__ == "__main__":
    main()
