from mnply_board import *


def comcardp1():
    if ((800 < player1.x < 870) and (820 < player1.y < 960)) or ((100 < player1.x < 240) and (50 < player1.y < 120)) or ((870 < player1.x < 1010) and (330 < player1.y < 470)):
        comcardp1 = py.image.load("ComCard/comone.png")
        screen.blit(comcardp1, (400, 500))