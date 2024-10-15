class Pawn:       
    def __init__(self):
        self.notation = 'P'
        self.value = 1
        self.moves = [(0, 1), (0, 2), (1, 1), (-1, 1)]
        self.has_moved = False
        
    def movement(game, player, pos, capture=True):
        return ''