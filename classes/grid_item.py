class GridItem:
    def __init__(self, rect, name):
        self.rect = rect
        self.name = name
        self.checked = False
        self.player = 0

    def set_checked(self, player_number):
        if self.checked:
            return False
        self.checked = True
        self.player = player_number
        return True
