import random

class HumanPlayer:
   def __init__(self, symbol):
       self.symbol = symbol


   def make_move(self, game, row, col):
        return game.make_move(row, col, self.symbol)


# RandomAI
class RandomAI:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, game):

        available_moves = game.get_available_moves()

        if not available_moves:
            return False
        
        row, col = random.choice(available_moves)

        return game.make_move(row, col, self.symbol)


class MinimaxAI:
    def __init__(self, symbol):
        self.symbol = symbol

    def make_move(self, game):

        # Calcularemos el mejor movimiento usando Minimax
        best_score = float("-inf")
        best_move = None

        for row, col in game.get_available_moves():
        
            # Simular movimiento de la IA
            game.board[row][col] = self.symbol
            score = self.minimax(game, False)

            # Deshacer movimiento
            game.board[row][col] = ""

            if score > best_score:
                best_score = score
                best_move = (row, col)

        if best_move is None:
            return False

        row, col = best_move

        return game.make_move(row, col, self.symbol)

    def minimax(self, game, maximizing):
        # Explora las posibilidades fuera del juego.

        # ¿Ganó la máquina?
        if game.check_winner(self.symbol):
            return 1

        # ¿Ganó el humano?
        opponent = "X" if self.symbol == "O" else "O"
        
        if game.check_winner(opponent):
            return -1

        # Empate
        if game.is_draw():
            return 0

        if maximizing:
            best_score = float("-inf")

            for row, col in game.get_available_moves():

                game.board[row][col] = self.symbol
                score = self.minimax(game, False)
                game.board[row][col] = ""
                best_score = max(best_score, score)

            return best_score

        else:
            best_score = float("inf")

            for row, col in game.get_available_moves():
                game.board[row][col] = opponent
                score = self.minimax(game, True)
                game.board[row][col] = ""
                best_score = min(best_score, score)

            return best_score       
        
      

     
    
# IRONEDIT:1789238767:1d57b:9ee51c33649ab63643335b4e4f646942b973c067fea8c82dca3e49f65fd5980a
