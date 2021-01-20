class Settings:

    def __init__(self):

        self.screen_width = 800
        self.screen_height = 700
        self.score = 0
        self.scoreboard_size = 800, 100
        self.scoreboard_color = (191, 191, 191)
        with open('best_score.txt', 'r') as f:
            self.best_score = int(f.read())

        self.bg_color = (0, 0, 0)

        self.snake_size = 3

        self.cell_size = 25
        self.cell_color = (0, 255, 0)

        self.food_color = (255, 0, 0)

        self.score_color = (0, 0, 0)

        self.counter_food = 0
        self.increase_points = 2
        self.level = 1
        self.point = 10
        self.up_point = 10