import pygame as py
import random

py.init()


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), py.RESIZABLE)

def board():
    full_board = py.image.load("Streets.png")
    full_board_scale = py.transform.scale(full_board, (full_board.get_width()*1, full_board.get_height()*0.99))
    screen.blit(full_board_scale, (-88, -10))


class player():
    def __init__(self, x, y, width, height, color, jail, money, jailfree, orbit, rail):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.jail = jail
        self.money = money
        self.jailfree = jailfree
        self.orbit = orbit
        self.rail = rail

    def draw(self, win):
        py.draw.rect(win, self.color, self.rect)


def diceroll():


    Diceroll = [ ]
    for i in range (1):
        global N
        N = random.randint(1,6)
        global A
        A = random.randint(1,6)


        Diceroll.append(N)
        Diceroll.append(A)
    print(Diceroll)
    global dice_sum
    dice_sum = N + A
    print("Total: %s" %dice_sum)
diceroll()


def dicetext():      
    global font, text, textRect, text1, textRect1, text2, textRect2, text3, textRect3
    font = py.font.Font('freesansbold.ttf', 32)
    text = font.render(str(N), True, (0, 0, 0), (255, 255, 255))
    textRect = py.draw.rect(screen, (255,255,255), (1160, 50, 140, 140))
    text1 = font.render(str(A), True, (0, 0, 0), (255, 255, 255))
    textRect1 = py.draw.rect(screen, (255,255,255), (1100, 50, 140, 140))
    text2 = font.render('Total: ' + str(dice_sum), True, (0, 0, 0), (255, 255, 255))
    textRect2 = py.draw.rect(screen, (255,255,255), (1050, 130, 140, 140))
   

def playerinfo():
    global font1, p1text, p1textRect, p1text1, p1textRect1, p2text, p2textRect, p2text1, p2textRect1
    font1 = py.font.Font('freesansbold.ttf', 16)
    p1text = font1.render("Player 1's Money: " + str(player1.money), True, (0, 0, 0), (255, 255, 255))
    p1textRect = py.draw.rect(screen, (255,255,255), (1040, 700, 140, 140))
    p1text1 = font1.render("Player 1's Jail Free Cards: " + str(player1.jailfree), True, (0, 0, 0), (255, 255, 255))
    p1textRect1 = py.draw.rect(screen, (255,255,255), (1040, 750, 140, 140))
    p2text = font1.render("Player 2's Money: " + str(player2.money), True, (0, 0, 0), (255, 255, 255))
    p2textRect = py.draw.rect(screen, (255,255,255), (1040, 800, 140, 140))
    p2text1 = font1.render("Player 2's Jail Free Cards: " + str(player2.jailfree), True, (0, 0, 0), (255, 255, 255))
    p2textRect1 = py.draw.rect(screen, (255,255,255), (1040, 850, 140, 140))
    



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
        if (self.x < posx < self.x+200) and (self.y < posy < self.y+200):
            if (click[0] == 1) and (self.clicked == False):
                self.clicked = True
                action = True
            if click[0] == 0:
                self.clicked = False
        return action
         
player1 = player(888, 783, 35, 35, (255, 0, 0), 0, 1500, 0, 0, 0)
player2 = player(888, 837, 35, 35, (0, 255, 0), 0, 1500, 0, 0, 0)
font = py.font.Font('freesansbold.ttf', 32)
dice_button_text = font.render("Roll the Dice", True, (0, 0, 0), (215, 215, 215))
dbt_Rect = py.draw.rect(screen, (215, 215, 215), (1050, 330, 140, 140))
dicebutton = button(1050, 300, 200, 100, (215, 215, 215))
endturn = button(1050, 500, 200, 100, (215, 215, 215))
etb_rect = py.draw.rect(screen, (215, 215, 215), (1050, 530, 140, 140))
etb_text = font.render("End Turn", True, (0, 0, 0), (215, 215, 215))
font1 = py.font.Font('freesansbold.ttf', 16)
p1text = font1.render("Player 1's Money: " + str(player1.money), True, (0, 0, 0), (255, 255, 255))
p1textRect = py.draw.rect(screen, (255,255,255), (1040, 700, 140, 140))
p1text1 = font1.render("Player 1's Jail Free Cards: " + str(player1.jailfree), True, (0, 0, 0), (255, 255, 255))
p1textRect1 = py.draw.rect(screen, (255,255,255), (1040, 750, 140, 140))
p2text = font1.render("Player 2's Money: " + str(player2.money), True, (0, 0, 0), (255, 255, 255))
p2textRect = py.draw.rect(screen, (255,255,255), (1040, 800, 140, 140))
p2text1 = font1.render("Player 2's Jail Free Cards: " + str(player2.jailfree), True, (0, 0, 0), (255, 255, 255))
p2textRect1 = py.draw.rect(screen, (255,255,255), (1040, 850, 140, 140))

#Property Values
medavep1 = 0
medavep2 = 0
balavep1 = 0
balavep2 = 0
oriavep1 = 0
oriavep2 = 0
veravep1 = 0
veravep2 = 0
conavep1 = 0
conavep2 = 0
chaavep1 = 0
chaavep2 = 0
staavep1 = 0
staavep2 = 0
viravep1 = 0
viravep2 = 0
jamavep1 = 0
jamavep2 = 0
tenavep1 = 0
tenavep2 = 0
nyavep1 = 0
nyavep2 = 0
kenavep1 = 0
kenavep2 = 0
indavep1 = 0
indavep2 = 0
illavep1 = 0
illavep2 = 0
atlavep1 = 0
atlavep2 = 0
venavep1 = 0
venavep2 = 0
margarp1 = 0
margarp2 = 0
pacavep1 = 0
pacavep2 = 0
caravep1 = 0
caravep2 = 0
penavep1 = 0
penavep2 = 0
parplap1 = 0
parplap2 = 0
brdwlkp1 = 0
brdwlkp2 = 0
bo_railp1 = 0
bo_railp2 = 0
shortlinep1 = 0
shortlinep2 = 0
penn_railp1 = 0
penn_railp2 = 0
readingrailp1 = 0
readingrailp2 = 0
elecomp1 = 0
elecomp2 = 0
watworp1 = 0
watworp2 = 0


turn = 1
stamp = False
run = True
end_turn = 0
while run:
    screen.fill((255, 255, 255))
    board()


    if stamp == False:
        player1.draw(screen)
        player2.draw(screen)


    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
       

    if dicebutton.draw(screen) and (end_turn == 0):
        diceroll()
        dicetext()
        stamp = True
        end_turn = 1
        if (turn % 2 == 1):#see if it is player one's turn
            player1.orbit += dice_sum * 70
            if (player1.jail == 0):
                if (188 < player1.x <= 888) and (player1.y == 783):#bottom right to bottom left
                    player1.x -= (70*dice_sum)
                    if player1.x < 188:#if going around bottom left corner
                        player1.y -= 188 - player1.x
                        player1.x = 188
                elif (player1.x == 188) and (83 < player1.y <= 783):#bottom left to top left
                    player1.y -= (70*dice_sum)
                    if player1.y < 83:#if going around top left corner
                        player1.x += 143 - player1.y
                        player1.y = 83
                elif (188 <= player1.x < 888) and (player1.y == 83):#top left to top right
                    player1.x += (70*dice_sum)
                    if player1.x > 888:#if going around top right corner
                        player1.y += player1.x - 888
                        player1.x = 888
                elif (player1.x == 888) and (83 <= player1.y < 783):#top right to bottom right
                    player1.y += (70*dice_sum)
                    if player1.y > 783:#if going around bottom right corner
                        player1.x -= player1.y - 843
                        player1.y = 783
                player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree, player1.orbit, player1.rail)
                turn += 1#making it next person's turn
            else:
                turn += 1 #next person's turn
        else:
            player2.orbit += dice_sum * 70
            if (player2.jail == 0):
                if (188 < player2.x <= 888) and (780 <= player2.y <= 900):#bottom right to bottom left
                    player2.x -= (70*dice_sum)
                    if player2.x < 188:#if going around bottom left corner
                        player2.y = 783
                        player2.y -= 188 - player2.x
                        player2.x = 118
                    if (100 <= player2.x <= 240) and (760 <= player2.y <= 900):#if reaching bottom left corner
                        player2.x = 118
                        player2.y = 783
                elif (100 <= player2.x <= 240) and (137 < player2.y <= 837):#bottom left to top left
                    player2.y -= (70*dice_sum)
                    if player2.y < 83:#if going around top left corner
                        player2.x = 188
                        player2.x += 143 - player2.y
                        player2.y = 13
                    if (100 <= player2.x <= 240)and (-10 <= player2.y <= 130):#if reaching top left corner
                        player2.x = 188
                        player2.y = 13
                elif (118 <= player2.x < 888) and (-10 <= player2.y <= 130):#top left to top right
                    player2.x += (70*dice_sum)
                    if player2.x > 888:#if going around top right corner
                        player2.y = 83
                        player2.y += player2.x - 888
                        player2.x = 958
                    if (870 <= player2.x <= 1010) and (-10 <= player2.y <= 230):#if reaching top right corner
                        player2.x = 958
                        player2.y = 83
                elif (870 <= player2.x <= 1010) and (83 <= player2.y < 837):#top right to bottom right
                    player2.y += (70*dice_sum)
                    if player2.y > 783:#if going around bottom right corner
                        player2.x = 888
                        player2.x -= player2.y - 843
                        player2.y = 837
                    if (870 <= player2.x <= 1010) and (760 <= player2.y <= 900):#if reaching bottom right corner
                        player2.x = 888
                        player2.y = 837
                player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit, player2.rail)
                turn += 1#making it next person's turn
            else:
                turn += 1#making it next person's turn

            if (870 < player1.x < 1010) and (-10< player1.y <130):
                player1.jail = 1
                player1.x = 188
                player1.y = 783
                player1.orbit = 700
                player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree, player1.orbit, player1.rail)
            if (870 < player2.x < 1010) and (-10< player2.y <160):
                player2.jail = 1
                player2.x = 118
                player2.y = 783
                player2.orbit = 700
                player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit, player2.rail)
        
        if player1.orbit >= 2800:
            player1.money += 200
            player1.orbit = (888 - player1.x) + (783 - player1.y)
            player1 = player(player1.x, player1.y, 35, 35, (255, 0, 0), player1.jail, player1.money, player1.jailfree, player1.orbit, player1.rail)
        if player2.orbit >= 2800:
            player2.money += 200
            player2.orbit = (888 - player2.x) + (783 - player2.y)
            player2 = player(player2.x, player2.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit, player2.rail)

    if (player2.x > 1010):
        if (-10 < player2.y < 130):
            player2.x = 958
            player2.y = 83
            player2 = player(player1.x, player1.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit, player2.rail)
        if ( 130 < player2.y < 760):
            player2.x = 958
            player2 = player(player1.x, player1.y, 35, 35, (0, 255, 0), player2.jail, player2.money, player2.jailfree, player2.orbit, player2.rail)

    from communitycard import * 
    comcardp1()
    comcardp2()
    from chancecard import *
    chancecardp1()
    chancecardp2()

    def propendturn():
        global end_turn
        end_turn = 2

    from propertycards import *
    propcards()

    #Jail Free Card
    if (player1.jailfree != 0) and (player1.jail > 0) and ((turn % 2 == 1) and (end_turn == 0)):
        font = py.font.Font('freesansbold.ttf', 32)
        jailfreetext = font.render("Use JAILFREECARD", True, (0, 0, 0), (215, 215, 215))
        jf_Rect = py.draw.rect(screen, (215, 215, 215), (325, 375, 200, 60))
        jailfreebutton = button(325, 375, 200, 60, (215, 215, 215))
        if jailfreebutton.draw(screen):
            player1.jail = 0
            player1.jailfree -= 1
        screen.blit(jailfreetext, jf_Rect)

    if (player2.jailfree != 0) and (player2.jail > 0) and ((turn % 2 == 0) and (end_turn == 0)):
        font = py.font.Font('freesansbold.ttf', 32)
        jailfreetext = font.render("Use JAILFREECARD", True, (0, 0, 0), (215, 215, 215))
        jf_Rect = py.draw.rect(screen, (215, 215, 215), (325, 375, 200, 60))
        jailfreebutton = button(325, 375, 200, 60, (215, 215, 215))
        if jailfreebutton.draw(screen):
            player2.jail = 0
            player2.jailfree -= 1
        screen.blit(jailfreetext, jf_Rect)
    
    if endturn.draw(screen):
    #    print(end_turn)
        end_turn = 0
        if player1.jail != 0:
            if (player1.jail <= 5) and (turn & 2 == 0):
                player1.jail += 1        
            if (player1.jail == 5):
                player1.jail = 0
            else:
                if N == A:
                    player1.jail = 0
                else:
                    player1.jail += 1

        if (player2.jail != 0) and (turn % 2 == 1):
            if (player2.jail == 1):
                if (player1.jailfree != 0):
                    font = py.font.Font('freesansbold.ttf', 32)
                    jailfreetext = font.render("Use JAILFREECARD", True, (0, 0, 0), (215, 215, 215))
                    jf_Rect = py.draw.rect(screen, (215, 215, 215), (325, 375, 200, 60))
                    jailfreebutton = button(325, 375, 200, 60, (215, 215, 215))
                    if jailfreebutton.draw(screen):
                        player2.jail = 0
                        player2.jailfree -= 1
                    screen.blit(jailfreetext, jf_Rect)
                else:
                    player2.jail += 1    
                player2.jail += 1
            if (player2.jail == 5):
                player2.jail = 0
            else:  
                if N == A:
                    player2.jail = 0
                else:
                    player2.jail += 1
        #print(player1.money)
        #print(player2.money)
        print(medavep1)
        print(medavep2)
        print(balavep1)
        print(balavep2)
        print(oriavep1)
        print(oriavep2)
        print(veravep1)
        print(veravep2)
        print(conavep1)
        print(conavep2)

    if stamp == True:
        screen.blit(text, textRect)
        screen.blit(text1, textRect1)
        screen.blit(text2, textRect2)
        
    screen.blit(dice_button_text, dbt_Rect)
    screen.blit(etb_text, etb_rect)
    playerinfo()
    screen.blit(p1text, p1textRect)
    screen.blit(p1text1, p1textRect1)
    screen.blit(p2text, p2textRect)
    screen.blit(p2text1, p2textRect1)


    player1.draw(screen)
    player2.draw(screen)

#win condition
    if player1.money <= 0:
        font = py.font.Font('freesansbold.ttf', 24)
        wintext1_rect = py.draw.rect(screen, (0, 0, 0), (0, 0, 2000, 2000))
        wintext1 = font.render("Player 2 wins!", True, (255, 255, 255), (0, 0, 0))
        screen.blit(wintext1, wintext1_rect)


    elif player2.money <= 0:
        font = py.font.Font('freesansbold.ttf', 24)
        wintext2_rect = py.draw.rect(screen, (0, 0, 0), (0, 0, 2000, 2000))
        wintext2 = font.render("Player 1 wins!", True, (255, 255, 255), (0, 0, 0))
        screen.blit(wintext2, wintext2_rect)

    py.display.update()


py.quit()