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

def propcardsp1():
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    from mnply_board import end_turn
    from mnply_board import button
    from mnply_board import dice_sum
    if ((800 < player1.x < 870) and (820 < player1.y < 960) and (turn % 2 == 0) and (end_turn == 1)):
        med_ave = py.image.load("PropertyCards/Mediterranean_Ave.png")
        screen.blit(med_ave, (325, 375))
        global medavecount
        medavecount = 1 
        global font
        font = py.font.Font('freesansbold.ttf', 24)
        if medavecount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                medavecount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif medavecount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1
    elif ((660 <player1.x < 730) and (820 < player1.y < 960) and (turn % 2 == 0) and (end_turn == 1)):
        baltic_ave = py.image.load("PropertyCards/Baltic_Ave.png")
        screen.blit(baltic_ave, (325, 375))
        global balticavecount
        #global font 
        font = py.font.Font('freesansbold.ttf', 24)
        balticavecount = 1
        if balticavecount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                medavecount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif balticavecount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 4 
            player2.money += 4
            turn += 1
        #elif ((590 < player1.x < 660) and (820 < player1.y < 960)):
            #font = py.font.Font('freesansbold.ttf', 32)
            #incometaxtext = font.render("Income Tax!", True, (0, 0, 0), (215, 215, 215))
            #tax_Rect = py.draw.rect(screen, (215, 215, 215), (1050, 330, 140, 140))
            #player1.money -= 200
            #player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree)
            #player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree)

    elif ((520 < player1.x < 590) and (820 < player1.y < 960) and (turn % 2 == 0) and (end_turn == 1)):
        reading_railroad = py.image.load("PropertyCards/Reading_Railroad.png")
        screen.blit(reading_railroad, (325, 375))
        global readingrailroadcount
        readingrailroadcount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if readingrailroadcount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            screen.blit(buy_text, buy_Rect)
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            screen.blit(ignore_text, ignore_rect)
            if buybutton.draw(screen):
                player1.money -= 200
                readingrailroadcount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif readingrailroadcount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 25 
            player2.money += 25
            turn += 1
    elif ((450 < player1.x < 520) and (820 < player1.y < 960) and (turn % 2 == 0) and (end_turn == 1)):
        oriental_ave = py.image.load("PropertyCards/Oriental_Ave.png")
        screen.blit(oriental_ave, (325, 375))
        global orientalavecount
        orientalavecount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if orientalavecount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            screen.blit(buy_text, buy_Rect)
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            screen.blit(ignore_text, ignore_rect)
            if buybutton.draw(screen):
                player1.money -= 200
                orientalavecount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif orientalavecount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 25 
            player2.money += 25
            turn += 1
    elif ((310 < player1.x < 380) and (820 < player1.y < 960) and (turn % 2 == 0) and (end_turn == 1)):
        vermont_ave = py.image.load("PropertyCards/Vermont_Ave.png")
        screen.blit(vermont_ave, (325, 375))
        global vermontavecount
        vermontavecount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if vermontavecount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            screen.blit(buy_text, buy_Rect)
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            screen.blit(ignore_text, ignore_rect)
            if buybutton.draw(screen):
                player1.money -= 100
                vermontavecount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif vermontavecount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 6 
            player2.money += 6
            turn += 1
    elif ((240 < player1.x < 310) and (820 < player1.y < 960) and (turn % 2 == 0) and (end_turn == 1)):
        conn_ave = py.image.load("PropertyCards/Connecticut_Ave.png")
        screen.blit(conn_ave, (325, 375))
        global connavecount
        connavecount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if connavecount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            screen.blit(buy_text, buy_Rect)
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            screen.blit(ignore_text, ignore_rect)
            if buybutton.draw(screen):
                player1.money -= 120
                connavecount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif connavecount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 8 
            player2.money += 8
            turn += 1
    elif ((100 < player1.x < 240) and (750 < player1.y < 820) and (turn % 2 == 0) and (end_turn == 1)):
        stcharles = py.image.load("PropertyCards/St. Charles Pl.png")
        screen.blit(stcharles, (325, 375))
        global stcharlescount
        stcharlescount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if stcharlescount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            screen.blit(buy_text, buy_Rect)
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            screen.blit(ignore_text, ignore_rect)
            if buybutton.draw(screen):
                player1.money -= 140
                stcharlescount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif stcharlescount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 10 
            player2.money += 10
            turn += 1
    elif (100 < player1.x < 240) and (680 < player1.y < 750) and (turn % 2 == 0) and (end_turn == 1):
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
    elif (100 < player1.x < 240) and (610 < player1.y < 680) and (turn % 2 == 0) and (end_turn == 1):
        states_ave = py.image.load("PropertyCards/States_Ave.png")
        screen.blit(states_ave, (325, 375))
        global statesavecount
        statesavecount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if statesavecount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            screen.blit(buy_text, buy_Rect)
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            screen.blit(ignore_text, ignore_rect)
            if buybutton.draw(screen):
                player1.money -= 140
                statesavecount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif statesavecount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 10 
            player2.money += 10
            turn += 1
    elif(100 < player1.x < 240) and (540 < player1.y < 610) and (turn % 2 == 0) and (end_turn == 1):
        virginia_ave = py.image.load("PropertyCards/Virginia_Ave.png")
        screen.blit(virginia_ave, (325, 375))
        global virginiaavecount
        virginiaavecount = 1 
        font = py.font.Font('freesansbold.ttf', 24)
        if virginiaavecount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 160
                virginiaavecount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif virginiaavecount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1
    elif ((100 < player1.x < 240) and (470 < player1.y < 540) and (turn % 2 == 0) and (end_turn == 1)):
        penn_railroad = py.image.load("PropertyCards/Pennsylvania_Railroad.png")
        screen.blit(penn_railroad, (325, 375))
        global pennrailcount
        pennrailcount = 1 
        font = py.font.Font('freesansbold.ttf', 24)
        if pennrailcount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                pennrailcount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif pennrailcount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1
    elif ((100 < player1.x < 240) and (400 < player1.y < 470) and (turn % 2 == 0) and (end_turn == 1)):
        stjames = py.image.load("PropertyCards/St. James Pl.png")
        screen.blit(stjames, (325, 375))
        global stjamescount
        stjamescount = 1 
        font = py.font.Font('freesansbold.ttf', 24)
        if stjamescount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                pennrailcount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif stjamescount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1
    elif ((100 < player1.x < 240) and (260 < player1.y < 330) and (turn % 2 == 0) and (end_turn == 1)):
        tenn_ave = py.image.load("PropertyCards/Tennessee_Ave.png")
        screen.blit(tenn_ave, (325, 375))
        global tennavecount
        tennavecount = 1 
        font = py.font.Font('freesansbold.ttf', 24)
        if tennavecount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                tennavecount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif tennavecount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1
    elif ((100 < player1.x < 240) and (190 < player1.y < 260) and (turn % 2 == 0) and (end_turn == 1)):
        ny_ave = py.image.load("PropertyCards/New_York_Ave.png")
        screen.blit(ny_ave, (325, 375))
        global nyavecount
        nyavecount = 1 
        font = py.font.Font('freesansbold.ttf', 24)
        if nyavecount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                nyavecount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif nyavecount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1
    elif ((240 < player1.x  < 310) and (50 < player1.y < 190) and (turn % 2 == 0) and (end_turn == 1)):
        kent_ave = py.image.load("PropertyCards/Kentucky_Ave.png")
        screen.blit(kent_ave, (325, 375))
        global kentavecount
        kentavecount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if kentavecount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                kentavecount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif kentavecount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1
    elif ((380 < player1.x < 450) and (50 < player1.y < 190) and (turn % 2 == 0) and (end_turn == 1)):
        indi_ave = py.image.load("PropertyCards/Indiana_Ave.png")
        screen.blit(indi_ave, (325, 375))
        global indiavecount
        indiavecount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if indiavecount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                indiavecount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif indiavecount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1
    elif ((450 < player1.x < 520) and (50 < player1.y < 190) and (turn % 2 == 0) and (end_turn == 1)):
        ill_ave = py.image.load("PropertyCards/Illinois_Ave.png")
        screen.blit(ill_ave, (325, 375))
        global illavecount
        illavecount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if illavecount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                illavecount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif illavecount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1
    elif ((520 < player1.x < 590) and (50 < player1.y < 190) and (turn % 2 == 0) and (end_turn == 1)):
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
    elif ((590 < player1.x < 660) and (50 < player1.y < 190) and (turn % 2 == 0) and (end_turn == 1)):
        atlantic_ave = py.image.load("PropertyCards/Atlantic_Avenue.png")
        screen.blit(atlantic_ave, (325, 375))
        global atlavecount
        atlavecount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if atlavecount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                atlavecount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif atlavecount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1
    elif ((660 < player1.x < 730) and (50 < player1.y < 190) and (turn % 2 == 0) and (end_turn == 1)):
        ventnor_ave = py.image.load("PropertyCards/Ventnor_Avenue.png")
        screen.blit(ventnor_ave, (325, 375))
        global ventavecount
        ventavecount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if ventavecount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                ventavecount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif ventavecount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1
    elif ((730 < player1.x < 800) and (50 < player1.y < 190) and (turn % 2 == 0) and (end_turn == 1)):
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
    elif ((800 < player1.x < 870) and (50 < player1.y < 190) and (turn % 2 == 0) and (end_turn == 1)):
        marv_gardens = py.image.load("PropertyCards/Marvin_Gardens.png")
        screen.blit(marv_gardens, (325, 375))
        global marvgardcount
        marvgardcount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if marvgardcount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                marvgardcount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif marvgardcount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1
    elif ((870 < player1.x < 1010) and (190 < player1.y < 260) and (turn % 2 == 0) and (end_turn == 1)):
        pacific_ave = py.image.load("PropertyCards/Pacific_Avenue.png")
        screen.blit(pacific_ave, (325, 375))
        global pacavecount
        pacavecount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if pacavecount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                pacavecount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif pacavecount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1
    elif ((870 < player1.x < 1010) and (260 < player1.y < 330) and (turn % 2 == 0) and (end_turn == 1)):
        nc_ave= py.image.load("PropertyCards/North_Carolina.png")
        screen.blit(nc_ave, (325, 375))
        global nccount
        nccount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if nccount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                nccount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif nccount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1
    elif ((870 < player1.x < 1010) and (400 < player1.y < 470) and (turn % 2 == 0) and (end_turn == 1)):
        penn_ave = py.image.load("PropertyCards/Pennsylvania_Avenue.png")
        screen.blit(penn_ave, (325, 375))
        global pennavecount
        pennavecount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if pennavecount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                pennavecount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif pennavecount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1
    elif ((870 < player1.x < 1010) and (470 < player1.y < 540) and (turn % 2 == 0) and (end_turn == 1)):
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
    elif ((870 < player1.x < 1010) and (610 < player1.y < 680) and (turn % 2 == 0) and (end_turn == 1)):
        park_place = py.image.load("PropertyCards/Park_Place.png")
        screen.blit(park_place, (325, 375))
        global parkpcount
        parkpcount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if parkpcount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                parkpcount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif parkpcount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1
    elif ((870 < player1.x < 1010) and (750 < player1.y < 820) and (turn % 2 == 0) and (end_turn == 1)):
        boardwalk = py.image.load("PropertyCards/Boardwalk.png")
        screen.blit(boardwalk, (325, 375))
        global brdwlkcount
        brdwlkcount = 1
        font = py.font.Font('freesansbold.ttf', 24)
        if brdwlkcount == 1:
            buy_text = font.render("Buy", True, (0, 0, 0), (215, 215, 215))
            buy_Rect = py.draw.rect(screen, (215, 215, 215), (450, 785, 100, 30))
            buybutton = button(450, 785, 100, 30, (215, 215, 215))
            ignore_text = font.render("Ignore", True,(0, 0, 0), (215, 215, 215) )
            ignore_rect = py.draw.rect(screen, (215, 215, 215), (590, 785, 100, 30))
            ignore_button = button(590, 785, 100, 30, (215, 215, 215))
            if buybutton.draw(screen):
                player1.money -= 60
                brdwlkcount = 0
                turn += 1
            elif ignore_button.draw(screen):
                turn += 1
            screen.blit(buy_text, buy_Rect)
            screen.blit(ignore_text, ignore_rect)
        elif brdwlkcount != 1:
            rent_text = font.render("Pay RENT", True, (0, 0, 0), (215, 215, 215))
            rent_Rect = py.draw.rect(screen, ((215, 215, 215), (300, 400, 100, 30)))
            player1.money -= 2
            player2.money += 2
            turn += 1

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

    def p2buttons(buynum, upgradenum):
        font = py.font.Font('freesansbold.ttf', 24)
        global propownerp2
        if propownerp2 == 0:
            buyButton = button(400, 800, 100, 30, (0, 255, 0))
            buy_rect = py.draw.rect(screen, (0, 255, 0), (400, 800, 100, 30))
            buy = font.render("Buy", True, (0, 0, 0), (0, 255, 0))
            if buyButton.draw(screen):
                player2.money -= buynum
                propownerp2 = 1
                global end_turn
                end_turn = 0
            screen.blit(buy, buy_rect)
        if propownerp2 != 0:
            house = 0
            upgradeButton = button(400, 800, 100, 30, (0, 255, 0))
            upgrade_rect = py.draw.rect(screen, (0, 255, 0), (400, 800, 100, 30))
            upgrade = font.render("Upgrade", True, (0, 0, 0), (0, 255, 0))
            if upgradeButton.draw(screen) and (house < 4):
                player2.money -= upgradenum
                house += 1
                end_turn = 0
            screen.blit(upgrade, upgrade_rect)
        closeButton = button(620, 800, 100, 30, (255, 0, 0))
        close_rect = py.draw.rect(screen, (0, 255, 0), (620, 800, 100, 30))
        close = font.render("Close", True, (0, 0, 0), (255, 0, 0))
        screen.blit(close, close_rect)
        if closeButton.draw(screen):
            end_turn = 0
        screen.blit(close, close_rect)

    #Mediterranean Avenue
    if ((800 < player2.x < 870) and (820 < player2.y < 960)) and (turn % 2 == 1) and (end_turn == 1):
        mediterraneanAvenue = py.image.load("PropertyCards/Mediterranean_Ave.png")
        screen.blit(mediterraneanAvenue, (300, 400))
        global propownerp2
        propownerp2 = 0
        p2buttons(60, 50)

    #Baltic Avenue
    if ((660 < player2.x < 730) and (820 < player2.y < 960)) and (turn % 2 == 1) and (end_turn == 1):
        balticAvenue = py.image.load("PropertyCards/Baltic_Ave.png")
        screen.blit(balticAvenue, (300, 400))
        propownerp2 = 0
        p2buttons(60, 50)

    #Reading Railroad
    if ((520 < player2.x < 590) and (820 < player2.y < 960)) and (turn % 2 == 1) and (end_turn == 1):
        readingRailroad = py.image.load("PropertyCards/Reading_Railroad.png")
        screen.blit(readingRailroad, (300, 400))

    #Oriental Avenue
    if ((450 < player2.x < 520) and (820 < player2.y < 960)) and (turn % 2 == 1) and (end_turn == 1):
        orientalAvenue = py.image.load("PropertyCards/Oriental_Ave.png")
        screen.blit(orientalAvenue, (300, 400))
        propownerp2 = 0
        p2buttons(100, 50)

    #Vermont Avenue
    if ((310 < player2.x < 380) and (820 < player2.y < 960)) and (turn % 2 == 1) and (end_turn == 1):
        vermontAvenue = py.image.load("PropertyCards/Vermont_Ave.png")
        screen.blit(vermontAvenue, (300, 400))
        propownerp2 = 0
        p2buttons(100, 50)

    #Connecticut Avenue
    if ((240 < player2.x < 310) and (820 < player2.y < 960)) and (turn % 2 == 1) and (end_turn == 1):
        connecticutAvenue = py.image.load("PropertyCards/Connecticut_Ave.png")
        screen.blit(connecticutAvenue, (300, 400))
        propownerp2 = 0
        p2buttons(120, 50)

    #St. Charles Place
    if ((100 < player2.x < 240) and (750 < player2.y < 820)) and (turn % 2 == 1) and (end_turn == 1):
        stCharlesPlace = py.image.load("PropertyCards/St. Charles Pl.png")
        screen.blit(stCharlesPlace, (300, 400))
        propownerp2 = 0
        p2buttons(140, 50)

    #Electric Company
    if ((100 < player2.x < 240) and (680 < player2.y < 750)) and (turn % 2 == 1) and (end_turn == 1):
        electricCompany = py.image.load("PropertyCards/Electric_Company.png")
        screen.blit(electricCompany, (300, 400))

    #States Avenue
    if ((100 < player2.x < 240) and (610 < player2.y < 680)) and (turn % 2 == 1) and (end_turn == 1):
        statesAvenue = py.image.load("PropertyCards/States_Ave.png")
        screen.blit(statesAvenue, (300, 400))
        propownerp2 = 0
        p2buttons(140, 50)

    #Virginia Avenue
    if ((100 < player2.x < 240) and (540 < player2.y < 610)) and (turn % 2 == 1) and (end_turn == 1):
        virginiaAvenue = py.image.load("PropertyCards/Virginia_Ave.png")
        screen.blit(virginiaAvenue, (300, 400))
        propownerp2 = 0
        p2buttons(160, 50)

    #Pennsylvania Railroad
    if ((100 < player2.x < 240) and (470 < player2.y < 540)) and (turn % 2 == 1) and (end_turn == 1):
        pennsylaniaRailroad = py.image.load("PropertyCards/Pennsylvania_Railroad.png")
        screen.blit(pennsylaniaRailroad, (300, 400))

    #St. James Place
    if ((100 < player2.x < 240) and (400 < player2.y < 470)) and (turn % 2 == 1) and (end_turn == 1):
        stJamesPlace = py.image.load("PropertyCards/St. James Pl.png")
        screen.blit(stJamesPlace, (300, 400))
        propownerp2 = 0
        p2buttons(180, 50)

    #Tennessee Avenue
    if ((100 < player2.x < 240) and (260 < player2.y < 330)) and (turn % 2 == 1) and (end_turn == 1):
        tennesseeAvenue = py.image.load("PropertyCards/Tennessee_Ave.png")
        screen.blit(tennesseeAvenue, (300, 400))
        propownerp2 = 0
        p2buttons(180, 50)

    #New York Avenue
    if ((100 < player2.x < 240) and (190 < player2.y < 260)) and (turn % 2 == 1) and (end_turn == 1):
        newYorkAvenue = py.image.load("PropertyCards/New_York_Ave.png")
        screen.blit(newYorkAvenue, (300, 400))
        propownerp2 = 0
        p2buttons(200, 50)

    #Kentucky Avenue
    if ((240 < player2.x < 310) and (50 < player2.y < 190)) and (turn % 2 == 1) and (end_turn == 1):
        kentuckyAvenue = py.image.load("PropertyCards/Kentucky_Ave.png")
        screen.blit(kentuckyAvenue, (300, 400))
        propownerp2 = 0
        p2buttons(220, 50)

    #Indiana Avenue
    if ((380 < player2.x < 450) and (50 < player2.y < 190)) and (turn % 2 == 1) and (end_turn == 1):
        indianaAvenue = py.image.load("PropertyCards/Indiana_Ave.png")
        screen.blit(indianaAvenue, (300, 400))
        propownerp2 = 0
        p2buttons(220, 50)

    #Illinois Avenue
    if ((450 < player2.x < 520) and (50 < player2.y < 190)) and (turn % 2 == 1) and (end_turn == 1):
        illinoisAvenue = py.image.load("PropertyCards/Illinois_Ave.png")
        screen.blit(illinoisAvenue, (300, 400))
        propownerp2 = 0
        p2buttons(240, 50)

    #B. & O. Railroad
    if ((520 < player2.x < 590) and (50 < player2.y < 190)) and (turn % 2 == 1) and (end_turn == 1):
        bandoRailroad = py.image.load("PropertyCards/BandO_Railroad.png")
        screen.blit(bandoRailroad, (300, 400))
    #Atlantic Avenue
    if ((590 < player2.x < 660) and (50 < player2.y < 190)) and (turn % 2 == 1) and (end_turn == 1):
        atlanticAvenue = py.image.load("PropertyCards/Atlantic_Avenue.png")
        screen.blit(atlanticAvenue, (300, 400))
        propownerp2 = 0
        p2buttons(260, 50)

    #Ventnor Avenue
    if ((660 < player2.x < 730) and (50 < player2.y < 190)) and (turn % 2 == 1) and (end_turn == 1):
        ventnorAvenue = py.image.load("PropertyCards/Ventnor_Avenue.png")
        screen.blit(ventnorAvenue, (300, 400))
        propownerp2 = 0
        p2buttons(260, 50)

    #Water Works
    if ((730 < player2.x <800) and (50 < player2.y < 190)) and (turn % 2 == 1) and (end_turn == 1):
        waterWorks = py.image.load("PropertyCards/Water_Works.png")
        screen.blit(waterWorks, (300, 400))

    #Marvin Gardens
    if ((800 < player2.x < 870) and (50 < player2.y < 190)) and (turn % 2 == 1) and (end_turn == 1):
        marvinGardens = py.image.load("PropertyCards/Marvin_Gardens.png")
        screen.blit(marvinGardens, (300, 400))
        propownerp2 = 0
        p2buttons(280, 50)

    #Pacific Avenue
    if ((870 < player2.x < 1010) and (190 < player2.y < 260)) and (turn % 2 == 1) and (end_turn == 1):
        pacificAvenue = py.image.load("PropertyCards/Pacific_Avenue.png")
        screen.blit(pacificAvenue, (300, 400))
        propownerp2 = 0
        p2buttons(300, 50)

    #North Carolina Avenue
    if ((870 < player2.x < 1010) and (260 < player2.y < 330)) and (turn % 2 == 1) and (end_turn == 1):
        northCarolinaAvenue = py.image.load("PropertyCards/North_Carolina.png")
        screen.blit(northCarolinaAvenue, (300, 400))
        propownerp2 = 0
        p2buttons(300, 50)

    #Pennsylvania Avenue
    if ((870 < player2.x < 1010) and (400 < player2.y < 470)) and (turn % 2 == 1) and (end_turn == 1):
        pennsylvaniaAvenue = py.image.load("PropertyCards/Pennsylvania_Avenue.png")
        screen.blit(pennsylvaniaAvenue, (300, 400))
        propownerp2 = 0
        p2buttons(320, 50)

    #Short Line
        
    #Park Place
    if ((870 < player2.x < 1010) and (610 < player2.y < 680)) and (turn % 2 == 1) and (end_turn == 1):
        parkPlace = py.image.load("PropertyCards/Park_Place.png")
        screen.blit(parkPlace, (300, 400))
        propownerp2 = 0
        p2buttons(350, 50)

    #BoardWalk
    if ((870 < player2.x < 1010) and (680 < player2.y < 750)) and (turn % 2 == 1) and (end_turn == 1):
        boardwalk = py.image.load("PropertyCards/Boardwalk.png")
        screen.blit(boardwalk, (300, 400))
        propownerp2 = 0
        p2buttons(400, 50)