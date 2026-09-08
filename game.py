
class Game:
    def __init__(self):
        self.board = self.create_board()
        self.current_player = "X"
        self.winner = None
        self.game_over = False
    
    def create_board(self):
        
        return [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    def make_move(self, row, col, symbol):
        # Coloca un simbolo SI la casilla está disponible
        if self.game_over:
            return False
        
        if self.board[row][col] != "":
            return False
        
        self.board[row][col] = symbol
        
        if self.check_winner(symbol):
            self.winner = symbol
            self.game_over = True

        elif self.is_draw():
            self.game_over = True
        return True

    def check_winner(self, symbol):
        # Comprobaremos si el símbolo ha conseguido tres en raya
        

       # Filas
        for row in self.board:
            if all(cell == symbol for cell in row):
                return True

        # Columnas
        for col in range(3):
            if all(self.board[row][col] == symbol for row in range(3)):
                return True

       # Diagonal principal
        if all(self.board[i][i] == symbol for i in range(3)):
           return True

        # Diagonal secundaria
        if all(self.board[i][2 - i] == symbol for i in range(3)):
           return True

        return False

    def is_draw(self):
    # Comprueba si el tablero está lleno sin ganador.
    
        return all(
            cell != ""
            for row in self.board
            for cell in row
        )

    def get_available_moves(self):
        moves = []
        
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    moves.append((row, col)) 

        return moves

    def reset(self):
        self.board = self.create_board()
        self.current_player = "X"
        self.winner = None
        self.game_over = False  
# IRONEDIT:1788801724:1d57b:3be0574895b29aa5c8b564f81ebfb1b46f4f8fbace14c48f6d01ad6e98106c71
