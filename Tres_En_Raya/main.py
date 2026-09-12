import pygame

from game import Game
from player import HumanPlayer, MinimaxAI, RandomAI
from settings import(
    WIDTH,
    HEIGHT,
    BOARD_SIZE,
    CELL_SIZE,
    FPS,
    BACKGROUND_COLOR,
    LINE_COLOR,
    X_COLOR,
    O_COLOR,
    TEXT_COLOR,
    LINE_WIDTH,
    HUMAN_SYMBOL,
    MACHINE_SYMBOL,
    BUTTON_WIDTH,
    BUTTON_HEIGHT,
    BUTTON_X,
    BUTTON_Y,
    BUTTON_COLOR,
    BUTTON_HOVER_COLOR,
    BUTTON_TEXT_COLOR,
    X_HINT_COLOR
)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tres en Raya")

clock = pygame.time.Clock()

font = pygame.font.Font(None, 50)
game = Game()

human = HumanPlayer(HUMAN_SYMBOL)
machine = MinimaxAI(MACHINE_SYMBOL)
randomAI = RandomAI("O")
minimax_auto = MinimaxAI("X")

game_mode = None

running = True

def draw_board():

    screen.fill(BACKGROUND_COLOR)

    # Líneas verticales
    for x in range(1, 3):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (x * CELL_SIZE, 0),
            (x * CELL_SIZE, BOARD_SIZE),
            LINE_WIDTH
        )

    # Líneas horizontales
    for y in range(1, 3):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, y * CELL_SIZE),
            (BOARD_SIZE, y * CELL_SIZE),
            LINE_WIDTH
        )

def draw_symbols():
    # Dibuja X y 0 dependidendo del estado del tablero

    for row in range(3):
        for col in range(3):
            symbol = game.board[row][col]

            center_x = col * CELL_SIZE + CELL_SIZE // 2
            center_y = row * CELL_SIZE + CELL_SIZE // 2

            if symbol == "X":
                padding = 50

                pygame.draw.line(
                   screen, 
                   X_COLOR,
                   (
                      center_x - padding,
                      center_y - padding
                   ),
                   (
                      center_x + padding,
                      center_y + padding
                   ),
                    LINE_WIDTH 
                )

                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                       center_x + padding,
                       center_y - padding
                    ),
                    (
                        center_x - padding,
                        center_y + padding
                    ),
                    LINE_WIDTH
                )


            elif symbol == "O":
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (center_x, center_y),
                    70,
                    LINE_WIDTH
                )

# Dibujar las posibles jugadas

def draw_available_moves():
    if game.game_over:
        return

    if game.current_player != HUMAN_SYMBOL:
        return

    for row, col in game.get_available_moves():
        
        center_x = col * CELL_SIZE + CELL_SIZE // 2
        center_y = row * CELL_SIZE + CELL_SIZE // 2
        
        padding = 50

        pygame.draw.line(
            screen,
            X_HINT_COLOR,
            (
               center_x - padding,
               center_y - padding
            ),
            (
               center_x + padding,
               center_y + padding
            ), 
            LINE_WIDTH
        )

        pygame.draw.line(
            screen,
            X_HINT_COLOR,
            (
               center_x + padding,
               center_y - padding
            ),
            (
               center_x - padding,
               center_y + padding
            ),
            LINE_WIDTH
        )

def draw_message():
    if game.game_over:
        
        if game.winner == HUMAN_SYMBOL:
            message = "¡Ganaste!"

        elif game.winner == MACHINE_SYMBOL:
            message = "La máquina ha ganado"

        else: 
            message = "¡Empate!"

    else:
        message = "Tu turno"


    text = font.render(message, True, TEXT_COLOR)
    
    text_rect = text.get_rect(
        center = (WIDTH // 2, BOARD_SIZE + 50)
     )

    screen.blit(text, text_rect)

# Imprimir ganador en el modo minimax vs randomAI

RANDOM_AI_SYMBOL = "O"
MINIMAX_SYMBOL = "X"

def draw_message_minimax_random():
    if game.game_over:
       if game.winner == MINIMAX_SYMBOL:
           message = "MinimaxAI ha ganado"
       elif game.winner == RANDOM_AI_SYMBOL:
           message = "RandomAI ha ganado"

       else:
           message = "Empate"

    else: 
        message = "Procesando... "
    
    text = font.render(message, True, TEXT_COLOR)
    
    text_rect = text.get_rect(
        center = (WIDTH // 2, BOARD_SIZE + 50)
    )

    screen.blit(text, text_rect)

def draw_restart_button():
    
    mouse_pos = pygame.mouse.get_pos()

    button_rect = pygame.Rect(
        BUTTON_X,
        BUTTON_Y,
        BUTTON_WIDTH,
        BUTTON_HEIGHT
    )
    
    if button_rect.collidepoint(mouse_pos):
        color = BUTTON_HOVER_COLOR
    
    else:
        color = BUTTON_COLOR

    pygame.draw.rect(
        screen,
        color, 
        button_rect,
        border_radius=10
    )

    text = font.render(
        "Reiniciar",
        True,
        BUTTON_TEXT_COLOR 
    )

    text_rect = text.get_rect(
        center = button_rect.center
    )

    screen.blit(text, text_rect)

def get_cell_from_mouse(position):
    x, y = position

    if y >= BOARD_SIZE:
        return None

    col = x // CELL_SIZE
    row = y // CELL_SIZE

    return row, col

def get_menu_buttons():
    button1 = pygame.Rect(
        100,
        200,
        WIDTH - 200,
        70
    )   

    button2 = pygame.Rect(
        100,
        300,
        WIDTH - 200,
        70
    )

    return button1, button2

def draw_menu():
    screen.fill(BACKGROUND_COLOR)
    
    title_font = pygame.font.Font(None, 70)
    button_font = pygame.font.Font(None, 40)

    title = title_font.render(
        "Tres en Raya",
        True,
        TEXT_COLOR
    ) 

    title_rect = title.get_rect(
        center = (WIDTH // 2, 100)
    )

    screen.blit(title, title_rect)

    button1, button2 = get_menu_buttons()
    
    """
    button1 = pygame.Rect(
        100,
        200,
        WIDTH - 200,
        70    
    )

    button2 = pygame.Rect(
        100,
        300,
        WIDTH - 200,
        70
    )
    """

    pygame.draw.rect(
        screen,
        BUTTON_COLOR,
        button1,
        border_radius=10
    )

    pygame.draw.rect(
        screen,
        BUTTON_COLOR,
        button2,
        border_radius = 10
    )

    text1 = button_font.render(
        "Humano vs Minimax",
        True,
        BUTTON_TEXT_COLOR
    )

    text2 = button_font.render(
        "Minimax vs Random",
        True,
        BUTTON_TEXT_COLOR
    )

    screen.blit(
        text1,
        text1.get_rect(center=button1.center)
    )
    
    screen.blit(
        text2,
        text2.get_rect(center=button2.center)
    )
    
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False
            
       if game_mode is None:
           if event.type == pygame.MOUSEBUTTONDOWN:
               button1, button2 = get_menu_buttons()

               if button1.collidepoint(event.pos):
                   game_mode = "human_vs_minimax"
                   game.reset()

               elif button2.collidepoint(event.pos):
                   game_mode = "minimax_vs_random"
                   game.reset()

           continue  

       if event.type == pygame.MOUSEBUTTONDOWN:
           
           mouse_x, mouse_y = event.pos
        
           restart_button = pygame.Rect(
                BUTTON_X,
                BUTTON_Y,
                BUTTON_WIDTH,
                BUTTON_HEIGHT
           )


            # Comprobar si se pulsó Reiniciar
           if restart_button.collidepoint(mouse_x, mouse_y):
               game.reset()

               continue

            # Si la partida terminó, no permitir más movimientos
           if game.game_over:
               continue

             # Solo el jugador humano puede mover en su turno:
           if game.current_player != HUMAN_SYMBOL:
               continue

           cell = get_cell_from_mouse(event.pos)
        
           if cell is None:
               continue

           row, col = cell

           if human.make_move(game, row, col):

               if not game.game_over:
                   game.current_player = MACHINE_SYMBOL
                   machine.make_move(game)

                   if not game.game_over:
                       game.current_player = HUMAN_SYMBOL

       if game_mode == "minimax_vs_random" and not game.game_over:
           if game.current_player == "X":
               minimax_auto.make_move(game)

               if not game.game_over:
                   game.current_player = "O"

           elif game.current_player == "O":
               randomAI.make_move(game)

               if not game.game_over:
                   game.current_player = "X"
            

     # Dibujar la pantalla:
   if game_mode is None:
       draw_menu()

   elif game_mode == "minimax_vs_random":
       draw_board()
       draw_available_moves()
       draw_symbols()
       draw_message_minimax_random()
       draw_restart_button()
   else:
       draw_board()
       draw_available_moves()
       draw_symbols()
       draw_message()
       draw_restart_button()
    
   pygame.display.flip()
   clock.tick(FPS)

   # Modo de juego: RandomAI vs MinimaxAI


pygame.quit()
        
# IRONEDIT:1789234708:1d57b:3576de82cef050060fc8c5cb9a5bf0fa0b8e9cea2fd2973c97114c703e21ba76
