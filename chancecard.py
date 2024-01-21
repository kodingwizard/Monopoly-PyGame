import pygame as py
import random

py.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), py.RESIZABLE)

chancecounterp1 = 0
chancecounterp2 = 0

def chance1():
    global chancecard
    chancecard = py.image.load("ChanceCards/chancecardone.png")

def chance2():
    global chancecard
    chancecard = py.image.load("ChanceCards/chancecardtwo.png")

def chance3():
    global chancecard
    chancecard = py.image.load("ChanceCards/chancecardthree.png")

def chance4():
    global chancecard
    chancecard = py.image.load("ChanceCards/chancecardfour.png")

def chance5():
    global chancecard
    chancecard = py.image.load("ChanceCards/chancecardfive.png")

def chance6():
    global chancecard
    chancecard = py.image.load("ChanceCards/chancecardsix.png")

def chance7():
    global chancecard
    chancecard = py.image.load("ChanceCards/chancecardseven.png")

chancelist = [chance1, chance2, chance3, chance4, chance5, chance6, chance7]

def chancecardp1():
    from mnply_board import player1
    from mnply_board import end_turn
    from mnply_board import turn
    global chancecounterp1
    if(((380 < player1.x < 450) and (820 < player1.y < 960)) or ((310 < player1.x < 380) and (50 < player1.y < 190)) or ((870 < player1.x < 1100) and (520 < player1.y < 590))) and (end_turn == 1) and (turn % 2 == 0):
        if chancecounterp1 == 0:
            random.choice(chancelist)()
            chancecounterp1 = 1
        screen.blit(chancecard, (400, 500))
    else:
        chancecounterp1 = 0

def chancecardp2():
    from mnply_board import player2
    from mnply_board import end_turn
    from mnply_board import turn
    global chancecounterp2
    if(((380 < player2.x < 450) and (820 < player2.y < 960)) or ((310 < player2.x < 380) and (50 < player2.y < 190)) or ((870 < player2.x < 1100) and (520 < player2.y < 590))) and (end_turn == 1) and (turn % 2 == 1):
        if chancecounterp2 == 0:
            random.choice(chancelist)()
            chancecounterp2 = 1
        screen.blit(chancecard, (400, 500))
    else:
        chancecounterp2 = 0


