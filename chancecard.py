import pygame as py

py.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000


screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), py.RESIZABLE)


def chancecardp1():
    from mnply_board import player1
    from mnply_board import end_turn
    from mnply_board import turn
    if(((380 < player1.x < 450) and (820 < player1.y < 960)) or ((310 < player1.x < 380) and (50 < player1.y < 190)) or ((870 < player1.x < 1100) and (520 < player1.y < 590))) and (end_turn == 1) and (turn % 2 == 0):
        chance_test = py.image.load("ChanceCards/chancecard.png")
        screen.blit(chance_test, (100,100))

def chancecardp2():
    from mnply_board import player2
    from mnply_board import end_turn
    from mnply_board import turn
    if(((380 < player2.x < 450) and (820 < player2.y < 960)) or ((310 < player2.x < 380) and (50 < player2.y < 190)) or ((870 < player2.x < 1100) and (520 < player2.y < 590))) and (end_turn == 1) and (turn % 2 == 1):
        chance_test = py.image.load("ChanceCards/chancecard.png")
        screen.blit(chance_test, (100,100))

