import pygame as py
import random

py.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000


screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), py.RESIZABLE)

def com1():
    global comcard
    comcard = py.image.load("ComCard/comone.png")

def com2():
    global comcard
    comcard = py.image.load("ComCard/comtwo.png")

comlist = [com1, com2]


def comcardp1():
    from mnply_board import player1
    from mnply_board import end_turn
    from mnply_board import turn
    comcardp1 = 0
    comcounterp1 = 0
    if (((730 < player1.x < 800) and (820 < player1.y < 960)) or ((100 < player1.x < 240) and (330 < player1.y < 400)) or ((870 < player1.x < 1010) and (330 < player1.y < 400))) and (end_turn == 1) and (turn % 2 == 0):
        if comcounterp1 == 0:
            random.choice(comlist)()
            comcounterp1 += 1
            
    if comcounterp1 != 0:
        screen.blit(comcard, (400, 500))

    if end_turn == 0:
        comcounterp1 = 0
    

def comcardp2():
    from mnply_board import player2
    from mnply_board import end_turn
    from mnply_board import turn
    comcounterp2 = 0
    if (((730 < player2.x < 800) and (820 < player2.y < 960)) or ((100 < player2.x < 240) and (330 < player2.y < 400)) or ((870 < player2.x < 1010) and (330 < player2.y < 400))) and (end_turn == 1) and (turn % 2 == 1):
        if comcounterp2 == 0:
            random.choice(comlist)()
            comcounterp2 += 1

    if comcounterp2 != 0:
        screen.blit(comcard, (400, 500))
    
    if end_turn == 0:
        comcounterp2 = 0

