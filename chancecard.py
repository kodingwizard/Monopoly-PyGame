import pygame as py
import random

py.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), py.RESIZABLE)

chancecounterp1 = 0
chancecounterp2 = 0

def chance1():
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    global chancecard
    chancecard = py.image.load("ChanceCards/chancecardone.png")
    if (turn % 2 == 0):
        player1.x = 888
        player1.y = 843
        player1.money += 200
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree)
    elif (turn % 2 == 1):
        player2.x = 888
        player2.y = 897
        player2.money += 200
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree)

def chance2():
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    global chancecard
    chancecard = py.image.load("ChanceCards/chancecardtwo.png")
    if (turn % 2 == 0):
        player1.money -= 100
        player2.money += 100
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree)
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree)
    elif (turn % 2 == 1):
        player2.money -= 100
        player1.money += 100
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree)
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree)
def chance3():
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    global chancecard
    chancecard = py.image.load("ChanceCards/chancecardthree.png")
    if (turn % 2 == 0):
        player1.money -= 25
        player2.money += 25
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree)
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree)
    elif (turn % 2 == 1):
        player2.money -= 25
        player1.money += 25
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree)
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree)

def chance4():
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    global chancecard
    chancecard = py.image.load("ChanceCards/chancecardfour.png")
    if (turn % 2 == 0):
        if ((870 < player1.x < 1100) and (520 < player1.y < 590)):
            player1.y -= 210
        if ((380 < player1.x < 450) and (820 < player1.y < 960)):
            player1.x += 210
        if ((310 < player1.x < 380) and (50 < player1.y < 190)):
            player1.x = 170
            player1.y = 225
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree)
    if (turn % 2 == 1):
        if ((870 < player2.x < 1100) and (520 < player2.y < 590)):
            player2.y -= 210
        if ((380 < player2.x < 450) and (820 < player2.y < 960)):
            player2.x += 210
        if ((310 < player2.x < 380) and (50 < player2.y < 190)):
            player2.x = 170
            player2.y = 225
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree)
def chance5():
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    global chancecard
    chancecard = py.image.load("ChanceCards/chancecardfive.png")
    if (turn % 2 == 0):
        player1.money -= 25
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree)
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree)
    elif (turn % 2 == 1):
        player2.money -= 25
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree)
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree)
def chance6():
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    global chancecard
    chancecard = py.image.load("ChanceCards/chancecardsix.png")
    if (turn % 2 == 0):
        player1.money -= 15
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree)
    elif (turn % 2 == 1):
        player2.money -= 15
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree)

def chance7():
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    global chancecard
    chancecard = py.image.load("ChanceCards/chancecardseven.png")
    if (turn % 2 == 0):
        player1.money -= 50
        player2.money += 50
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree)
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree)
    elif (turn % 2 == 1):
        player2.money -= 50
        player1.money += 50
        player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree)
        player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree)

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
        chancecard_scale = py.transform.scale(chancecard, (chancecard.get_width()*0.5, chancecard.get_height()*0.5))
        screen.blit(chancecard_scale, (325, 375))
        
    else:
        chancecounterp1 = 0

def chancecardp2():
    from mnply_board import player2
    from mnply_board import end_turn
    from mnply_board import turn
    global chancecounterp2
    if(((380 < player2.x < 450) and (820 < player2.y < 960)) or ((310 < player2.x < 380) and (50 < player2.y < 190)) or ((870 < player2.x < 1100) and (520 < player2.y < 590))) and (end_turn == 1) and (turn % 2 == 0):
        if chancecounterp2 == 0:
            random.choice(chancelist)()
            chancecounterp2 = 1
        chancecard_scale = py.transform.scale(chancecard, (chancecard.get_width()*0.5, chancecard.get_height()*0.5))
        screen.blit(chancecard_scale, (325, 375))
    else:
        chancecounterp2 = 0


