from mnply_board import *
player()
def chancecard():
    if(((380 < player1.x < 450) and (820 < player1.y < 960)) or ((310 < player1.x < 380) and (50 < player1.y < 190)) or ((870 < player1.x < 1100) and (520 < player1.y < 590))):
        chance_test = py.image.load("chancecard")
        screen.blit(chance_test, 100,100)

py.quit()