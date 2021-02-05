import pygame
import math
from game import Game
from player import Player
from projectile import Projectile
pygame.init()

#definir une clock
clock = pygame.time.Clock()
FPS = 60


pygame.display.set_caption("nerve attack")
screen_width = 1300
screen_height = 600
screen = pygame.display.set_mode((1300, 600))
background = pygame.image.load('assets/bg.jpg')
background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 3.33)
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2.9)
play_button_rect.y = math.ceil(screen.get_height() / 1.6)
game = Game()
player = Player(game)
running = True

while running:

    screen.blit(background, (0, 0))

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


    print(game.player.rect.x)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("exit game")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    game.start()
                    # jouer le son
                    game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
                #jouer le son
                game.sound_manager.play('click')
    #fixer le nombre de FPS sur ma clock
    clock.tick(FPS)



