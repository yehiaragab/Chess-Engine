class Knight:
    def __init__(self):
        self.notation = 'N'
        self.value = 2
        self.moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        
    def movement(game, player, pos, capture=True):
        return ''