import pygame as py

py.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), py.RESIZABLE)

class button():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.clicked = False


    def draw(self, win):
        action = False
        py.draw.rect(win, self.color, self.rect)
        posx, posy = py.mouse.get_pos()
        click = py.mouse.get_pressed()
        if (self.x < posx < self.x+100) and (self.y < posy < self.y+30):
            if (click[0] == 1) and (self.clicked == False):
                self.clicked = True
                action = True
            if click[0] == 0:
                self.clicked = False
        return action


font = py.font.Font('freesansbold.ttf', 24)

def propcardsp1():
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    from mnply_board import end_turn
    from mnply_board import button
    from mnply_board import dice_sum
    from mnply_board import medavep1,  medavep2, balavep1, balavep2, oriavep1, oriavep2, veravep1, veravep2, conavep1, conavep2, chaavep1, chaavep2, staavep1, staavep2, viravep1, viravep2, jamavep1, jamavep2, tenavep1, tenavep2, nyavep1, nyavep2, kenavep1, kenavep2, indavep1, indavep2, illavep1, illavep2, atlavep1, atlavep2,venavep1,venavep2,margarp1,margarp2,pacavep1,pacavep2,caravep1,caravep2,penavep1,penavep2,parplap1,parplap2,brdwlkp1,brdwlkp2
    global font
    from mnply_board import propendturn

    #Mediterranean Avenue
    if ((800 < player1.x < 870) and (820 - 60 < player1.y < -60 + 960) and (turn % 2 == 0) and (end_turn == 1)):
        meditave = py.image.load("PropertyCards/Mediterranean_Ave.png")
        screen.blit(meditave, (325, 275))
        global medavep1
        if medavep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 60
                propendturn()
                medavep1 += 0
            screen.blit(buy, buy_rect)
        if medavep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                medavep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    #Baltic Avenue
    elif ((660 <player1.x < 730) and (820 - 60 < player1.y < -60 + 960) and (turn % 2 == 0) and (end_turn == 1)):
        baltic_ave = py.image.load("PropertyCards/Baltic_Ave.png")
        screen.blit(baltic_ave, (325, 375))
        global balavep1
        if balavep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 60
                propendturn()
                balavep1 += 0
            screen.blit(buy, buy_rect)
        if balavep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen) and (balavep1 < 5):
                player1.money -= 20
                propendturn()
                balavep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

        
    #elif ((520 < player1.x < 590) and (820 - 60 < player1.y < -60 + 960) and (turn % 2 == 0) and (end_turn == 1)):
    #   reading_railroad = py.image.load("PropertyCards/Reading_Railroad.png")
    #   screen.blit(reading_railroad, (325, 375))
        
    #Oriental Avenue
    elif ((450 < player1.x < 520) and (820 - 60 < player1.y < -60 + 960) and (turn % 2 == 0) and (end_turn == 1)):
        oriental_ave = py.image.load("PropertyCards/Oriental_Ave.png")
        screen.blit(oriental_ave, (325, 375))
        global oriavep1
        if oriavep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 60
                propendturn()
                oriavep1 += 0
            screen.blit(buy, buy_rect)
        if oriavep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen) and (oriavep1 < 5):
                player1.money -= 20
                propendturn()
                oriavep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((310 < player1.x < 380) and (820 - 60 < player1.y < -60 + 960) and (turn % 2 == 0) and (end_turn == 1)):
        vermont_ave = py.image.load("PropertyCards/Vermont_Ave.png")
        screen.blit(vermont_ave, (325, 375))
        global verave
        if veravep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 60
                propendturn()
                veravep1 += 0
            screen.blit(buy, buy_rect)
        if veravep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen) and (veravep1 < 5):
                player1.money -= 20
                propendturn()
                veravep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((240 < player1.x < 310) and (820 - 60 < player1.y < -60 + 960) and (turn % 2 == 0) and (end_turn == 1)):
        conn_ave = py.image.load("PropertyCards/Connecticut_Ave.png")
        screen.blit(conn_ave, (325, 375))
        global conavep1
        if conavep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 60
                propendturn()
                conavep1 += 0
            screen.blit(buy, buy_rect)
        if conavep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                conavep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((100 < player1.x < 240) and (750 - 60 < player1.y < -60 + 820) and (turn % 2 == 0) and (end_turn == 1)):
        stcharles = py.image.load("PropertyCards/St. Charles Pl.png")
        screen.blit(stcharles, (325, 375))
        global chaavep1
        if chaavep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 140
                propendturn()
                chaavep1 += 0
            screen.blit(buy, buy_rect)
        if chaavep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                chaavep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif (100 < player1.x < 240) and (680 - 60 < player1.y < -60 + 750) and (turn % 2 == 0) and (end_turn == 1):
        elec_comp = py.image.load("PropertyCards/Electric_Company.png")
        screen.blit(elec_comp, (325, 375))
        global eleccompcount
        eleccompcount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if eleccompcount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            screen.blit(buy_text, buy_Rect)
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            screen.blit(ignore_text, ignore_rect)
            if buybutton.draw(screen):
                player1.money -= 150
                eleccompcount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif eleccompcount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 4*dice_sum 
            player2.money += 4*dice_sum
            turn += 1

    elif (100 < player1.x < 240) and (610 - 60 < player1.y < -60 + 680) and (turn % 2 == 0) and (end_turn == 1):
        states_ave = py.image.load("PropertyCards/States_Ave.png")
        screen.blit(states_ave, (325, 375))
        global staavep1
        if staavep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 140
                propendturn()
                staavep1 += 0
            screen.blit(buy, buy_rect)
        if staavep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                staavep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif(100 < player1.x < 240) and (540 - 60 < player1.y < -60 + 610) and (turn % 2 == 0) and (end_turn == 1):
        virginia_ave = py.image.load("PropertyCards/Virginia_Ave.png")
        screen.blit(virginia_ave, (325, 375))
        global viravep1
        if viravep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 160
                propendturn()
                viravep1 += 0
            screen.blit(buy, buy_rect)
        if viravep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                viravep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((100 < player1.x < 240) and (470 - 60 < player1.y < -60 + 540) and (turn % 2 == 0) and (end_turn == 1)):
        penn_railroad = py.image.load("PropertyCards/Pennsylvania_Railroad.png")
        screen.blit(penn_railroad, (325, 375))
        ##p1buttons(160, 50, 60, pennrailp1, viravep2)
        
    elif ((100 < player1.x < 240) and (400 - 60 < player1.y < -60 + 470) and (turn % 2 == 0) and (end_turn == 1)):
        stjames = py.image.load("PropertyCards/St. James Pl.png")
        screen.blit(stjames, (325, 375))
        global jamavep1
        if jamavep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 180
                propendturn()
                jamavep1 += 0
            screen.blit(buy, buy_rect)
        if jamavep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                jamavep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((100 < player1.x < 240) and (260 - 60 < player1.y < -60 + 330) and (turn % 2 == 0) and (end_turn == 1)):
        tenn_ave = py.image.load("PropertyCards/Tennessee_Ave.png")
        screen.blit(tenn_ave, (325, 375))
        global tenavep1
        if tenavep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 180
                propendturn()
                tenavep1 += 0
            screen.blit(buy, buy_rect)
        if tenavep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                tenavep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((100 < player1.x < 240) and (190 - 60 < player1.y < -60 + 260) and (turn % 2 == 0) and (end_turn == 1)):
        ny_ave = py.image.load("PropertyCards/New_York_Ave.png")
        screen.blit(ny_ave, (325, 375))
        global nyavep1
        if nyavep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 200
                propendturn()
                nyavep1 += 0
            screen.blit(buy, buy_rect)
        if nyavep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                nyavep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((240 < player1.x  < 310) and (50 - 60 < player1.y < -60 + 190) and (turn % 2 == 0) and (end_turn == 1)):
        kent_ave = py.image.load("PropertyCards/Kentucky_Ave.png")
        screen.blit(kent_ave, (325, 375))
        global kenavep1
        if kenavep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 220
                propendturn()
                kenavep1 += 0
            screen.blit(buy, buy_rect)
        if kenavep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                kenavep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((380 < player1.x < 450) and (50 - 60 < player1.y < -60 + 190) and (turn % 2 == 0) and (end_turn == 1)):
        indi_ave = py.image.load("PropertyCards/Indiana_Ave.png")
        screen.blit(indi_ave, (325, 375))
        global indavep1
        if indavep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 220
                propendturn()
                indavep1 += 0
            screen.blit(buy, buy_rect)
        if indavep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                indavep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((450 < player1.x < 520) and (50 - 60 < player1.y < -60 + 190) and (turn % 2 == 0) and (end_turn == 1)):
        ill_ave = py.image.load("PropertyCards/Illinois_Ave.png")
        screen.blit(ill_ave, (325, 375))
        global illavep1
        if illavep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 240
                propendturn()
                illavep1 += 0
            screen.blit(buy, buy_rect)
        if illavep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                illavep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((520 < player1.x < 590) and (50 - 60 < player1.y < -60 + 190) and (turn % 2 == 0) and (end_turn == 1)):
        bo_railroad = py.image.load("PropertyCards/BandO_Railroad.png")
        screen.blit(bo_railroad, (325, 375))
        global borailcount
        borailcount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if borailcount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                borailcount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif borailcount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1

    elif ((590 < player1.x < 660) and (50 - 60 < player1.y < -60 + 190) and (turn % 2 == 0) and (end_turn == 1)):
        atlantic_ave = py.image.load("PropertyCards/Atlantic_Avenue.png")
        screen.blit(atlantic_ave, (325, 375))
        global atlavep1
        if atlavep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 260
                propendturn()
                atlavep1 += 0
            screen.blit(buy, buy_rect)
        if atlavep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                atlavep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((660 < player1.x < 730) and (50 - 60 < player1.y < -60 + 190) and (turn % 2 == 0) and (end_turn == 1)):
        ventnor_ave = py.image.load("PropertyCards/Ventnor_Avenue.png")
        screen.blit(ventnor_ave, (325, 375))
        global venavep1
        if venavep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 260
                propendturn()
                venavep1 += 0
            screen.blit(buy, buy_rect)
        if venavep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                venavep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((730 < player1.x < 800) and (50 - 60 < player1.y < -60 + 190) and (turn % 2 == 0) and (end_turn == 1)):
        water_works = py.image.load("PropertyCards/Water_Works.png")
        screen.blit(water_works, (325, 375))
        global wtrwrkavecount
        wtrwrkcount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if wtrwrkcount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                wtrwrkcount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif wtrwrkcount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1

    elif ((800 < player1.x < 870) and (50 - 60 < player1.y < -60 + 190) and (turn % 2 == 0) and (end_turn == 1)):
        marv_gardens = py.image.load("PropertyCards/Marvin_Gardens.png")
        screen.blit(marv_gardens, (325, 375))
        global margarp1
        if margarp1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 300
                propendturn()
                margarp1 += 0
            screen.blit(buy, buy_rect)
        if margarp1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                margarp1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((870 < player1.x < 1010) and (190 - 60 < player1.y < -60 + 260) and (turn % 2 == 0) and (end_turn == 1)):
        pacific_ave = py.image.load("PropertyCards/Pacific_Avenue.png")
        screen.blit(pacific_ave, (325, 375))
        global pacavep1
        if pacavep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 300
                propendturn()
                pacavep1 += 0
            screen.blit(buy, buy_rect)
        if pacavep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                pacavep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((870 < player1.x < 1010) and (260 - 60 < player1.y < -60 + 330) and (turn % 2 == 0) and (end_turn == 1)):
        nc_ave= py.image.load("PropertyCards/North_Carolina.png")
        screen.blit(nc_ave, (325, 375))
        global caravep1
        if caravep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 300
                propendturn()
                caravep1 += 0
            screen.blit(buy, buy_rect)
        if caravep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                caravep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((870 < player1.x < 1010) and (470 - 60 < player1.y < -60 + 540) and (turn % 2 == 0) and (end_turn == 1)):
        short_line = py.image.load("PropertyCards/Short_Line.png")
        screen.blit(short_line, (325, 375))
        global shortlncount
        shortlncount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if shortlncount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                shortlncount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif shortlncount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1

    elif ((870 < player1.x < 1010) and (400 - 60 < player1.y < -60 + 470) and (turn % 2 == 0) and (end_turn == 1)):
        penn_ave= py.image.load("PropertyCards/Pennsylvania_Avenue.png")
        screen.blit(penn_ave, (325, 375))
        global penavep1
        if penavep1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 320
                propendturn()
                penavep1 += 0
            screen.blit(buy, buy_rect)
        if penavep1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                penavep1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((870 < player1.x < 1010) and (610 - 60 < player1.y < -60 + 680) and (turn % 2 == 0) and (end_turn == 1)):
        park_place = py.image.load("PropertyCards/Park_Place.png")
        screen.blit(park_place, (325, 375))
        global parplap1
        if parplap1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 350
                propendturn()
                parplap1 += 0
            screen.blit(buy, buy_rect)
        if parplap1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                parplap1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

    elif ((870 < player1.x < 1010) and (750 - 60 < player1.y < -60 + 820) and (turn % 2 == 0) and (end_turn == 1)):
        boardwalk = py.image.load("PropertyCards/Boardwalk.png")
        screen.blit(boardwalk, (325, 375))
        global brdwlkp1
        if brdwlkp1 == 0:
            buyButton = button(400, 740, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player1.money -= 400
                propendturn()
                brdwlkp1 += 0
            screen.blit(buy, buy_rect)
        if brdwlkp1 >= 0:
            upgradeButton = button(400, 740, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 740, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen):
                player1.money -= 20
                propendturn()
                brdwlkp1 += 1 
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 740, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 740, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        if closeButton.draw(screen):
            propendturn()
        screen.blit(close, close_rect)

def propcardsp2():
    from mnply_board import player2
    from mnply_board import turn
    from mnply_board import end_turn


    class button():
        def __init__(self, x, y, width, height, color):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color
            self.rect = (x,y,width,height)
            self.clicked = False


        def draw(self, win):
            action = False
            py.draw.rect(win, self.color, self.rect)
            posx, posy = py.mouse.get_pos()
            click = py.mouse.get_pressed()
            if (self.x < posx < self.x+100) and (self.y < posy < self.y+30):
                if (click[0] == 1) and (self.clicked == False):
                    self.clicked = True
                    action = True
                if click[0] == 0:
                    self.clicked = False
            return action

    #from mnply_board import #p2buttons

    #Mediterranean Avenue
    if ((800 < player2.x < 870) and (820 - 60 < player2.y < -60 + 960)) and (turn % 2 == 1) and (end_turn == 1):
        mediterraneanAvenue = py.image.load("PropertyCards/Mediterranean_Ave.png")
        screen.blit(mediterraneanAvenue, (300, 400))
        #p2buttons(60, 50, 10, medavep2, medavep1)

    #Baltic Avenue
    if ((660 < player2.x < 730) and (820 - 60 < player2.y < -60 + 960)) and (turn % 2 == 1) and (end_turn == 1):
        balticAvenue = py.image.load("PropertyCards/Baltic_Ave.png")
        screen.blit(balticAvenue, (300, 400))
        #p2buttons(60, 50, 20, balavep2, balavep1)

    #Reading Railroad
    if ((520 < player2.x < 590) and (820 - 60 < player2.y < -60 + 960)) and (turn % 2 == 1) and (end_turn == 1):
        readingRailroad = py.image.load("PropertyCards/Reading_Railroad.png")
        screen.blit(readingRailroad, (300, 400))

    #Oriental Avenue
    if ((450 < player2.x < 520) and (820 - 60 < player2.y < -60 + 960)) and (turn % 2 == 1) and (end_turn == 1):
        orientalAvenue = py.image.load("PropertyCards/Oriental_Ave.png")
        screen.blit(orientalAvenue, (300, 400))
        #p2buttons(100, 50, 30, oriavep2, oriavep1)

    #Vermont Avenue
    if ((310 < player2.x < 380) and (820 - 60 < player2.y < -60 + 960)) and (turn % 2 == 1) and (end_turn == 1):
        vermontAvenue = py.image.load("PropertyCards/Vermont_Ave.png")
        screen.blit(vermontAvenue, (300, 400))
        #p2buttons(100, 50, 30, veravep2, veravep1)

    #Connecticut Avenue
    if ((240 < player2.x < 310) and (820 - 60 < player2.y < -60 + 960)) and (turn % 2 == 1) and (end_turn == 1):
        connecticutAvenue = py.image.load("PropertyCards/Connecticut_Ave.png")
        screen.blit(connecticutAvenue, (300, 400))
        #p2buttons(120, 50, 40, conavep2, conavep1)

    #St. Charles Place
    if ((100 < player2.x < 240) and (750 - 60 < player2.y < -60 + 820)) and (turn % 2 == 1) and (end_turn == 1):
        stCharlesPlace = py.image.load("PropertyCards/St. Charles Pl.png")
        screen.blit(stCharlesPlace, (300, 400))
        #p2buttons(140, 50, 50, chaavep2, chaavep1)

    #Electric Company
    if ((100 < player2.x < 240) and (680 - 60 < player2.y < -60 + 750)) and (turn % 2 == 1) and (end_turn == 1):
        electricCompany = py.image.load("PropertyCards/Electric_Company.png")
        screen.blit(electricCompany, (300, 400))

    #States Avenue
    if ((100 < player2.x < 240) and (610 - 60 < player2.y < -60 + 680)) and (turn % 2 == 1) and (end_turn == 1):
        statesAvenue = py.image.load("PropertyCards/States_Ave.png")
        screen.blit(statesAvenue, (300, 400))
        #p2buttons(140, 50, 50, staavep2, staavep1)

    #Virginia Avenue
    if ((100 < player2.x < 240) and (540 - 60 < player2.y < -60 + 610)) and (turn % 2 == 1) and (end_turn == 1):
        virginiaAvenue = py.image.load("PropertyCards/Virginia_Ave.png")
        screen.blit(virginiaAvenue, (300, 400))
        #p2buttons(160, 50, 60, viravep2, viravep1)

    #Pennsylvania Railroad
    if ((100 < player2.x < 240) and (470 - 60 < player2.y < -60 + 540)) and (turn % 2 == 1) and (end_turn == 1):
        pennsylaniaRailroad = py.image.load("PropertyCards/Pennsylvania_Railroad.png")
        screen.blit(pennsylaniaRailroad, (300, 400))

    #St. James Place
    if ((100 < player2.x < 240) and (400 - 60 < player2.y < -60 + 470)) and (turn % 2 == 1) and (end_turn == 1):
        stJamesPlace = py.image.load("PropertyCards/St. James Pl.png")
        screen.blit(stJamesPlace, (300, 400))
        #p2buttons(180, 50, 70, jamavep2, jamavep1)

    #Tennessee Avenue
    if ((100 < player2.x < 240) and (260 - 60 < player2.y < -60 + 330)) and (turn % 2 == 1) and (end_turn == 1):
        tennesseeAvenue = py.image.load("PropertyCards/Tennessee_Ave.png")
        screen.blit(tennesseeAvenue, (300, 400))
        #p2buttons(180, 50, 70, tenavep2, tenavep1)

    #New York Avenue
    if ((100 < player2.x < 240) and (190 - 60 < player2.y < -60 + 260)) and (turn % 2 == 1) and (end_turn == 1):
        newYorkAvenue = py.image.load("PropertyCards/New_York_Ave.png")
        screen.blit(newYorkAvenue, (300, 400))
        #p2buttons(200, 50, 80, nyavep2, nyavep1)

    #Kentucky Avenue
    if ((240 < player2.x < 310) and (50 - 60 < player2.y < -60 + 190)) and (turn % 2 == 1) and (end_turn == 1):
        kentuckyAvenue = py.image.load("PropertyCards/Kentucky_Ave.png")
        screen.blit(kentuckyAvenue, (300, 400))
        #p2buttons(220, 50, 90, kenavep2, kenavep1)

    #Indiana Avenue
    if ((380 < player2.x < 450) and (50 - 60 < player2.y < -60 + 190)) and (turn % 2 == 1) and (end_turn == 1):
        indianaAvenue = py.image.load("PropertyCards/Indiana_Ave.png")
        screen.blit(indianaAvenue, (300, 400))
        #p2buttons(220, 50, 90, indavep2, indavep1)

    #Illinois Avenue
    if ((450 < player2.x < 520) and (50 - 60 < player2.y < -60 + 190)) and (turn % 2 == 1) and (end_turn == 1):
        illinoisAvenue = py.image.load("PropertyCards/Illinois_Ave.png")
        screen.blit(illinoisAvenue, (300, 400))
        #p2buttons(240, 50, 100, illavep2, illavep1)

    #B. & O. Railroad
    if ((520 < player2.x < 590) and (50 - 60 < player2.y < -60 + 190)) and (turn % 2 == 1) and (end_turn == 1):
        bandoRailroad = py.image.load("PropertyCards/BandO_Railroad.png")
        screen.blit(bandoRailroad, (300, 400))

    #Atlantic Avenue
    if ((590 < player2.x < 660) and (50 - 60 < player2.y < -60 + 190)) and (turn % 2 == 1) and (end_turn == 1):
        atlanticAvenue = py.image.load("PropertyCards/Atlantic_Avenue.png")
        screen.blit(atlanticAvenue, (300, 400))
        #p2buttons(260, 50, 110, atlavep2, atlavep1)

    #Ventnor Avenue
    if ((660 < player2.x < 730) and (50 - 60 < player2.y < -60 + 190)) and (turn % 2 == 1) and (end_turn == 1):
        ventnorAvenue = py.image.load("PropertyCards/Ventnor_Avenue.png")
        screen.blit(ventnorAvenue, (300, 400))
        #p2buttons(260, 50, 110, venavep2, venavep1)

    #Water Works
    if ((730 < player2.x <800) and (50 - 60 < player2.y < -60 + 190)) and (turn % 2 == 1) and (end_turn == 1):
        waterWorks = py.image.load("PropertyCards/Water_Works.png")
        screen.blit(waterWorks, (300, 400))

    #Marvin Gardens
    if ((800 < player2.x < 870) and (50 - 60 < player2.y < -60 + 190)) and (turn % 2 == 1) and (end_turn == 1):
        marvinGardens = py.image.load("PropertyCards/Marvin_Gardens.png")
        screen.blit(marvinGardens, (300, 400))
        #p2buttons(280, 50, 120, margarp2, margarp1)

    #Pacific Avenue
    if ((870 < player2.x < 1010) and (190 - 60 < player2.y < -60 + 260)) and (turn % 2 == 1) and (end_turn == 1):
        pacificAvenue = py.image.load("PropertyCards/Pacific_Avenue.png")
        screen.blit(pacificAvenue, (300, 400))
        #p2buttons(300, 50, 130, pacavep2, pacavep1)

    #North Carolina Avenue
    if ((870 < player2.x < 1010) and (260 - 60 < player2.y < -60 + 330)) and (turn % 2 == 1) and (end_turn == 1):
        northCarolinaAvenue = py.image.load("PropertyCards/North_Carolina.png")
        screen.blit(northCarolinaAvenue, (300, 400))
        #p2buttons(300, 50, 130, caravep2, caravep1)

    #Pennsylvania Avenue
    if ((870 < player2.x < 1010) and (400 - 60 < player2.y < -60 + 470)) and (turn % 2 == 1) and (end_turn == 1):
        pennsylvaniaAvenue = py.image.load("PropertyCards/Pennsylvania_Avenue.png")
        screen.blit(pennsylvaniaAvenue, (300, 400))
        #p2buttons(320, 50, 150, penavep2, penavep1)

    #Short Line
        
    #Park Place
    if ((870 < player2.x < 1010) and (610 - 60 < player2.y < -60 + 680)) and (turn % 2 == 1) and (end_turn == 1):
        parkPlace = py.image.load("PropertyCards/Park_Place.png")
        screen.blit(parkPlace, (300, 400))
        #p2buttons(350, 50, 175, parplap2, parplap1)

    #BoardWalk
    if ((870 < player2.x < 1010) and (680 - 60 < player2.y < -60 + 750)) and (turn % 2 == 1) and (end_turn == 1):
        boardwalk = py.image.load("PropertyCards/Boardwalk.png")
        screen.blit(boardwalk, (300, 400))
        #p2buttons(400, 50, 200, brdwlkp2, brdwlkp1)