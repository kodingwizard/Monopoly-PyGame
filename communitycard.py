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
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree, player1.orbit)
    else:
        player2.money -= 150
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit)
   

def com2():
    global comcard
    comcard = py.image.load("ComCard/comtwo.png")
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    if (turn % 2 == 0):
        player1.money += 200
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree, player1.orbit)
    else:
        player2.money += 200
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit)

def com3():
    global comcard
    comcard = py.image.load("ComCard/comthree.png")
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    if (turn % 2 == 0):
        player1.money -= 25
        player1.jailfree += 1
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree, player1.orbit)
    else:
        player2.money -= 25
        player2.jailfree += 1
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit)

def com4():
    global comcard
    comcard = py.image.load("ComCard/comfour.png")
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    if (turn % 2 == 0):
        player1.money += 100
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree, player1.orbit)
    else:
        player2.money += 100
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit)

def com5():
    global comcard
    comcard = py.image.load("ComCard/comfive.png")
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    if (turn % 2 == 0):
        player1.money -= 200
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree, player1.orbit)
    else:
        player2.money -= 200
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit)

def com6():
    global comcard
    comcard = py.image.load("ComCard/comsix.png")
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    if (turn % 2 == 0):
        player1.money -= 35
        player2.money += 35
        player1.jailfree += 1
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree, player1.orbit)
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit)
    else:
        player2.money -= 35
        player1.money += 35
        player2.jailfree += 1
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit)
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree, player1.orbit)


def com7():
    global comcard
    comcard = py.image.load("ComCard/comseven.png")
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    if (turn % 2 == 0):
        player1.money += 100
        player2.money -= 100
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree, player1.orbit)
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit)
    else:
        player2.money += 100
        player1.money -= 100
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit)
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree, player1.orbit)

def com8():
    global comcard
    comcard = py.image.load("ComCard/comeight.png")
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    if (turn % 2 == 0):
        player1.jailfree += 1
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree, player1.orbit)
    else:
        player2.jailfree += 1
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit)

comlist = [com1, com2, com3, com4, com5, com6, com7, com8]

def comcardp1():
    from mnply_board import player1
    from mnply_board import end_turn
    from mnply_board import turn
    global comcounterp1
    if (((730 < player1.x < 800) and (760 < player1.y < 900)) or ((100 < player1.x < 240) and (270 < player1.y < 340)) or ((870 < player1.x < 1010) and (270 < player1.y < 360))) and (end_turn == 1) and (turn % 2 == 0):
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
    if (((730 < player2.x < 800) and (760 < player2.y < 900)) or ((100 < player2.x < 240) and (270 < player2.y < 340)) or ((870 < player2.x < 1010) and (270 < player2.y < 340))) and (end_turn == 1) and (turn % 2 == 1):
        if comcounterp2 == 0:
            random.choice(comlist)()
            comcounterp2 = 1
        comcard_scale = py.transform.scale(comcard, (comcard.get_width()*0.5, comcard.get_height()*0.5))
        screen.blit(comcard_scale, (325, 375))
    else:
        comcounterp2 = 0

