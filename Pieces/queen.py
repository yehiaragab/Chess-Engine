class Queen:
    def __init__(self):
        self.notation = 'Q'
        self.value = 9
        self.moves = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        
    def movement(game, player, pos, capture=True):
        return ''