import pygame as py
import random


py.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), py.RESIZABLE)

comcounterp1 = 0
comcounterp2 = 0

def com1():
    global comcard
    comcard = py.image.load("ComCard/comone.png")
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    if (turn % 2 == 0):
        player1.money -= 150
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money)
    else:
        player2.money -= 150
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money)
   

def com2():
    global comcard
    comcard = py.image.load("ComCard/comtwo.png")

def com3():
    global comcard
    comcard = py.image.load("ComCard/comthree.png")

def com4():
    global comcard
    comcard = py.image.load("ComCard/comfour.png")

def com5():
    global comcard
    comcard = py.image.load("ComCard/comfive.png")

def com6():
    global comcard
    comcard = py.image.load("ComCard/comsix.png")

def com7():
    global comcard
    comcard = py.image.load("ComCard/comseven.png")

def com8():
    global comcard
    comcard = py.image.load("ComCard/comeight.png")

comlist = [com1, com2, com3, com4, com5, com6, com7, com8]

def comcardp1():
    from mnply_board import player1
    from mnply_board import end_turn
    from mnply_board import turn
    global comcounterp1
    if (((730 < player1.x < 800) and (820 < player1.y < 960)) or ((100 < player1.x < 240) and (330 < player1.y < 400)) or ((870 < player1.x < 1010) and (330 < player1.y < 400))) and (end_turn == 1) and (turn % 2 == 0):
        if comcounterp1 == 0:
            random.choice(comlist)()
            comcounterp1 = 1
        comcard_scale = py.transform.scale(comcard, (comcard.get_width()*0.5, comcard.get_height()*0.5))
        screen.blit(comcard_scale, (325, 375))
    else:
        comcounterp1 = 0
def comcardp2():
    from mnply_board import player2
    from mnply_board import end_turn
    from mnply_board import turn
    global comcounterp2
    if (((730 < player2.x < 800) and (820 < player2.y < 960)) or ((100 < player2.x < 240) and (330 < player2.y < 400)) or ((870 < player2.x < 1010) and (330 < player2.y < 400))) and (end_turn == 1) and (turn % 2 == 1):
        if comcounterp2 == 0:
            random.choice(comlist)()
            comcounterp2 = 1
        comcard_scale = py.transform.scale(comcard, (comcard.get_width()*0.5, comcard.get_height()*0.5))
        screen.blit(comcard_scale, (325, 375))
    else:
        comcounterp2 = 0

