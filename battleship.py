# Michael Liao
# 1/19/2022
# Battleship

from graphics import *
import random

def creategrid(x,y,win,s_label):
    l_grid = []
    l_alphabet = ["A","B","C","D","E","F","G","H","I","J"]
    Text(Point(x+200,y-50), s_label).draw(win).setSize(30)
    for i_row in range(10):
        l_inner = []
        Text(Point(x+20+i_row*40, y-15), l_alphabet[i_row]).draw(win).setSize(20)
        Text(Point(x-15, y+20+i_row*40), str(i_row+1)).draw(win).setSize(20)
        for i_col in range(10):
            l_inner.append("_")
            Rectangle(Point(x+i_col*40,y+i_row*40), Point(x+40+i_col*40,y+40+i_row*40)).draw(win)
        l_grid.append(l_inner)
    return l_grid

def compplaceships(l_comp_grid):
    l_ships = [["A","A","A","A","A",],["B","B","B","B"],["C","C","C"],["D","D","D"],["E","E"]]
    for l_ship in l_ships:
        b_valid = False
        while b_valid == False: # Keep checking if a ship's placement is invalid
            i_random_x = random.randint(0,9)
            i_random_y = random.randint(0,9)
            if l_comp_grid[i_random_y][i_random_x] == "_":
                b_valid = True
                i_coinflip = random.randint(0,1)
                i_index = 0
                if i_coinflip == 0: # Proceeding to the right
                    for s_letter in l_ship: 
                        if i_random_x+i_index > 9: # Validating that it would not go out of bounds
                            b_valid = False
                        i_index += 1
                    if b_valid == True:
                       i_index = 0
                       for s_letter in l_ship:
                            if l_comp_grid[i_random_y][i_random_x+i_index] != "_": # Validating that every grid that this ship would take up is free
                                b_valid = False
                            i_index += 1
                    if b_valid == True:
                        i_index = 0
                        for s_letter in l_ship: # Placing ship
                            l_comp_grid[i_random_y][i_random_x+i_index] = s_letter
                            i_index += 1
                if i_coinflip == 1: # Proceeding downwards
                    b_valid = True
                    i_index = 0
                    for s_letter in l_ship:
                        if i_random_y+i_index > 9: # Validating that it would not go out of bounds
                            b_valid = False
                        i_index += 1
                    if b_valid == True:
                        i_index = 0
                        for s_letter in l_ship:
                            if l_comp_grid[i_random_y+i_index][i_random_x] != "_": # Validating that every grid this ship would take up is free
                                b_valid = False
                            i_index += 1
                    if b_valid == True: # Placing ship
                        i_index = 0
                        for s_letter in l_ship:
                            l_comp_grid[i_random_y+i_index][i_random_x] = s_letter
                            i_index += 1
    return l_comp_grid

def getsquare(x, y, l_grid, l_ship, win):
    i_row = 0
    b_valid = True
    for l_row in l_grid:
        i_col = 0
        for s_value in l_row:
            if x >= (490+i_col*40) and x < (490+40+i_col*40) and y >= (80+i_row*40) and y < (80+40+i_row*40):
                if s_value != "_":
                    b_valid = False
                else:
                    temp0 = Rectangle(Point(490+i_col*40,80+i_row*40), Point(490+40+i_col*40,80+40+i_row*40))
                    temp0.draw(win).setFill("#bbf")
                    temp1 = Rectangle(Point(490+(i_col+1)*40,80+i_row*40), Point(490+40+(i_col+1)*40,80+40+i_row*40))
                    temp1.draw(win).setFill("#ffb")
                    temp2 = Rectangle(Point(490+(i_col)*40,80+(i_row+1)*40), Point(490+40+(i_col)*40,80+40+(i_row+1)*40))
                    temp2.draw(win).setFill("#ffb")
                    click = True
                    while click != False:
                        click = win.getMouse()
                        if click.getX() > (490+(i_col+1)*40) and click.getX() < (490+40+(i_col+1)*40) and click.getY() > (80+i_row*40) and click.getY() < (80+40+i_row*40):
                            temp2.undraw()
                            i_index = 0
                            for s_letter in l_ship: 
                                if i_col+i_index > 9: # Validating that it would not go out of bounds
                                     b_valid = False
                                i_index += 1
                            if b_valid == True:
                               i_index = 0
                               for s_letter in l_ship:
                                    if l_grid[i_row][i_col+i_index] != "_": # Validating that every grid that this ship would take up is free
                                        b_valid = False
                                    i_index += 1
                            if b_valid == True:
                                i_index = 0
                                for s_letter in l_ship: # Placing ship
                                    l_grid[i_row][i_col+i_index] = s_letter
                                    i_index += 1
                            click = False
                        elif click.getX() > (490+i_col*40) and click.getX() < (490+40+i_col*40) and click.getY() > (80+(i_row+1)*40) and click.getY() < (80+40+(i_row+1)*40):
                            temp1.undraw()
                            b_valid = True
                            i_index = 0
                            for s_letter in l_ship:
                                if i_row+i_index > 9: # Validating that it would not go out of bounds
                                    b_valid = False
                                i_index += 1
                            if b_valid == True:
                                i_index = 0
                                for s_letter in l_ship:
                                    if l_grid[i_row+i_index][i_col] != "_": # Validating that every grid this ship would take up is free
                                        b_valid = False
                                    i_index += 1
                            if b_valid == True: # Placing ship
                                i_index = 0
                                for s_letter in l_ship:
                                    l_grid[i_row+i_index][i_col] = s_letter
                                    i_index += 1
                            click = False
                    temp0.undraw()
                    temp1.undraw()
                    temp2.undraw()
            i_col += 1
        i_row += 1
    if b_valid == True: # Placing ship visually
        i_row = 0
        for l_row in l_grid:
            i_col = 0
            for s_value in l_row:
                if s_value != "_":
                    Text(Point(490+20+i_col*40, 80+20+i_row*40), s_value).draw(win).setSize(20)
                i_col += 1
            i_row += 1
    return b_valid, l_grid

def playerplaceships(l_player_grid, message, win):
    l_ships = [["A","A","A","A","A",],["B","B","B","B"],["C","C","C"],["D","D","D"],["E","E"]]
    message.setText("You have five ships. Click your board to place them and then click the highlighted direction you want the ship to be oriented.")
    for l_ship in l_ships:
        temp1 = Text(Point(450,530), "Currently placing ship " + l_ship[0] + ", which is " + str(len(l_ship)) + " units long.")
        temp1.draw(win)
        click = True
        while click != False:
            click = win.getMouse()
            while click.getX() < 490 or click.getX() >= 890 or click.getY() < 80 or click.getY() >= 480: # Checking if click is not on own board
                message.setText("Click on your own board.")
                click = win.getMouse()
            message.setText("You have five ships. Click your board to place them and then click the highlighted direction you want the ship to be oriented.")
            b_valid, l_player_grid = getsquare(click.getX(), click.getY(), l_player_grid, l_ship, win)
            while b_valid == False:
                message.setText("Oops, can't place that there. Try again!")
                click = win.getMouse()
                b_valid, l_player_grid = getsquare(click.getX(), click.getY(), l_player_grid, l_ship, win)
            message.setText("You have five ships. Click your board to place them and then click the highlighted direction you want the ship to be oriented.")
            if b_valid == True:
                click = False
            temp1.undraw()
    message.setText("All done placing ships! Click to continue.")
    win.getMouse()
    message.setText("")
    return l_player_grid

def createboard():
    win = GraphWin("Battleship", 900, 550)
    message = Text(Point(450,510), "Currently loading, please wait...")
    message.draw(win)
    l_comp_grid = creategrid(40,80,win, "Computer")
    l_comp_grid = compplaceships(l_comp_grid)
    l_player_grid = creategrid(490,80,win, "You")
    l_player_grid = playerplaceships(l_player_grid, message, win)
    return win, l_comp_grid, l_player_grid, message

def checkhit(x, y, l_grid, message, win):
    i_row = 0
    b_fire_again = True
    b_on_board = False
    for l_row in l_grid:
        i_col = 0
        for s_value in l_row:
            if x > (40+i_col*40) and x < (40+40+i_col*40) and y > (80+i_row*40) and y < (80+40+i_row*40):
                if s_value != "_":
                    if s_value == "H" or s_value == "M":
                        message.setText("You've already fired there! Pick a different spot.")
                        b_fire_again = True
                    else:
                        message.setText("Hit! Shoot again!")
                        l_grid[i_row][i_col] = "H"
                        Rectangle(Point(40+i_col*40,80+i_row*40), Point(40+40+i_col*40,80+40+i_row*40)).draw(win).setFill("#fbb")
                        b_fire_again = True
                else:
                    message.setText("Missed!")
                    l_grid[i_row][i_col] = "M"
                    Rectangle(Point(40+i_col*40,80+i_row*40), Point(40+40+i_col*40,80+40+i_row*40)).draw(win).setFill("#bbf")
                    b_fire_again = False
                b_on_board = True
            i_col += 1
        i_row += 1
    if b_on_board == False:
        message.setText("Click on your own board, please! Shoot again.")
    return l_grid, b_fire_again

def redraw(l_player_grid, win):
    i_row = 0
    for l_row in l_player_grid:
        i_col = 0
        for s_value in l_row:
            if s_value != "_":
                Text(Point(490+20+i_col*40, 80+20+i_row*40), s_value).draw(win).setSize(20)
            i_col += 1
        i_row += 1

def compfire(l_computer_shots, l_player_grid, win): # Check why the lists are copying each other
    b_valid = False
    while b_valid == False:
        i_random_x = random.randint(0,9)
        i_random_y = random.randint(0,9)
        if l_computer_shots[i_random_y][i_random_x] != "_":
            if l_computer_shots[i_random_y][i_random_x] == "H" or l_computer_shots[i_random_y][i_random_x] == "M":
                b_valid = False
            else:
                l_computer_shots[i_random_y][i_random_x] = "H"
                Rectangle(Point(490+i_random_x*40,80+i_random_y*40), Point(490+40+i_random_x*40,80+40+i_random_y*40)).draw(win).setFill("#fbb")
                redraw(l_player_grid, win)
                b_valid = True
                b_hit = True
        else:
            l_computer_shots[i_random_y][i_random_x] = "M"
            Rectangle(Point(490+i_random_x*40,80+i_random_y*40), Point(490+40+i_random_x*40,80+40+i_random_y*40)).draw(win).setFill("#bbf")
            b_valid = True
            b_hit = False
    return l_computer_shots, b_hit

def play(l_comp_grid, l_player_grid, message, win):
    b_player_win = False
    b_comp_win = False
    i_turn = 0
    l_computer_shots = []
    for l_row in l_player_grid: # Creating a copy for redrawing letters. Might be better shorthand somewhere
        l_buffer = []
        for s_value in l_row:
            l_buffer.append(s_value)
        l_computer_shots.append(l_buffer)
    b_infoA = False
    b_infoB = False
    b_infoC = False
    b_infoD = False
    b_infoE = False
    while b_player_win == False and b_comp_win == False:
        if i_turn % 2 == 0: # Player's turn
            message.setText("Your turn. Click a square on the computer's board to fire!")
            click = True
            b_fire_again = True
            while click != False and b_fire_again == True:
                click = win.getMouse()
                l_comp_grid, b_fire_again = checkhit(click.getX(), click.getY(), l_comp_grid, message, win)
                b_player_win = True
                for l_row in l_comp_grid:
                    for s_value in l_row:
                        if s_value != "H" and s_value != "M" and s_value != "_":
                            b_player_win = False
                if b_player_win == True:
                    click = False
                # Informing the player if a ship is sunk, only doing it once
                b_sunkA = True
                b_sunkB = True
                b_sunkC = True
                b_sunkD = True
                b_sunkE = True
                for l_row in l_comp_grid:
                    # print(l_row) Debug code, uncomment to see computer's grid
                    if "A" in l_row:
                        b_sunkA = False
                    if "B" in l_row:
                        b_sunkB = False
                    if "C" in l_row:
                        b_sunkC = False
                    if "D" in l_row:
                        b_sunkD = False
                    if "E" in l_row:
                        b_sunkE = False
                if b_infoA == False and b_sunkA == True:
                    popup = GraphWin("!", 600, 100)
                    Text(Point(300,50), "You sunk the computer's A ship (5 units long)!").draw(popup).setSize(20)
                    Text(Point(300,90), "Click to close.").draw(popup)
                    popup.getMouse()
                    popup.close()
                    b_infoA = True
                if b_infoB == False and b_sunkB == True:
                    popup = GraphWin("!", 600, 100)
                    Text(Point(300,50), "You sunk the computer's B ship (4 units long)!").draw(popup).setSize(20)
                    Text(Point(300,90), "Click to close.").draw(popup)
                    popup.getMouse()
                    popup.close()
                    b_infoB = True
                if b_infoC == False and b_sunkC == True:
                    popup = GraphWin("!", 600, 100)
                    Text(Point(300,50), "You sunk the computer's C ship (3 units long)!").draw(popup).setSize(20)
                    Text(Point(300,90), "Click to close.").draw(popup)
                    popup.getMouse()
                    popup.close()
                    b_infoC = True
                if b_infoD == False and b_sunkD == True:
                    popup = GraphWin("!", 600, 100)
                    Text(Point(300,50), "You sunk the computer's D ship (3 units long)!").draw(popup).setSize(20)
                    Text(Point(300,90), "Click to close.").draw(popup)
                    popup.getMouse()
                    popup.close()
                    b_infoD = True
                if b_infoE == False and b_sunkE == True:
                    popup = GraphWin("!", 600, 100)
                    Text(Point(300,50), "You sunk the computer's E ship (2 units long)!").draw(popup).setSize(20)
                    Text(Point(300,90), "Click to close.").draw(popup)
                    popup.getMouse()
                    popup.close()
                    b_infoE = True
                # Checking if player won
                b_player_win = True
                for l_row in l_comp_grid:
                    for s_value in l_row:
                        if s_value != "H" and s_value != "M" and s_value != "_":
                            b_player_win = False
        else: # Computer's turn
            l_computer_shots, b_hit = compfire(l_computer_shots, l_player_grid, win)
            while b_hit == True: # Let computer fire again
                l_computer_shots, b_hit = compfire(l_computer_shots, l_player_grid, win)
            # Checking if computer wins
            b_comp_win = True
            for l_row in l_computer_shots:
                for s_value in l_row:
                    if s_value != "H" and s_value != "M" and s_value != "_":
                        b_comp_win = False
        i_turn += 1
    return b_player_win, b_comp_win

def main():
    win, l_comp_grid, l_player_grid, message = createboard()
    b_player_win, b_comp_win = play(l_comp_grid, l_player_grid, message, win)
    if b_player_win == True:
        popup = GraphWin("!", 600, 100)
        Text(Point(300,50), "You won! Great job.").draw(popup).setSize(20)
        Text(Point(300,90), "Click to close.").draw(popup)
        popup.getMouse()
        popup.close()
    if b_comp_win == True:
        popup = GraphWin("!", 600, 100)
        Text(Point(300,50), "You lost... Next time, maybe!").draw(popup).setSize(20)
        Text(Point(300,90), "Click to close.").draw(popup)
        popup.getMouse()
        popup.close()
main()
