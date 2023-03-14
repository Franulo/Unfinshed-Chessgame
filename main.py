import pygame
import time
import sys
import math

pygame.init()

SIZE = 800

BOARD = pygame.image.load("assets/board_plain_01.png")
B_KING = pygame.image.load("assets/B_King.png")
B_QUEEN = pygame.image.load("assets/B_Queen.png")
B_BISHOP = pygame.image.load("assets/B_Bishop.png")
B_ROOK = pygame.image.load("assets/B_Rook.png")
B_KNIGHT = pygame.image.load("assets/B_Knight.png")
B_PAWN = pygame.image.load("assets/B_Pawn.png")
W_KING = pygame.image.load("assets/W_King.png")
W_QUEEN = pygame.image.load("assets/W_Queen.png")
W_BISHOP = pygame.image.load("assets/W_Bishop.png")
W_ROOK = pygame.image.load("assets/W_Rook.png")
W_KNIGHT = pygame.image.load("assets/W_Knight.png")
W_PAWN = pygame.image.load("assets/W_Pawn.png")

SIZED_BOARD = pygame.transform.scale(BOARD, (800, 800))
SCREEN = pygame.display.set_mode((SIZE, SIZE))

pygame.display.set_caption("Chess")

graphical_board = [[W_ROOK, W_KNIGHT, W_BISHOP, W_KING, W_QUEEN, W_BISHOP, W_KNIGHT, W_ROOK],
                [W_PAWN, W_PAWN, W_PAWN, W_PAWN, W_PAWN, W_PAWN, W_PAWN, W_PAWN],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None],
                [B_PAWN, B_PAWN, B_PAWN, B_PAWN, B_PAWN, B_PAWN, B_PAWN, B_PAWN],
                [B_ROOK, B_KNIGHT, B_BISHOP, B_KING, B_QUEEN, B_BISHOP, B_KNIGHT, B_ROOK]]


def check_movement_rules(selected_row, selected_colum, figure, row, colum):
    if figure == W_PAWN:
        if row == selected_row+1 and colum == selected_colum and graphical_board[row][colum] is None:



def sized_Figure(image):
    return pygame.transform.scale(image, (55, 120))


def renderer():
    SCREEN.blit(SIZED_BOARD, (0, 0))
    for row, val1 in enumerate(graphical_board):
        for colum, val2 in enumerate(val1):
            if graphical_board[row][colum] is not None:
                x_coords = (100 * colum) * 0.905 + 58
                y_coords = (700 - 100 * row) * 0.9 + 10
                SCREEN.blit(sized_Figure(val2), (x_coords, y_coords))


def change_player_turn(player_turn):
    if player_turn == "White":
        return "Black"
    else:
        return "White"


def which_color(selected_row, selected_colum):
    if graphical_board[selected_row][selected_colum] == (W_PAWN or W_ROOK or W_KING or W_KNIGHT or W_BISHOP or W_QUEEN):
        return "White"
    else:
        return "Black"


def select_clicked_figure():
    mouse_posX, mouse_posY = pygame.mouse.get_pos()
    colum = round((mouse_posX - 58) / 90.5)
    row = round(((mouse_posY - 10) / 0.9 - 800) / -100)
    return row, colum


def move_to_clicked(selected_row, selected_colum):
    mouse_posX, mouse_posY = pygame.mouse.get_pos()
    colum = round((mouse_posX - 58) / 90.5)
    row = round(((mouse_posY - 10) / 0.9 - 800) / -100)
    if check_movement_rules(graphical_board[selected_row][selected_colum], selected_row, selected_colum, row, colum):
        move_figure(selected_row, selected_colum, row, colum)


def move_figure(figure_row, figure_colum, new_row, new_colum):
    print("df")
    figure = graphical_board[figure_row][figure_colum]
    graphical_board[figure_row][figure_colum] = None
    graphical_board[new_row][new_colum] = figure


def second_click(selected_row, selected_colum):
    print(selected_row, selected_colum)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # player_turn
                move_to_clicked(selected_row, selected_colum)
                main()


def main():
    global player_turn
    renderer()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected_row, selected_colum = select_clicked_figure()
                if player_turn == which_color(selected_row, selected_colum):
                    player_turn = change_player_turn(player_turn)
                    if graphical_board[selected_row][selected_colum] is not None:
                        second_click(selected_row, selected_colum)


if __name__ == "__main__":
    player_turn = "White"
    main()
