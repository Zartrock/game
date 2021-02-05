import pygame
from projectile import Projectile
import animation
class Player(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity_x = 5
        self.velocity_y = 5
        self.velocity_y_2 = 170
        self.velocity_y_3 = 10
        self.velocity_y_4 = 30
        self.velocity_y_5 = 50
        self.velocity_y_6 = 80
        self.velocity_y_7 = 110
        self.velocity_y_8 = 140
        self.velocity_y_9 = 170
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 340
        self.jump = self.rect.y - 170

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):

        pygame.draw.rect(surface, (60, 63, 60),
                         [self.rect.x + 50, self.rect.y + 20,
                          self.max_health, 7])

        pygame.draw.rect(surface, (111, 210, 46),
                         [self.rect.x + 50, self.rect.y + 20,
                          self.health, 7])



    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        self.start_animation()
        #jouer le son
        self.game.sound_manager.play('tir')


    def move_right(self):
        if not self.game.check_collision(self, self.
                game.all_monsters):
            self.rect.x += self.velocity_x

    def move_left(self):
        self.rect.x -= self.velocity_x










