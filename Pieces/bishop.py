class Bishop:
    def __init__(self):
        self.notation = 'B'
        self.value = 3
        self.moves = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
        
    def movement(game, player, pos, capture=True):
        return ''