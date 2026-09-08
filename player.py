import random

class HumanPlayer:
    def __init__(self, symbol):
        self.symbol = symbol
    
    def make_move(self, game, row, col):
        return game.make_move(row, col, self.symbol)

class RandomAI:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, game):
       # Selecciona aleatoriamente una casilla disponible 
        
        available_moves = game.get_available_moves()

        if not available_moves:
            return False

        row, col = random.choice(available_moves)

        if not available_moves:
            return False

        row, col = random.choice(available_moves)
        
        return game.make_move(row, col, self.symbol)
# IRONEDIT:1788798054:1d57b:fc2d4092b5b1ab966012278d35da965194c5b9e63d2949516a84d9b6919645b3
