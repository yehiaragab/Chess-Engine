class King:
    def __init__(self):
        self.notation = 'K'
        self.value = 6
        self.moves = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        self.has_moved = False
        
    def movement(game, player, pos, capture=True):
        return ''