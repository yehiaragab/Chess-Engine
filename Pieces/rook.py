class Rook:
    def __init__(self):
        self.notation = 'R'
        self.value = 5
        self.moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.has_moved = False
        
    def movement(game, player, pos, capture=True):
        return ''