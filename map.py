class Map:

    def __init__(self, game):

        self.screen = game.screen
        self.settings = game.settings
        self.grid = []

    def make_map(self):
        for y in range(100, self.screen.get_height(), self.settings.cell_size):
            for x in range(0, self.screen.get_width(), self.settings.cell_size):
                self.grid.append((x, y))
