import pygame

from game import Game
from player import HumanPlayer, RandomAI
from settings import (
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
    BUTTON_TEXT_COLOR
)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tres en Raya")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)

game = Game()
human = HumanPlayer(HUMAN_SYMBOL)
machine = RandomAI(MACHINE_SYMBOL)
running = True

# Dibujar el tablero

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
    # Dibujar X o O dependiendo del estado del tablero

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
        center=(WIDTH // 2, BOARD_SIZE + 50)
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
        border_radius = 10    
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

while running:
    for event in pygame.event.get():
        
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
            
            # Si la partifa terminó, no permitir movimientos
            if game.game_over:
                continue

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
    draw_board()
    draw_symbols()
    draw_message()
    draw_restart_button()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

   
# IRONEDIT:1788887063:1d57b:5fb828ae6942f162875d2f0f0c4375037ff171bdfd89b93726fdcab4c2ce1c6f
