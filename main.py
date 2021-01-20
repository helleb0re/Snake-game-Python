import sys
import pygame
import random
import time
from settings import Settings
from map import Map
from snake import Snake, Cell
from scoreboard import Scoreboard


class SnakeGame:

    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Snake')

        self.snake = Snake(self)
        self.map = Map(self)
        self.scoreboard = Scoreboard(self)

    def run(self):
        self.map.make_map()
        self._create_point()
        self.snake.start()
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.snake.choose_direction = 'right'
        elif event.key == pygame.K_LEFT:
            self.snake.choose_direction = 'left'
        elif event.key == pygame.K_UP:
            self.snake.choose_direction = 'up'
        elif event.key == pygame.K_DOWN:
            self.snake.choose_direction = 'down'

    def _create_point(self):
        self.food = Cell(self.settings, *random.choice(self.map.grid))
        while pygame.sprite.spritecollideany(self.food, self.snake.body):
            self.food = Cell(self.settings, *random.choice(self.map.grid))

    def _check_snake(self):
        if self.snake.body[0].x < 0 or self.snake.body[0].x >= self.settings.screen_width:
            self.game_over()
        elif self.snake.body[0].y < self.settings.scoreboard_size[1]\
                or self.snake.body[0].y >= self.settings.screen_height:
            self.game_over()
        if pygame.sprite.spritecollideany(self.snake.body[0], self.snake.body[1:]):
            self.game_over()

    def game_over(self):
        with open('best_score.txt', 'w') as f:
            print(self.settings.best_score, file=f)
        time.sleep(1)
        sys.exit()

    def _check_collision(self, head):
        if head.x == self.food.x and head.y == self.food.y:
            self.food.kill()
            self._update_score()
            self._increase_level()
            self._create_point()
            return False
        return True

    def _increase_level(self):
        if self.settings.counter_food % 5 == 0 and self.settings.counter_food != 0:
            self.settings.level += 1
            self.scoreboard.prep_level()
            self.settings.point = self.settings.up_point*self.settings.level

    def _update_score(self):
        self.settings.score += self.settings.point
        self.settings.counter_food += 1
        self.scoreboard.prep_score()
        if self.settings.score > self.settings.best_score:
            self.settings.best_score = self.settings.score
            self.scoreboard.prep_best_score()

    def snake_move(self):
        self.snake.change_direction()
        head = self.snake.body[0]
        if self.snake.direction == 'up':
            new_cell = Cell(self.settings, head.x, head.y - self.settings.cell_size)
        elif self.snake.direction == 'down':
            new_cell = Cell(self.settings, head.x, head.y + self.settings.cell_size)
        elif self.snake.direction == 'right':
            new_cell = Cell(self.settings, head.x+self.settings.cell_size, head.y)
        elif self.snake.direction == 'left':
            new_cell = Cell(self.settings, head.x-self.settings.cell_size, head.y)
        if self._check_collision(new_cell):
            self.snake.body.pop()
        self.snake.body = [new_cell] + self.snake.body

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.draw.rect(self.screen, self.settings.scoreboard_color, self.scoreboard.place_scoreboard)
        self.snake_move()
        pygame.draw.rect(self.screen, self.settings.food_color, self.food.rect)
        self.snake.draw()
        self._check_snake()
        self.scoreboard.show_score()
        self.scoreboard.show_best_score()
        self.scoreboard.show_level()

        pygame.display.flip()
        pygame.time.Clock().tick(15)


if __name__ == '__main__':
    game = SnakeGame()
    game.run()
