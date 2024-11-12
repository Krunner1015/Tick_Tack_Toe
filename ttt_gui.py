import sys
import pygame
from constants import *
from tictactoe import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

#to draw X and Os
chip_font = pygame.font.Font(None, CHIP_FONT)
game_over_font = pygame.font.Font(None, GAME_OVER_FONT)

#initialize board
board = initialize_board()

def draw_grid():
    #draw horizontal lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )
    #draw vertical lines
    for i in range(1, BOARD_COLS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, HEIGHT),
            LINE_WIDTH
        )

def draw_chips():
    chip_x_surf = chip_font.render("x", 0, CROSS_COLOR)
    chip_o_surf = chip_font.render("o", 0, CIRCLE_COLOR)

    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == "x":
                chip_x_rect = chip_x_surf.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE/2, row * SQUARE_SIZE + SQUARE_SIZE/2))
                screen.blit(chip_x_surf, chip_x_rect)
            elif board[row][col] == "o":
                chip_o_rect = chip_o_surf.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE/2, row * SQUARE_SIZE + SQUARE_SIZE/2))
                screen.blit(chip_o_surf, chip_o_rect)

def draw_game_over():
    screen.fill(BG_COLOR)
    end_surf = game_over_font.render(end_text, 0, LINE_COLOR)
    end_rect = end_surf.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
    screen.blit(end_surf, end_rect)

    restart_text = "Press r to play the game again..."
    restart_surf = game_over_font.render(restart_text, 0, LINE_COLOR)
    restart_rect = restart_surf.get_rect(center=(WIDTH//2, HEIGHT//2 + 100))
    screen.blit(restart_surf, restart_rect)

screen.fill(BG_COLOR)
draw_grid()
game_over = False
count = 1

while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row = y//200
            col = x//200
            print(x, y)
            print(row, col)

            if count == 1 and available_square(board, row, col):
                board[row][col] = "x"
                draw_chips()

                if check_if_winner(board, "x"):
                    end_text = "X is the winner!"
                    game_over = True

                count += 1
            elif count == 2 and available_square(board, row, col):
                board[row][col] = "o"
                draw_chips()
                if check_if_winner(board, "o"):
                    end_text = "O is the winner!"
                    game_over = True

                count -= 1

            if board_is_full(board):
                end_text = "Noone wins!"
                game_over = True

            print_board(board)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                #restart the game
                board = initialize_board()
                screen.fill(BG_COLOR)
                draw_grid()
                game_over = False
                count = 1

        if game_over:
            pygame.display.update()
            pygame.time.delay(1000)
            draw_game_over()
            
    pygame.display.update()
