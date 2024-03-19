import pygame as py

py.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), py.RESIZABLE)

font = py.font.Font('freesansbold.ttf', 24)

def propcards():
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    from mnply_board import end_turn
    from mnply_board import button
    from mnply_board import dice_sum
    global medavep1,  medavep2, balavep1, balavep2, oriavep1, oriavep2, veravep1, veravep2, conavep1, conavep2, chaavep1, chaavep2, staavep1, staavep2, viravep1, viravep2, jamavep1, jamavep2, tenavep1, tenavep2, nyavep1, nyavep2, kenavep1, kenavep2, indavep1, indavep2, illavep1, illavep2, atlavep1, atlavep2,venavep1,venavep2,margarp1,margarp2,pacavep1,pacavep2,caravep1,caravep2,penavep1,penavep2,parplap1,parplap2,brdwlkp1,brdwlkp2, bo_railp1, bo_railp2, shortlinep1, shortlinep2, penn_railp1, penn_railp2, readingrailp1, readingrailp2, elecomp1, elecomp2, watworp1, watworp2 
    from mnply_board import medavep1,  medavep2, balavep1, balavep2, oriavep1, oriavep2, veravep1, veravep2, conavep1, conavep2, chaavep1, chaavep2, staavep1, staavep2, viravep1, viravep2, jamavep1, jamavep2, tenavep1, tenavep2, nyavep1, nyavep2, kenavep1, kenavep2, indavep1, indavep2, illavep1, illavep2, atlavep1, atlavep2,venavep1,venavep2,margarp1,margarp2,pacavep1,pacavep2,caravep1,caravep2,penavep1,penavep2,parplap1,parplap2,brdwlkp1,brdwlkp2, bo_railp1, bo_railp2, shortlinep1, shortlinep2, penn_railp1, penn_railp2, readingrailp1, readingrailp2, elecomp1, elecomp2, watworp1, watworp2
    global font
    from mnply_board import propendturn

    def buytext():
        global font
        buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
        buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
        screen.blit(buy, buy_rect)

    def upgradetext():
        global font
        upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
        upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
        screen.blit(upgrade, upgrade_rect)

    def closebutton():
        global font
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    def rentdeduction():
        global font
        rent_text = font.render("You must pay your rent.", True, (0, 0, 0), (255, 255, 255))
        rent_box = py.draw.rect(screen, (255, 255, 255), (350, 700, 500, 30))
        screen.blit(rent_text, rent_box)

    #Mediterranean Avenue
    if ((800 < player1.x < 870) and (820 - 60 < player1.y < -60 + 960) and (turn % 2 == 0) and (end_turn == 1)):
        meditave = py.image.load("PropertyCards/Mediterranean_Ave.png")
        screen.blit(meditave, (325, 275))
        if medavep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 2
                player2.money += 2
                propendturn()
            rentdeduction()
        else:
            if medavep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= 40
                    propendturn()
                    medavep1 += 1
                buytext()
            if medavep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    medavep1 += 1 
                upgradetext()
            closebutton()

    #Baltic Avenue
    elif ((660 <player1.x < 730) and (820 - 60 < player1.y < -60 + 960) and (turn % 2 == 0) and (end_turn == 1)):
        baltic_ave = py.image.load("PropertyCards/Baltic_Ave.png")
        screen.blit(baltic_ave, (325, 375))
        if balavep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 4
                player2.money += 4
                propendturn()
            rentdeduction()
        else:
            if balavep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= 40
                    propendturn()
                    balavep1 += 1
                buytext()
            if balavep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen) and (balavep1 < 5):
                    player1.money -= 20
                    propendturn()
                    balavep1 += 1 
                upgradetext()
            closebutton()

        
    #elif ((520 < player1.x < 590) and (820 - 60 < player1.y < -60 + 960) and (turn % 2 == 0) and (end_turn == 1)):
    #   reading_railroad = py.image.load("PropertyCards/Reading_Railroad.png")
    #   screen.blit(reading_railroad, (325, 375))
        
    #Oriental Avenue
    elif ((450 < player1.x < 520) and (820 - 60 < player1.y < -60 + 960) and (turn % 2 == 0) and (end_turn == 1)):
        oriental_ave = py.image.load("PropertyCards/Oriental_Ave.png")
        screen.blit(oriental_ave, (325, 375))
        if oriavep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 6
                player2.money += 6
                propendturn()
            rentdeduction()
        else:
            if oriavep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= 80
                    propendturn()
                    oriavep1 += 1
                buytext()
            if oriavep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen) and (oriavep1 < 5):
                    player1.money -= 20
                    propendturn()
                    oriavep1 += 1 
                upgradetext()
            closebutton()
    #Vermont Avenue
    elif ((310 < player1.x < 380) and (820 - 60 < player1.y < -60 + 960) and (turn % 2 == 0) and (end_turn == 1)):
        vermont_ave = py.image.load("PropertyCards/Vermont_Ave.png")
        screen.blit(vermont_ave, (325, 375))
        if veravep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 6
                player2.money += 6
                propendturn()
            rentdeduction()
        else:
            if veravep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 80
                    propendturn()
                    veravep1 += 1
                buytext()
            if veravep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen) and (veravep1 < 5):
                    player1.money -= 20
                    propendturn()
                    veravep1 += 1 
                upgradetext()
            closebutton()
    #Connecticut Avenue
    elif ((240 < player1.x < 310) and (820 - 60 < player1.y < -60 + 960) and (turn % 2 == 0) and (end_turn == 1)):
        conn_ave = py.image.load("PropertyCards/Connecticut_Ave.png")
        screen.blit(conn_ave, (325, 375))
        if conavep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 8
                player2.money += 8
                propendturn()
            rentdeduction()
        else:
            if conavep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= 100
                    propendturn()
                    conavep1 += 1
                buytext()
            if conavep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    conavep1 += 1 
                upgradetext()
            closebutton()
    #St. Charles Place
    elif ((100 < player1.x < 240) and (750 - 60 < player1.y < -60 + 820) and (turn % 2 == 0) and (end_turn == 1)):
        stcharles = py.image.load("PropertyCards/St. Charles Pl.png")
        screen.blit(stcharles, (325, 375))
        if chaavep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 10
                player2.money += 10
                propendturn()
            rentdeduction()
        else:
            if chaavep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= 120
                    propendturn()
                    chaavep1 += 1
                buytext()
            if chaavep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    chaavep1 += 1 
                upgradetext()
            closebutton()
    #Electric Company
    elif (100 < player1.x < 240) and (680 - 60 < player1.y < -60 + 750) and (turn % 2 == 0) and (end_turn == 1):
        elec_comp = py.image.load("PropertyCards/Electric_Company.png")
        screen.blit(elec_comp, (325, 375))
        if elecomp2 != 0:
            if watworp2 != 0:
                player1.money -= dice_sum * 10
                player2.money += dice_sum * 10
                propendturn()
            else:
                player1.money -= dice_sum * 4
                player2.money += dice_sum * 4
                propendturn()
            rentdeduction()
        else:
            if elecomp1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= 150
                    propendturn()
                    elecomp1 += 1
                buytext()
            closebutton()
        
    #States Avenue
    elif (100 < player1.x < 240) and (610 - 60 < player1.y < -60 + 680) and (turn % 2 == 0) and (end_turn == 1):
        states_ave = py.image.load("PropertyCards/States_Ave.png")
        screen.blit(states_ave, (325, 375))
        if staavep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 10
                player2.money += 10
                propendturn()
            rentdeduction()
        else:
            if staavep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= 120
                    propendturn()
                    staavep1 += 1
                buytext()
            if staavep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    staavep1 += 1 
                upgradetext()
            closebutton()
    #Virginia Avenue
    elif(100 < player1.x < 240) and (540 - 60 < player1.y < -60 + 610) and (turn % 2 == 0) and (end_turn == 1):
        virginia_ave = py.image.load("PropertyCards/Virginia_Ave.png")
        screen.blit(virginia_ave, (325, 375))
        if viravep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 12
                player2.money += 12
                propendturn()
            rentdeduction()
        else:
            if viravep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= 140
                    propendturn()
                    viravep1 += 1
                buytext()
            if viravep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    viravep1 += 1 
                upgradetext()
            closebutton()

    #elif ((100 < player1.x < 240) and (470 - 60 < player1.y < -60 + 540) and (turn % 2 == 0) and (end_turn == 1)):
        #penn_railroad = py.image.load("PropertyCards/Pennsylvania_Railroad.png")
        #screen.blit(penn_railroad, (325, 375))
        ##p1buttons(160, 50, 60, pennrailp1, viravep2)
    #St. James Places
    elif ((100 < player1.x < 240) and (400 - 60 < player1.y < -60 + 470) and (turn % 2 == 0) and (end_turn == 1)):
        stjames = py.image.load("PropertyCards/St. James Pl.png")
        screen.blit(stjames, (325, 375))
        if jamavep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 14
                player2.money += 14
                propendturn()
            rentdeduction()
        else:
            if jamavep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 160
                    propendturn()
                    jamavep1 += 1
                buytext()
            if jamavep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    jamavep1 += 1 
                upgradetext()
            closebutton()
    #Tennessee Avenue
    elif ((100 < player1.x < 240) and (260 - 60 < player1.y < -60 + 330) and (turn % 2 == 0) and (end_turn == 1)):
        tenn_ave = py.image.load("PropertyCards/Tennessee_Ave.png")
        screen.blit(tenn_ave, (325, 375))
        if tenavep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 14
                player2.money += 14
                propendturn()
            rentdeduction()
        else:
            if tenavep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 180
                    propendturn()
                    tenavep1 += 1
                buytext()
            if tenavep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    tenavep1 += 1 
                upgradetext()
            closebutton()
    #New York Avenue
    elif ((100 < player1.x < 240) and (190 - 60 < player1.y < -60 + 260) and (turn % 2 == 0) and (end_turn == 1)):
        ny_ave = py.image.load("PropertyCards/New_York_Ave.png")
        screen.blit(ny_ave, (325, 375))
        if nyavep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 16
                player2.money += 16
                propendturn()
            rentdeduction()
        else:
            if nyavep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 200
                    propendturn()
                    nyavep1 += 1
                buytext()
            if nyavep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    nyavep1 += 1 
                upgradetext()
            closebutton()
    #Kentucky Avenue
    elif ((240 < player1.x  < 310) and (50 - 60 < player1.y < -60 + 190) and (turn % 2 == 0) and (end_turn == 1)):
        kent_ave = py.image.load("PropertyCards/Kentucky_Ave.png")
        screen.blit(kent_ave, (325, 375))
        if kenavep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 18
                player2.money += 18
                propendturn()
            rentdeduction()
        else:
            if kenavep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 220
                    propendturn()
                    kenavep1 += 1
                buytext()
            if kenavep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    kenavep1 += 1 
                upgradetext()
            closebutton()
    #Indiana Avenue
    elif ((380 < player1.x < 450) and (50 - 60 < player1.y < -60 + 190) and (turn % 2 == 0) and (end_turn == 1)):
        indi_ave = py.image.load("PropertyCards/Indiana_Ave.png")
        screen.blit(indi_ave, (325, 375))
        if indavep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 18
                player2.money += 18
                propendturn()
            rentdeduction()
        else:
            if indavep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 220
                    propendturn()
                    indavep1 += 1
                buytext()
            if indavep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    indavep1 += 1 
                upgradetext()
            closebutton()
    #Illinois Avenue
    elif ((450 < player1.x < 520) and (50 - 60 < player1.y < -60 + 190) and (turn % 2 == 0) and (end_turn == 1)):
        ill_ave = py.image.load("PropertyCards/Illinois_Ave.png")
        screen.blit(ill_ave, (325, 375))
        if illavep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 20
                player2.money += 20
                propendturn()
            rentdeduction()
        else:
            if illavep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 240
                    propendturn()
                    illavep1 += 1
                buytext()
            if illavep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    illavep1 += 1 
                upgradetext()
            closebutton()
    #B & O Railroad
    elif ((520 < player1.x < 590) and (50 - 60 < player1.y < -60 + 190) and (turn % 2 == 0) and (end_turn == 1)):
        bo_railroad = py.image.load("PropertyCards/BandO_Railroad.png")
        screen.blit(bo_railroad, (325, 375))
        if bo_railp1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 25*player2.rail
                player2.money += 25*player2.rail
                propendturn()
            rentdeduction()
        else:
            if bo_railp1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 260
                    propendturn()
                    player1.rail += 1
                buytext()
            closebutton()
    #Reading Railroad
    elif ((520 < player1.x < 590) and (820 < player1.y < 960) and (turn % 2 == 0) and (end_turn == 1)):
        reading_railroad = py.image.load("PropertyCards/Readin_Railroad.png")
        screen.blit(reading_railroad, (325, 375))
        if readingrailp1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 25*player2.rail
                player2.money += 25*player2.rail
                propendturn()
            rentdeduction()
        else:
            if readingrailp1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 260
                    propendturn()
                    player1.rail += 1
                buytext()
            closebutton()
    #Pennsylvania Railroad
    elif ((100 < player1.x < 240) and (470 < player1.y < 540) and (turn % 2 == 0) and (end_turn == 1)):
        penn_Rail = py.image.load("PropertyCards/Pennsylvania_Railroad.png")
        screen.blit(penn_Rail, (325, 375))
        if penn_railp1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 25*player2.rail
                player2.money += 25*player2.rail
                propendturn()
            rentdeduction()
        else:
            if penn_railp1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 260
                    propendturn()
                    player1.rail += 1
                buytext()
            closebutton()
    #Atlantic Avenue
    elif ((590 < player1.x < 660) and (50 - 60 < player1.y < -60 + 190) and (turn % 2 == 0) and (end_turn == 1)):
        atlantic_ave = py.image.load("PropertyCards/Atlantic_Avenue.png")
        screen.blit(atlantic_ave, (325, 375))
        if atlavep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 22
                player2.money += 22
                propendturn()
            rentdeduction()
        else:
            if atlavep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 260
                    propendturn()
                    atlavep1 += 1
                buytext()
            if atlavep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    atlavep1 += 1 
                upgradetext()
            closebutton()
    #Ventnor Avenue
    elif ((660 < player1.x < 730) and (50 - 60 < player1.y < -60 + 190) and (turn % 2 == 0) and (end_turn == 1)):
        ventnor_ave = py.image.load("PropertyCards/Ventnor_Avenue.png")
        screen.blit(ventnor_ave, (325, 375))
        if venavep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 22
                player2.money += 22
                propendturn()
            rentdeduction()
        else:
            if venavep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 260
                    propendturn()
                    venavep1 += 1
                buytext()
            if venavep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    venavep1 += 1 
                upgradetext()
            closebutton()
    #Water Works
    elif ((730 < player1.x < 800) and (50 - 60 < player1.y < -60 + 190) and (turn % 2 == 0) and (end_turn == 1)):
        water_works = py.image.load("PropertyCards/Water_Works.png")
        screen.blit(water_works, (325, 375))
        if watworp2 != 0:
            if elecomp2 != 0:
                player1.money -= dice_sum * 10
                player2.money += dice_sum * 10
                propendturn()
            else:
                player1.money -= dice_sum * 4
                player2.money += dice_sum * 4
                propendturn()
            rentdeduction()
        else:
            if watworp1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= 150
                    propendturn()
                    watworp1 += 1
                buytext()
            closebutton()
    #Marvin Gardens
    elif ((800 < player1.x < 870) and (50 - 60 < player1.y < -60 + 190) and (turn % 2 == 0) and (end_turn == 1)):
        marv_gardens = py.image.load("PropertyCards/Marvin_Gardens.png")
        screen.blit(marv_gardens, (325, 375))
        if margarp2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 24
                player2.money += 24
                propendturn()
            rentdeduction()
        else:
            if margarp1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 300
                    propendturn()
                    margarp1 += 1
                buytext()
            if margarp1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    margarp1 += 1 
                upgradetext()
            closebutton()
    #Pacific Avenue
    elif ((870 < player1.x < 1010) and (190 - 60 < player1.y < -60 + 260) and (turn % 2 == 0) and (end_turn == 1)):
        pacific_ave = py.image.load("PropertyCards/Pacific_Avenue.png")
        screen.blit(pacific_ave, (325, 375))
        if pacavep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 26
                player2.money += 26
                propendturn()
            rentdeduction()
        else:
            if pacavep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 300
                    propendturn()
                    pacavep1 += 1
                buytext()
            if pacavep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    pacavep1 += 1 
                upgradetext()
            closebutton()
    #North Carolina Avenue
    elif ((870 < player1.x < 1010) and (260 - 60 < player1.y < -60 + 330) and (turn % 2 == 0) and (end_turn == 1)):
        nc_ave= py.image.load("PropertyCards/North_Carolina.png")
        screen.blit(nc_ave, (325, 375))
        if caravep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 26
                player2.money += 26
                propendturn()
            rentdeduction()
        else:
            if caravep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 300
                    propendturn()
                    caravep1 += 1
                buytext()
            if caravep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    caravep1 += 1 
                upgradetext()
            closebutton()
    #Short Line
    elif ((870 < player1.x < 1010) and (470 - 60 < player1.y < -60 + 540) and (turn % 2 == 0) and (end_turn == 1)):
        short_line = py.image.load("PropertyCards/Short_Line.png")
        screen.blit(short_line, (325, 375))
        if shortlinep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 25*player2.rail
                player2.money += 25*player2.rail
                propendturn()
            rentdeduction()
        else:
            if shortlinep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 260
                    propendturn()
                    player1.rail += 1
                buytext()
            closebutton()
    #Pennsylvania Avenue
    elif ((870 < player1.x < 1010) and (400 - 60 < player1.y < -60 + 470) and (turn % 2 == 0) and (end_turn == 1)):
        penn_ave= py.image.load("PropertyCards/Pennsylvania_Avenue.png")
        screen.blit(penn_ave, (325, 375))
        if penavep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 28
                player2.money += 28
                propendturn()
            rentdeduction()
        else:
            if penavep1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 320
                    propendturn()
                    penavep1 += 1
                buytext()
            if penavep1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    penavep1 += 1 
                upgradetext()
            closebutton()
    #Park Place
    elif ((870 < player1.x < 1010) and (610 - 60 < player1.y < -60 + 680) and (turn % 2 == 0) and (end_turn == 1)):
        park_place = py.image.load("PropertyCards/Park_Place.png")
        screen.blit(park_place, (325, 375))
        if parplap2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 35
                player2.money += 35
                propendturn()
            rentdeduction()
        else:
            if parplap1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 350
                    propendturn()
                    parplap1 += 1
                buytext()
            if parplap1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    parplap1 += 1 
                upgradetext()
            closebutton()
    #Boardwalk
    elif ((870 < player1.x < 1010) and (750 - 60 < player1.y < -60 + 820) and (turn % 2 == 0) and (end_turn == 1)):
        boardwalk = py.image.load("PropertyCards/Boardwalk.png")
        screen.blit(boardwalk, (325, 375))
        if brdwlkp2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player1.money -= 50
                player2.money += 50
                propendturn()
            rentdeduction()
        else:
            if brdwlkp1 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player1.money -= -20 + 400
                    propendturn()
                    brdwlkp1 += 1
                buytext()
            if brdwlkp1 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player1.money -= 20
                    propendturn()
                    brdwlkp1 += 1 
                upgradetext()
            closebutton()


#PLAYER 2-------------------------------------------------------------------------------------------------------------------------
    #Mediterranean Avenue
    if ((800 < player2.x < 870) and (820 - 60 < player2.y < -60 + 960)) and (turn % 2 == 1) and (end_turn == 1):
        mediterraneanAvenue = py.image.load("PropertyCards/Mediterranean_Ave.png")
        screen.blit(mediterraneanAvenue, (300, 400))
        if medavep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 2
                player1.money += 2
                propendturn()
            rentdeduction()
        else:
            if medavep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= 40
                    propendturn()
                    medavep2 += 1
                buytext()
            if medavep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    medavep2 += 1 
                upgradetext()
            closebutton()

    #Baltic Avenue
    if ((660 < player2.x < 730) and (820 - 60 < player2.y < -60 + 960)) and (turn % 2 == 1) and (end_turn == 1):
        balticAvenue = py.image.load("PropertyCards/Baltic_Ave.png")
        screen.blit(balticAvenue, (300, 400))
        if balavep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 4
                player1.money += 4
                propendturn()
            rentdeduction()
        else:
            if balavep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= 40
                    propendturn()
                    balavep2 += 1
                buytext()
            if balavep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen) and (balavep2 < 5):
                    player2.money -= 20
                    propendturn()
                    balavep2 += 1 
                upgradetext()
            closebutton()

    #Reading Railroad
    if ((520 < player2.x < 590) and (820 - 60 < player2.y < -60 + 960)) and (turn % 2 == 1) and (end_turn == 1):
        readingRailroad = py.image.load("PropertyCards/Reading_Railroad.png")
        screen.blit(readingRailroad, (300, 400))
        if readingrailp2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 25*player1.rail
                player1.money += 25*player1.rail
                propendturn()
            rentdeduction()
        else:
            if readingrailp2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 260
                    propendturn()
                    player2.rail += 1
                buytext()
            closebutton()
    #Oriental Avenue
    if ((450 < player2.x < 520) and (820 - 60 < player2.y < -60 + 960)) and (turn % 2 == 1) and (end_turn == 1):
        orientalAvenue = py.image.load("PropertyCards/Oriental_Ave.png")
        screen.blit(orientalAvenue, (300, 400))
        if oriavep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 6
                player1.money += 6
                propendturn()
            rentdeduction()
        else:
            if oriavep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= 80
                    propendturn()
                    oriavep2 += 1
                buytext()
            if oriavep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen) and (oriavep1 < 5):
                    player2.money -= 20
                    propendturn()
                    oriavep2 += 1 
                upgradetext()
            closebutton()

    #Vermont Avenue
    if ((310 < player2.x < 380) and (820 - 60 < player2.y < -60 + 960)) and (turn % 2 == 1) and (end_turn == 1):
        vermontAvenue = py.image.load("PropertyCards/Vermont_Ave.png")
        screen.blit(vermontAvenue, (300, 400))
        if veravep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 8
                player1.money += 8
                propendturn()
            rentdeduction()
        else:
            if veravep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= 100
                    propendturn()
                    veravep2 += 1
                buytext()
            if veravep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    veravep2 += 1 
                upgradetext()
            closebutton()

    #Connecticut Avenue
    if ((240 < player2.x < 310) and (820 - 60 < player2.y < -60 + 960)) and (turn % 2 == 1) and (end_turn == 1):
        connecticutAvenue = py.image.load("PropertyCards/Connecticut_Ave.png")
        screen.blit(connecticutAvenue, (300, 400))
        if conavep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 8
                player1.money += 8
                propendturn()
            rentdeduction()
        else:
            if conavep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= 100
                    propendturn()
                    conavep2 += 1
                buytext()
            if conavep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    conavep2 += 1 
                upgradetext()
            closebutton()

    #St. Charles Place
    if ((100 < player2.x < 240) and (750 - 60 < player2.y < -60 + 820)) and (turn % 2 == 1) and (end_turn == 1):
        stCharlesPlace = py.image.load("PropertyCards/St. Charles Pl.png")
        screen.blit(stCharlesPlace, (300, 400))
        if chaavep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 10
                player1.money += 10
                propendturn()
            rentdeduction()
        else:
            if chaavep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= 120
                    propendturn()
                    chaavep2 += 1
                buytext()
            if chaavep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    chaavep2 += 1 
                upgradetext()
            closebutton()

    #Electric Company
    if ((100 < player2.x < 240) and (680 - 60 < player2.y < -60 + 750)) and (turn % 2 == 1) and (end_turn == 1):
        electricCompany = py.image.load("PropertyCards/Electric_Company.png")
        screen.blit(electricCompany, (300, 400))
        if elecomp1 != 0:
            if watworp1 != 0:
                player2.money -= dice_sum * 10
                player1.money += dice_sum * 10
                propendturn()
            else:
                player2.money -= dice_sum * 4
                player1.money += dice_sum * 4
                propendturn()
            rentdeduction()
        else:
            if elecomp2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= 150
                    propendturn()
                    elecomp2 += 1
                buytext()
            closebutton()

    #States Avenue
    if ((100 < player2.x < 240) and (610 - 60 < player2.y < -60 + 680)) and (turn % 2 == 1) and (end_turn == 1):
        statesAvenue = py.image.load("PropertyCards/States_Ave.png")
        screen.blit(statesAvenue, (300, 400))
        if staavep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 10
                player1.money += 10
                propendturn()
            rentdeduction()
        else:
            if staavep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= 120
                    propendturn()
                    staavep2 += 1
                buytext()
            if staavep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    staavep2 += 1 
                upgradetext()
            closebutton()

    #Virginia Avenue
    if ((100 < player2.x < 240) and (540 - 60 < player2.y < -60 + 610)) and (turn % 2 == 1) and (end_turn == 1):
        virginiaAvenue = py.image.load("PropertyCards/Virginia_Ave.png")
        screen.blit(virginiaAvenue, (300, 400))
        if viravep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 12
                player1.money += 12
                propendturn()
            rentdeduction()
        else:
            if viravep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= 140
                    propendturn()
                    viravep2 += 1
                buytext()
            if viravep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    viravep2 += 1 
                upgradetext()
            closebutton()

    #Pennsylvania Railroad
    if ((100 < player2.x < 240) and (470 - 60 < player2.y < -60 + 540)) and (turn % 2 == 1) and (end_turn == 1):
        pennsylaniaRailroad = py.image.load("PropertyCards/Pennsylvania_Railroad.png")
        screen.blit(pennsylaniaRailroad, (300, 400))
        if penn_railp2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 25*player1.rail
                player1.money += 25*player1.rail
                propendturn()
            rentdeduction()
        else:
            if penn_railp2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 260
                    propendturn()
                    player2.rail += 1
                buytext()
            closebutton()
    #St. James Place
    if ((100 < player2.x < 240) and (400 - 60 < player2.y < -60 + 470)) and (turn % 2 == 1) and (end_turn == 1):
        stJamesPlace = py.image.load("PropertyCards/St. James Pl.png")
        screen.blit(stJamesPlace, (300, 400))
        if jamavep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 14
                player1.money += 14
                propendturn()
            rentdeduction()
        else:
            if jamavep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 160
                    propendturn()
                    jamavep2 += 1
                buytext()
            if jamavep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    jamavep2 += 1 
                upgradetext()
            closebutton()

    #Tennessee Avenue
    if ((100 < player2.x < 240) and (260 - 60 < player2.y < -60 + 330)) and (turn % 2 == 1) and (end_turn == 1):
        tennesseeAvenue = py.image.load("PropertyCards/Tennessee_Ave.png")
        screen.blit(tennesseeAvenue, (300, 400))
        if tenavep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 14
                player1.money += 14
                propendturn()
            rentdeduction()
        else:
            if tenavep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 180
                    propendturn()
                    tenavep2 += 1
                buytext()
            if tenavep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    tenavep2 += 1 
                upgradetext()
            closebutton()

    #New York Avenue
    if ((100 < player2.x < 240) and (190 - 60 < player2.y < -60 + 260)) and (turn % 2 == 1) and (end_turn == 1):
        newYorkAvenue = py.image.load("PropertyCards/New_York_Ave.png")
        screen.blit(newYorkAvenue, (300, 400))
        if nyavep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 16
                player1.money += 16
                propendturn()
            rentdeduction()
        else:
            if nyavep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 200
                    propendturn()
                    nyavep2 += 1
                buytext()
            if nyavep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    nyavep2 += 1 
                upgradetext()
            closebutton()

    #Kentucky Avenue
    if ((240 < player2.x < 310) and (50 - 60 < player2.y < -60 + 190)) and (turn % 2 == 1) and (end_turn == 1):
        kentuckyAvenue = py.image.load("PropertyCards/Kentucky_Ave.png")
        screen.blit(kentuckyAvenue, (300, 400))
        if kenavep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 18
                player1.money += 18
                propendturn()
            rentdeduction()
        else:
            if kenavep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 220
                    propendturn()
                    kenavep2 += 1
                buytext()
            if kenavep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    kenavep2 += 1 
                upgradetext()
            closebutton()

    #Indiana Avenue
    if ((380 < player2.x < 450) and (50 - 60 < player2.y < -60 + 190)) and (turn % 2 == 1) and (end_turn == 1):
        indianaAvenue = py.image.load("PropertyCards/Indiana_Ave.png")
        screen.blit(indianaAvenue, (300, 400))
        if indavep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 18
                player1.money += 18
                propendturn()
            rentdeduction()
        else:
            if indavep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 220
                    propendturn()
                    indavep2 += 1
                buytext()
            if indavep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    indavep2 += 1 
                upgradetext()
            closebutton()

    #Illinois Avenue
    if ((450 < player2.x < 520) and (50 - 60 < player2.y < -60 + 190)) and (turn % 2 == 1) and (end_turn == 1):
        illinoisAvenue = py.image.load("PropertyCards/Illinois_Ave.png")
        screen.blit(illinoisAvenue, (300, 400))
        if illavep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 20
                player1.money += 20
                propendturn()
            rentdeduction()
        else:
            if illavep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 240
                    propendturn()
                    illavep2 += 1
                buytext()
            if illavep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    illavep2 += 1 
                upgradetext()
            closebutton()

    #B. & O. Railroad
    if ((520 < player2.x < 590) and (50 - 60 < player2.y < -60 + 190)) and (turn % 2 == 1) and (end_turn == 1):
        bandoRailroad = py.image.load("PropertyCards/BandO_Railroad.png")
        screen.blit(bandoRailroad, (300, 400))
        if bo_railp2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 25*player1.rail
                player1.money += 25*player1.rail
                propendturn()
            rentdeduction()
        else:
            if bo_railp2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 260
                    propendturn()
                    player2.rail += 1
                buytext()
            closebutton()

    #Atlantic Avenue
    if ((590 < player2.x < 660) and (50 - 60 < player2.y < -60 + 190)) and (turn % 2 == 1) and (end_turn == 1):
        atlanticAvenue = py.image.load("PropertyCards/Atlantic_Avenue.png")
        screen.blit(atlanticAvenue, (300, 400))
        if atlavep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 22
                player1.money += 22
                propendturn()
            rentdeduction()
        else:
            if atlavep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 260
                    propendturn()
                    atlavep2 += 1
                buytext()
            if atlavep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    atlavep2 += 1 
                upgradetext()
            closebutton()

    #Ventnor Avenue
    if ((660 < player2.x < 730) and (50 - 60 < player2.y < -60 + 190)) and (turn % 2 == 1) and (end_turn == 1):
        ventnorAvenue = py.image.load("PropertyCards/Ventnor_Avenue.png")
        screen.blit(ventnorAvenue, (300, 400))
        if venavep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 22
                player1.money += 22
                propendturn()
            rentdeduction()
        else:
            if venavep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 260
                    propendturn()
                    venavep2 += 1
                buytext()
            if venavep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    venavep2 += 1 
                upgradetext()
            closebutton()

    #Water Works
    if ((730 < player2.x <800) and (50 - 60 < player2.y < -60 + 190)) and (turn % 2 == 1) and (end_turn == 1):
        waterWorks = py.image.load("PropertyCards/Water_Works.png")
        screen.blit(waterWorks, (300, 400))
        if watworp1 != 0:
            if elecomp1 != 0:
                player2.money -= dice_sum * 10
                player1.money += dice_sum * 10
                propendturn()
            else:
                player2.money -= dice_sum * 4
                player1.money += dice_sum * 4
                propendturn()
            rentdeduction()
        else:
            if watworp2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= 150
                    propendturn()
                    watworp2 += 1
                buytext()
            closebutton()

    #Marvin Gardens
    if ((800 < player2.x < 870) and (50 - 60 < player2.y < -60 + 190)) and (turn % 2 == 1) and (end_turn == 1):
        marvinGardens = py.image.load("PropertyCards/Marvin_Gardens.png")
        screen.blit(marvinGardens, (300, 400))
        if margarp1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 24
                player1.money += 24
                propendturn()
            rentdeduction()
        else:
            if margarp2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 300
                    propendturn()
                    margarp2 += 1
                buytext()
            if margarp2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    margarp2 += 1 
                upgradetext()
            closebutton()

    #Pacific Avenue
    if ((870 < player2.x < 1010) and (190 - 60 < player2.y < -60 + 260)) and (turn % 2 == 1) and (end_turn == 1):
        pacificAvenue = py.image.load("PropertyCards/Pacific_Avenue.png")
        screen.blit(pacificAvenue, (300, 400))
        if pacavep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 26
                player1.money += 26
                propendturn()
            rentdeduction()
        else:
            if pacavep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 300
                    propendturn()
                    pacavep2 += 1
                buytext()
            if pacavep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    pacavep2 += 1 
                upgradetext()
            closebutton()

    #North Carolina Avenue
    if ((870 < player2.x < 1010) and (260 - 60 < player2.y < -60 + 330)) and (turn % 2 == 1) and (end_turn == 1):
        northCarolinaAvenue = py.image.load("PropertyCards/North_Carolina.png")
        screen.blit(northCarolinaAvenue, (300, 400))
        if caravep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 26
                player1.money += 26
                propendturn()
            rentdeduction()
        else:
            if caravep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 300
                    propendturn()
                    caravep2 += 1
                buytext()
            if caravep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    caravep2 += 1 
                upgradetext()
            closebutton()

    #Pennsylvania Avenue
    if ((870 < player2.x < 1010) and (400 - 60 < player2.y < -60 + 470)) and (turn % 2 == 1) and (end_turn == 1):
        pennsylvaniaAvenue = py.image.load("PropertyCards/Pennsylvania_Avenue.png")
        screen.blit(pennsylvaniaAvenue, (300, 400))
        if penavep1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 28
                player1.money += 28
                propendturn()
            rentdeduction()
        else:
            if penavep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 320
                    propendturn()
                    penavep2 += 1
                buytext()
            if penavep2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    penavep2 += 1 
                upgradetext()
            closebutton()

    #Short Line
    elif ((870 < player2.x < 1010) and (470 - 60 < player2.y < -60 + 540) and (turn % 2 == 1) and (end_turn == 1)):
        short_line = py.image.load("PropertyCards/Short_Line.png")
        screen.blit(short_line, (325, 375))
        if shortlinep2 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 25*player1.rail
                player1.money += 25*player1.rail
                propendturn()
            rentdeduction()
        else:
            if shortlinep2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 260
                    propendturn()
                    player2.rail += 1
                buytext()
            closebutton()
    #Park Place
    if ((870 < player2.x < 1010) and (610 - 60 < player2.y < -60 + 680)) and (turn % 2 == 1) and (end_turn == 1):
        parkPlace = py.image.load("PropertyCards/Park_Place.png")
        screen.blit(parkPlace, (300, 400))
        if parplap1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 35
                player1.money += 35
                propendturn()
            rentdeduction()
        else:
            if parplap2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 350
                    propendturn()
                    parplap2 += 1
                buytext()
            if parplap2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    parplap2 += 1 
                upgradetext()
            closebutton()

    #BoardWalk
    if ((870 < player2.x < 1010) and (680 - 60 < player2.y < -60 + 750)) and (turn % 2 == 1) and (end_turn == 1):
        boardwalk = py.image.load("PropertyCards/Boardwalk.png")
        screen.blit(boardwalk, (300, 400))
        if brdwlkp1 != 0:
            rent_collect = button(510, 740, 100, 30, (255, 0 , 0))
            if rent_collect.draw(screen):
                player2.money -= 50
                player1.money += 50
                propendturn()
            rentdeduction()
        else:
            if brdwlkp2 == 0:
                buyButton = button(400, 740, 100, 30, (0, 255, 0))
                if buyButton.draw(screen):
                    player2.money -= -20 + 400
                    propendturn()
                    brdwlkp2 += 1
                buytext()
            if brdwlkp2 >= 0:
                upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
                if upgradeButton.draw(screen):
                    player2.money -= 20
                    propendturn()
                    brdwlkp2 += 1 
                upgradetext()
            closebutton()