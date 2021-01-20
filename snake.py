import pygame
from pygame.sprite import Sprite


class Cell(Sprite):

    def __init__(self, settings, x, y):

        super().__init__()
        self.settings = settings

        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.settings.cell_size, self.settings.cell_size)


class Snake:

    def __init__(self, game):

        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        self.body = []
        self.choose_direction = ''
        self.direction = 'up'

    def start(self):
        for i in range(self.settings.snake_size):
            pos = self.screen_rect.centerx, self.screen_rect.centery+(i-1)*self.settings.cell_size
            self.body.append(Cell(self.settings, *pos))

    def draw(self):
        for sprite in self.body:
            pygame.draw.rect(self.screen, self.settings.cell_color, sprite.rect)

    def change_direction(self):
        if self.choose_direction == 'up' and self.direction != 'down':
            self.direction = 'up'
        elif self.choose_direction == 'down' and self.direction != 'up':
            self.direction = 'down'
        elif self.choose_direction == 'right' and self.direction != 'left':
            self.direction = 'right'
        elif self.choose_direction == 'left' and self.direction != 'right':
            self.direction = 'left'
