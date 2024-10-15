from Pieces import *

class Chess:
    def __init__(self, EPD= 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -'):
        self.x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.y = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.notation = {'p':1, 'n':2, 'b':3, 'r':4, 'q':5, 'k':6}
        self.parts = {1: 'Pawn', 2: 'Knight', 3: 'Bishop', 4: 'Rook', 5: 'Queen', 6: 'King'}
        self.reset(EPD=EPD)
        
    def reset(self, EPD= 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -'):
        self.log = []
        self.init_pos = EPD
        self.EPD_table = {}
        self.p_move = 1
        self.castling = [True, True, True, True]
        self.en_passant = None
        self.board = [[0 for i in range(8)] for j in range(8)]
        self.load_EPD(EPD)
    
    
    def load_EPD(self,EPD):
        data = EPD.split(' ')
        if len(data) == 4:
            for x,rank in enumerate(data[0].split('/')):
                y = 0
                for p in rank:
                    if p.isdigit():
                        for i in range(int(p)):
                            self.board[x][y] = 0
                            y += 1
                    else:
                        self.board[x][y] = self.notation[str(p).lower()]*(-1) if str(p).islower() else self.notation[str(p).lower()]
                        y += 1
            self.p_move = 1 if data[1] == 'w' else -1
            if 'K' in data[2]:
                self.castling[0] = 1
            else:
                self.castling[0] = 0
            if 'Q' in data[2]:
                self.castling[1] = 1
            else:
                self.castling[1] = 0
            if 'k' in data[2]:
                self.castling[2] = 1
            else:
                self.castling[2] = 0
            if 'q' in data[2]:
                self.castling[3] = 1
            else:
                self.castling[3] = 0
            self.en_passant = None if data[3] == '-' else self.board_2_array(data[3])
            return True
        else:
            return False
        
    def display(self):
        result = '  a b c d e f g h  \n  ----------------\n'
        for c, row in enumerate(self.board):
            result += f'{8-c}|'
            for piece in row:
                if piece != 0:
                    # If piece is negative, it's a black piece, otherwise it's white
                    piece_char = list(self.notation.keys())[list(self.notation.values()).index(abs(piece))]
                    result += piece_char.lower() if piece < 0 else piece_char.upper()
                else:
                    result += '.'
                result += ' '
            result += f'|{8-c}\n'
        result += '  ----------------\n  a b c d e f g h\n'
        print(result)

    def board_to_array(self, pos):
        return ''
        
    def EPD_hash(self):
        return ''
    
    def log_move(self, part, cur_cord, next_cord, cur_pos, new_pos):
        return ''
    
    def move(self, cur_pos, new_pos):
        return ''
    
    def valid_move(self, cur_pos, new_pos):
        return ''
    
    def possible_moves(self, capture=True):
        return ''
    
    def is_checkmate(self, moves):
        return ''
    
    def pawn_promotion(self, cur_pos, new_pos):
        return ''
    
    def fifty_move_rule(self, moves):
        return ''
    
    def threefold_repetition(self, hash):
        return ''
    
    def insufficient_material(self):
        return ''
    
    def stalemate(self):
        return ''
    
    def draw(self):
        return ''
    
    def end(self):
        return ''
    
    def check_state(self, hash):
        return ''
    

if __name__ == '__main__':
    chess = Chess()
    chess.display()