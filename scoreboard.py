import pygame


class Scoreboard:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.place_scoreboard = pygame.Rect(0, 0, *self.settings.scoreboard_size)

        self.prep_score()
        self.prep_best_score()
        self.prep_level()

    def prep_score(self):
        score_str = f'Score: {self.settings.score:,}'
        self.score_image = pygame.font.SysFont(None, 40, True).render(score_str, True, self.settings.score_color,
                                                                      self.settings.scoreboard_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.place_scoreboard.left + 20
        self.score_rect.top = self.place_scoreboard.top + 5

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)

    def prep_best_score(self):
        best_score_str = f"Best score: {self.settings.best_score:,}"
        self.best_score = pygame.font.SysFont(None, 32).render(best_score_str, True, self.settings.score_color,
                                                               self.settings.scoreboard_color)
        self.best_score_rect = self.best_score.get_rect()
        self.best_score_rect.top = self.score_rect.bottom + 7
        self.best_score_rect.left = self.place_scoreboard.left + 20

    def show_best_score(self):
        self.screen.blit(self.best_score, self.best_score_rect)

    def prep_level(self):
        level_str = f'Level: {self.settings.level}'
        self.level = pygame.font.SysFont(None, 32).render(level_str, True, self.settings.score_color,
                                                          self.settings.scoreboard_color)
        self.level_rect = self.level.get_rect()
        self.level_rect.top = self.best_score_rect.bottom + 7
        self.level_rect.left = self.place_scoreboard.left + 20

    def show_level(self):
        self.screen.blit(self.level, self.level_rect)
