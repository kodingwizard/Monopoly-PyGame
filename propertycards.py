import pygame as py

py.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

screen = py.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), py.RESIZABLE)

def propcardsp1():
    from mnply_board import player1
    from mnply_board import player2
    from mnply_board import player
    from mnply_board import turn
    from mnply_board import end_turn
    if ((800 < player1.x < 870) and (820 < player1.y < 960) and (turn % 2 == 0) and (end_turn == 1)):
        med_ave = py.image.load("PropertyCards/Mediterranean_Ave.png")
        screen.blit(med_ave, (325, 375))
    elif ((660 <player1.x < 730) and (820 < player1.y < 960) and (turn % 2 == 0) and (end_turn == 1)):
        baltic_ave = py.image.load("PropertyCards/Baltic_Ave.png")
        screen.blit(baltic_ave, (325, 375))
    
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
    elif ((450 < player1.x < 520) and (820 < player1.y < 960) and (turn % 2 == 0) and (end_turn == 1)):
        oriental_ave = py.image.load("PropertyCards/Oriental_Ave.png")
        screen.blit(oriental_ave, (325, 375))
    elif ((310 < player1.x < 380) and (820 < player1.y < 960) and (turn % 2 == 0) and (end_turn == 1)):
        vermont_ave = py.image.load("PropertyCards/Vermont_Ave.png")
        screen.blit(vermont_ave, (325, 375))
    elif ((240 < player1.x < 310) and (820 < player1.y < 960) and (turn % 2 == 0) and (end_turn == 1)):
        conn_ave = py.image.load("PropertyCards/Connecticut_Ave.png")
        screen.blit(conn_ave, (325, 375))
    elif ((100 < player1.x < 240) and (750 < player1.y < 820) and (turn % 2 == 0) and (end_turn == 1)):
        stcharles = py.image.load("PropertyCards/St. Charles Pl.png")
        screen.blit(stcharles, (325, 375))
    elif (100 < player1.x < 240) and (680 < player1.y < 750) and (turn % 2 == 0) and (end_turn == 1):
        elec_comp = py.image.load("PropertyCards/Electric_Company.png")
        screen.blit(elec_comp, (325, 375))
    elif (100 < player1.x < 240) and (610 < player1.y < 680) and (turn % 2 == 0) and (end_turn == 1):
        states_ave = py.image.load("PropertyCards/States_Ave.png")
        screen.blit(states_ave, (325, 375))
    elif(100 < player1.x < 240) and (540 < player1.y < 610) and (turn % 2 == 0) and (end_turn == 1):
        virginia_ave = py.image.load("PropertyCards/Virginia_Ave.png")
        screen.blit(virginia_ave, (325, 375))
    elif ((100 < player1.x < 240) and (470 < player1.y < 540) and (turn % 2 == 0) and (end_turn == 1)):
        penn_railroad = py.image.load("PropertyCards/Pennsylvania_Railroad.png")
        screen.blit(penn_railroad, (325, 375))
    elif ((100 < player1.x < 240) and (400 < player1.y < 470) and (turn % 2 == 0) and (end_turn == 1)):
        stjames = py.image.load("PropertyCards/St. James Pl.png")
        screen.blit(stjames, (325, 375))
    elif ((100 < player1.x < 240) and (260 < player1.y < 330) and (turn % 2 == 0) and (end_turn == 1)):
        tenn_ave = py.image.load("PropertyCards/Tennessee_Ave.png")
        screen.blit(tenn_ave, (325, 375))
    elif ((100 < player1.x < 240) and (190 < player1.y < 260) and (turn % 2 == 0) and (end_turn == 1)):
        ny_ave = py.image.load("PropertyCards/New_York_Ave.png")
        screen.blit(ny_ave, (325, 375))
    elif ((240 < player1.x  < 310) and (50 < player1.y < 190) and (turn % 2 == 0) and (end_turn == 1)):
        kent_ave = py.image.load("PropertyCards/Kentucky_Ave.png")
        screen.blit(kent_ave, (325, 375))
    elif ((380 < player1.x < 450) and (50 < player1.y < 190) and (turn % 2 == 0) and (end_turn == 1)):
        indi_ave = py.image.load("PropertyCards/Indiana_Ave.png")
        screen.blit(indi_ave, (325, 375))
    elif ((450 < player1.x < 520) and (50 < player1.y < 190) and (turn % 2 == 0) and (end_turn == 1)):
        ill_ave = py.image.load("PropertyCards/Illinois_Ave.png")
        screen.blit(ill_ave, (325, 375))
    elif ((520 < player1.x < 590) and (50 < player1.y < 190) and (turn % 2 == 0) and (end_turn == 1)):
        bo_railroad = py.image.load("PropertyCards/BandO_Railroad.png")
        screen.blit(bo_railroad, (325, 375))
    elif ((590 < player1.x < 660) and (50 < player1.y < 190) and (turn % 2 == 0) and (end_turn == 1)):
        atlantic_ave = py.image.load("PropertyCards/Atlantic_Avenue.png")
        screen.blit(atlantic_ave, (325, 375))
    elif ((660 < player1.x < 730) and (50 < player1.y < 190) and (turn % 2 == 0) and (end_turn == 1)):
        ventnor_ave = py.image.load("PropertyCards/Ventnor_Ave.png")
        screen.blit(ventnor_ave, (325, 375))
    elif ((730 < player1.x < 800) and (50 < player1.y < 190) and (turn % 2 == 0) and (end_turn == 1)):
        water_works = py.image.load("PropertyCards/Water_Works.png")
        screen.blit(water_works, (325, 375))
    elif ((800 < player1.x < 870) and (50 < player1.y < 190) and (turn % 2 == 0) and (end_turn == 1)):
        marv_gardens = py.image.load("PropertyCards/Marvin_Gardens.png")
        screen.blit(marv_gardens, (325, 375))
    elif ((870 < player1.x < 1010) and (190 < player1.y < 260) and (turn % 2 == 0) and (end_turn == 1)):
        pacific_ave = py.image.load("PropertyCards/Pacific_Avenue.png")
        screen.blit(pacific_ave, (325, 375))
    elif ((870 < player1.x < 1010) and (260 < player1.y < 330) and (turn % 2 == 0) and (end_turn == 1)):
        nc_ave= py.image.load("PropertyCards/North_Carolina.png")
        screen.blit(nc_ave, (325, 375))
    elif ((870 < player1.x < 1010) and (400 < player1.y < 470) and (turn % 2 == 0) and (end_turn == 1)):
        penn_ave = py.image.load("PropertyCards/Pennsylvania_Avenue.png")
        screen.blit(penn_ave, (325, 375))
    elif ((870 < player1.x < 1010) and (470 < player1.y < 540) and (turn % 2 == 0) and (end_turn == 1)):
        short_line = py.image.load("PropertyCards/Short_Line.png")
        screen.blit(short_line, (325, 375))
    elif ((870 < player1.x < 1010) and (610 < player1.y < 680) and (turn % 2 == 0) and (end_turn == 1)):
        park_place = py.image.load("PropertyCards/Park_Place.png")
        screen.blit(park_place, (325, 375))
    elif ((870 < player1.x < 1010) and (750 < player1.y < 820) and (turn % 2 == 0) and (end_turn == 1)):
        boardwalk = py.image.load("PropertyCards/Boardwalk.png")
        screen.blit(boardwalk, (325, 375))

def propcardsp2():
    from mnply_board import player2
    from mnply_board import turn
    from mnply_board import end_turn
    #Mediterranean Avenue
    if ((800 < player2.x < 870) and (820 < player2.y < 960)) and (turn % 2 == 1) and (end_turn == 1):
        mediterraneanAvenue = py.image.load("PropertyCards/Mediterranean_Avenue.png")
        screen.blit(mediterraneanAvenue, (300, 400))
    #Baltic Avenue
    if ((660 < player2.x < 730) and (820 < player2.y < 960)) and (turn % 2 == 1) and (end_turn == 1):
        balticAvenue = py.image.load("PropertyCards/Baltic_Ave.png")
        screen.blit(balticAvenue, (300, 400))
    #Reading Railroad
    if ((520 < player2.x < 590) and (820 < player2.y < 960)) and (turn % 2 == 1) and (end_turn == 1):
        readingRailroad = py.image.load("PropertyCards/Reading_Railroad.png")
        screen.blit(readingRailroad, (300, 400))
    #Oriental Avenue
    if ((450 < player2.x < 520) and (820 < player2.y < 960)) and (turn % 2 == 1) and (end_turn == 1):
        orientalAvenue = py.image.load("PropertyCards/Oriental_Ave.png")
        screen.blit(orientalAvenue, (300, 400))
    #Vermont Avenue
    if ((310 < player2.x < 380) and (820 < player2.y < 960)) and (turn % 2 == 1) and (end_turn == 1):
        vermontAvenue = py.image.load("PropertyCards/Vermont_Ave.png")
        screen.blit(vermontAvenue, (300, 400))
    #Connecticut Avenue
    if ((240 < player2.x < 310) and (820 < player2.y < 960)) and (turn % 2 == 1) and (end_turn == 1):
        connecticutAvenue = py.image.load("PropertyCards/Connecticut_Ave.png")
        screen.blit(connecticutAvenue, (300, 400))
    #St. Charles Place
    if ((100 < player2.x < 240) and (750 < player2.y < 820)) and (turn % 2 == 1) and (end_turn == 1):
        stCharlesPlace = py.image.load("PropertyCards/St. Charles Pl.png")
        screen.blit(stCharlesPlace, (300, 400))
    #Electric Company
    if ((100 < player2.x < 240) and (680 < player2.y < 750)) and (turn % 2 == 1) and (end_turn == 1):
        electricCompany = py.image.load("PropertyCards/Electric_Company.png")
        screen.blit(electricCompany, (300, 400))
    #States Avenue
    if ((100 < player2.x < 240) and (610 < player2.y < 680)) and (turn % 2 == 1) and (end_turn == 1):
        statesAvenue = py.image.load("PropertyCards/States_Ave.png")
        screen.blit(statesAvenue, (300, 400))
    #Virginia Avenue
    if ((100 < player2.x < 240) and (540 < player2.y < 610)) and (turn % 2 == 1) and (end_turn == 1):
        virginiaAvenue = py.image.load("PropertyCards/Virginia_Ave.png")
        screen.blit(virginiaAvenue, (300, 400))
    #Pennsylvania Railroad
    if ((100 < player2.x < 240) and (470 < player2.y < 540)) and (turn % 2 == 1) and (end_turn == 1):
        pennsylaniaRailroad = py.image.load("PropertyCards/Pennsylvania_Railroad.png")
        screen.blit(pennsylaniaRailroad, (300, 400))
    #St. James Place
    if ((100 < player2.x < 240) and (400 < player2.y < 470)) and (turn % 2 == 1) and (end_turn == 1):
        stJamesPlace = py.image.load("PropertyCards/St. James Pl.png")
        screen.blit(stJamesPlace, (300, 400))
    #Tennessee Avenue
    if ((100 < player2.x < 240) and (260 < player2.y < 330)) and (turn % 2 == 1) and (end_turn == 1):
        tennesseeAvenue = py.image.load("PropertyCards/Tennessee_Ave.png")
        screen.blit(tennesseeAvenue, (300, 400))
    #New York Avenue
    if ((100 < player2.x < 240) and (190 < player2.y < 260)) and (turn % 2 == 1) and (end_turn == 1):
        newYorkAvenue = py.image.load("PropertyCards/New_York_Ave.png")
        screen.blit(newYorkAvenue, (300, 400))
    #Kentucky Avenue
    if ((240 < player2.x < 310) and (50 < player2.y < 190)) and (turn % 2 == 1) and (end_turn == 1):
        kentuckyAvenue = py.image.load("PropertyCards/Kentucky_Ave.png")
        screen.blit(kentuckyAvenue, (300, 400))
    #Indiana Avenue
    if ((380 < player2.x < 450) and (50 < player2.y < 190)) and (turn % 2 == 1) and (end_turn == 1):
        indianaAvenue = py.image.load("PropertyCards/Indiana_Ave.png")
        screen.blit(indianaAvenue, (300, 400))
    #Illinois Avenue
    if ((450 < player2.x < 520) and (50 < player2.y < 190)) and (turn % 2 == 1) and (end_turn == 1):
        illinoisAvenue = py.image.load("PropertyCards/Illinois_Ave.png")
        screen.blit(illinoisAvenue, (300, 400))
    #B. & O. Railroad
    if ((520 < player2.x < 590) and (50 < player2.y < 190)) and (turn % 2 == 1) and (end_turn == 1):
        bandoRailroad = py.image.load("PropertyCards/BandO_Railroad.png")
        screen.blit(bandoRailroad, (300, 400))
    #Atlantic Avenue
    if ((590 < player2.x < 660) and (50 < player2.y < 190)) and (turn % 2 == 1) and (end_turn == 1):
        atlanticAvenue = py.image.load("PropertyCards/Atlantic_Avenue.png")
        screen.blit(atlanticAvenue, (300, 400))
    #Ventnor Avenue
    if ((660 < player2.x < 730) and (50 < player2.y < 190)) and (turn % 2 == 1) and (end_turn == 1):
        ventnorAvenue = py.image.load("PropertyCards/Ventnor_Avenue.png")
        screen.blit(ventnorAvenue, (300, 400))
    #Water Works
    if ((730 < player2.x <800) and (50 < player2.y < 190)) and (turn % 2 == 1) and (end_turn == 1):
        waterWorks = py.image.load("PropertyCards/Water_Works.png")
        screen.blit(waterWorks, (300, 400))
    #Marvin Gardens
    if ((800 < player2.x < 870) and (50 < player2.y < 190)) and (turn % 2 == 1) and (end_turn == 1):
        marvinGardens = py.image.load("PropertyCards/Marvin_Gardens.png")
        screen.blit(marvinGardens, (300, 400))
    #Pacific Avenue
    if ((870 < player2.x < 1010) and (190 < player2.y < 260)) and (turn % 2 == 1) and (end_turn == 1):
        pacificAvenue = py.image.load("PropertyCards/Pacific_Avenue.png")
        screen.blit(pacificAvenue, (300, 400))
    #North Carolina Avenue
    if ((870 < player2.x < 1010) and (260 < player2.y < 330)) and (turn % 2 == 1) and (end_turn == 1):
        northCarolinaAvenue = py.image.load("PropertyCards/North_Carolina.png")
        screen.blit(northCarolinaAvenue, (300, 400))
    #Pennsylvania Avenue
    if ((870 < player2.x < 1010) and (400 < player2.y < 470)) and (turn % 2 == 1) and (end_turn == 1):
        pennsylvaniaAvenue = py.image.load("PropertyCards/Pennsylvania_Avenue.png")
        screen.blit(pennsylvaniaAvenue, (300, 400))
    #Short Line
    if ((870 < player2.x < 1010) and (470 < player2.y < 540)) and (turn % 2 == 1) and (end_turn == 1):
        shortLine = py.image.load("PropertyCards/Short_Line.png")
        screen.blit(shortLine, (300, 400))
    #Park Place
    if ((870 < player2.x < 1010) and (610 < player2.y < 680)) and (turn % 2 == 1) and (end_turn == 1):
        parkPlace = py.image.load("PropertyCards/Park_Place.png")
        screen.blit(parkPlace, (300, 400))
    #BoardWalk
    if ((870 < player2.x < 1010) and (750 < player2.y < 820)) and (turn % 2 == 1) and (end_turn == 1):
        boardwalk = py.image.load("PropertyCards/Boardwalk.png")
        screen.blit(boardwalk, (300, 400))
