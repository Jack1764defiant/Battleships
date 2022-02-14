X = 10
Y = 10
score = 0
lives = 17
player = Rect(0, 0, 50, 50)
enemy = Rect(500, 500, 50, 50)
compshots = []
bricks = []
backboard = []
fired = []
pfired = False
cbricks = []
cbackboard = []
cfired = []
from random import randint
from time import *
WIDTH =1000
HEIGHT=500
state = "playing"
nextshots = []
for x in range(0, X):
    for y in range(0, Y):
        brick = Rect(x*50,y*50, 50, 50)
        bricks.append(brick)
        fired.append("no")
for x in range(0, X):
    for y in range(0, Y):
        backboard.append("X")

for x in range(0, X):
    for y in range(0, Y):
        cbrick = Rect(x*50 + 500, y*50, 50, 50)
        cbricks.append(cbrick)
        cfired.append("no")
for x in range(0, X):
    for y in range(0, Y):
        cbackboard.append("X")

def shipSpawn(length):
    if randint(1,2) == 1:
        aship_row = randint(0,(8-length))
        aship_col = randint(0,9)
        while (backboard[aship_row + aship_col*10] == "!") or (backboard[(aship_row + 1) + aship_col*10] == "!") or (backboard[(aship_row + 2) + aship_col*10] == "!" and length > 2) or (backboard[(aship_row + 3) + aship_col*10] == "!" and length > 3)or (backboard[(aship_row +4) + aship_col*10] == "!" and length > 4):
            aship_row = randint(0,(8-length))
            aship_col = randint(0,9)
        backboard[aship_row + aship_col*10] = "!"

        aship_row2 = aship_row+1
        aship_col2 = aship_col
        backboard[aship_row2 + aship_col2*10] = "!"

        if length > 2:
            aship_row3 = aship_row+2
            aship_col3 = aship_col
            backboard[aship_row3 + aship_col3*10] = "!"

        if length > 3:
            aship_row4 = aship_row+3
            aship_col4 = aship_col
            backboard[aship_row4 + aship_col4*10] = "!"

        if length > 4:
            aship_row5 = aship_row+4
            aship_col5 = aship_col
            backboard[aship_row5 + aship_col5*10] = "!"

    else:
        aship_row = randint(0, 9)
        aship_col = randint(0,(8-length))
        while (backboard[aship_row + aship_col*10] == "!") or (backboard[aship_row + (aship_col+1)*10] == "!") or (backboard[aship_row + (aship_col+2)*10] == "!" and length > 2) or (backboard[aship_row + (aship_col+3)*10] == "!" and length > 3) or (backboard[aship_row + (aship_col+4)*10] == "!" and length > 4):
            aship_row = randint(0,9)
            aship_col = randint(0,(8-length))
        backboard[aship_row + aship_col*10] = "!"

        aship_row2 = aship_row
        aship_col2 = aship_col+1
        backboard[aship_row2 + aship_col2*10] = "!"

        if length > 2:
            aship_row3 = aship_row
            aship_col3 = aship_col+2
            backboard[aship_row3 + aship_col3*10] = "!"

        if length > 3:
            aship_row4 = aship_row
            aship_col4 = aship_col+3
            backboard[aship_row4 + aship_col4*10] = "!"

        if length > 4:
            aship_row5 = aship_row
            aship_col5 = aship_col+4
            backboard[aship_row5 + aship_col5*10] = "!"

def pshipSpawn(length):
    if randint(1,2) == 1:
        aship_row = randint(0,(8-length))
        aship_col = randint(0,9)
        while (cbackboard[aship_row + aship_col*10] == "!") or (cbackboard[(aship_row + 1) + aship_col*10] == "!") or (cbackboard[(aship_row + 2) + aship_col*10] == "!" and length > 2) or (cbackboard[(aship_row + 3) + aship_col*10] == "!" and length > 3)or (cbackboard[(aship_row +4) + aship_col*10] == "!" and length > 4):
            aship_row = randint(0,(8-length))
            aship_col = randint(0,9)
        cbackboard[aship_row + aship_col*10] = "!"

        aship_row2 = aship_row+1
        aship_col2 = aship_col
        cbackboard[aship_row2 + aship_col2*10] = "!"

        if length > 2:
            aship_row3 = aship_row+2
            aship_col3 = aship_col
            cbackboard[aship_row3 + aship_col3*10] = "!"

        if length > 3:
            aship_row4 = aship_row+3
            aship_col4 = aship_col
            cbackboard[aship_row4 + aship_col4*10] = "!"

        if length > 4:
            aship_row5 = aship_row+4
            aship_col5 = aship_col
            cbackboard[aship_row5 + aship_col5*10] = "!"

    else:
        aship_row = randint(0, 9)
        aship_col = randint(0,(8-length))
        while (cbackboard[aship_row + aship_col*10] == "!") or (cbackboard[aship_row + (aship_col+1)*10] == "!") or (cbackboard[aship_row + (aship_col+2)*10] == "!" and length > 2) or (cbackboard[aship_row + (aship_col+3)*10] == "!" and length > 3) or (cbackboard[aship_row + (aship_col+4)*10] == "!" and length > 4):
            aship_row = randint(0,9)
            aship_col = randint(0,(8-length))
        cbackboard[aship_row + aship_col*10] = "!"

        aship_row2 = aship_row
        aship_col2 = aship_col+1
        cbackboard[aship_row2 + aship_col2*10] = "!"

        if length > 2:
            aship_row3 = aship_row
            aship_col3 = aship_col+2
            cbackboard[aship_row3 + aship_col3*10] = "!"

        if length > 3:
            aship_row4 = aship_row
            aship_col4 = aship_col+3
            cbackboard[aship_row4 + aship_col4*10] = "!"

        if length > 4:
            aship_row5 = aship_row
            aship_col5 = aship_col+4
            cbackboard[aship_row5 + aship_col5*10] = "!"
shipSpawn(2)
shipSpawn(3)
shipSpawn(3)
shipSpawn(4)
shipSpawn(5)
pshipSpawn(2)
pshipSpawn(3)
pshipSpawn(3)
pshipSpawn(4)
pshipSpawn(5)

sremaining = 0
for i in range(0, len(backboard)):
    if backboard[i] == "!" and fired[i] == "no":
        sremaining += 1
csremaining = 0
for i in range(0, len(cbackboard)):
    if cbackboard[i] == "!" and cfired[i] == "no":
        csremaining += 1
def draw():
    global state, sremaining
    remaining = 0
    cremaining = 0
    for i in range(0, len(backboard)):
        if backboard[i] == "!" and fired[i] == "no":
            remaining += 1
    for i in range(0, len(cbackboard)):
        if cbackboard[i] == "!" and cfired[i] == "no":
            cremaining += 1
    if remaining == 0 and cremaining > 0:
        screen.clear()
        crosshairs = Rect (0, 0, 500, 500)
        screen.draw.filled_rect(crosshairs, "yellow")
        screen.draw.filled_circle(crosshairs.center, 250, "red")
        screen.draw.filled_circle(crosshairs.center, 150, "orange")
        screen.draw.filled_circle(crosshairs.center, 80, "yellow")
        screen.draw.text("You Sunk My Battleships!", (550, 150), color = "green")
        screen.draw.text("You had " + str(cremaining) + " remaining.", (550, 200), color = "green")
        sounds.clapping.play()
    elif cremaining == 0:
        crosshairs = Rect (500, 0, 500, 500)
        screen.draw.filled_rect(crosshairs, "yellow")
        screen.draw.filled_circle(crosshairs.center, 250, "red")
        screen.draw.filled_circle(crosshairs.center, 150, "orange")
        screen.draw.filled_circle(crosshairs.center, 80, "yellow")
        screen.draw.text("Your Battleships Were Sunk!", (550, 150), color = "black")
        sleep(1)
        sounds.laugh.play()
        for i in range(0, len(fired)):
            fired[i] = "yes"
    if remaining > 0:
        screen.clear()
        for i in range(0, len(bricks)):
            if fired[i] == "no":
                screen.draw.filled_rect(bricks[i], "grey")
                screen.draw.circle(bricks[i].center, 25, "red")
                crosshairs = Rect (bricks[i].x, bricks[i].y + 25, 50, 1)
                screen.draw.filled_rect(crosshairs, "red")
                crosshairs = Rect (bricks[i].x + 25, bricks[i].y, 1, 50)
                screen.draw.filled_rect(crosshairs, "red")
                crosshairs = Rect (bricks[i].x, bricks[i].y, 50, 50)
                screen.draw.rect(crosshairs, "black")
            else:
                if backboard[i] == "!":
                    crosshairs = Rect (bricks[i].x, bricks[i].y, 50, 50)
                    screen.draw.filled_rect(crosshairs, "yellow")
                    screen.draw.filled_circle(bricks[i].center, 25, "red")
                    screen.draw.filled_circle(bricks[i].center, 13, "orange")
                    screen.draw.filled_circle(bricks[i].center, 7, "yellow")
                else:
                    screen.draw.filled_rect(bricks[i], "blue")
                    crosshairs = Rect (bricks[i].x, bricks[i].y, 50, 50)
                    screen.draw.rect(crosshairs, "black")
        if cremaining > 0:
            for i in range(0, len(cbricks)):
                if cfired[i] == "no":
                    screen.draw.filled_rect(cbricks[i], "grey")
                    screen.draw.circle(cbricks[i].center, 25, "red")
                    crosshairs = Rect (cbricks[i].x, cbricks[i].y + 25, 50, 1)
                    screen.draw.filled_rect(crosshairs, "red")
                    crosshairs = Rect (cbricks[i].x + 25, cbricks[i].y, 1, 50)
                    screen.draw.filled_rect(crosshairs, "red")
                    crosshairs = Rect (cbricks[i].x, cbricks[i].y, 50, 50)
                    screen.draw.rect(crosshairs, "black")
                else:
                    if cbackboard[i] == "!":
                        crosshairs = Rect (cbricks[i].x, cbricks[i].y, 50, 50)
                        screen.draw.filled_rect(crosshairs, "yellow")
                        screen.draw.filled_circle(cbricks[i].center, 25, "red")
                        screen.draw.filled_circle(cbricks[i].center, 13, "orange")
                        screen.draw.filled_circle(cbricks[i].center, 7, "yellow")
                    else:
                        screen.draw.filled_rect(cbricks[i], "blue")
                        crosshairs = Rect (cbricks[i].x, cbricks[i].y, 50, 50)
                        screen.draw.rect(crosshairs, "black")
        screen.draw.text("Your destroyed: " + str(csremaining-cremaining) + "/" + str(csremaining), (505, 5), color="black")
        split = Rect(498, 0, 4, 500)
        screen.draw.filled_rect(split, "white")
        screen.draw.circle(player.center, 25, "green")
        crosshairs = Rect (player.x, player.y + 25, 50, 1)
        screen.draw.filled_rect(crosshairs, "green")
        crosshairs = Rect (player.x + 25, player.y, 1, 50)
        screen.draw.filled_rect(crosshairs, "green")
        screen.draw.circle(enemy.center, 25, "green")
        crosshairs = Rect (enemy.x, enemy.y + 25, 50, 1)
        screen.draw.filled_rect(crosshairs, "green")
        crosshairs = Rect (enemy.x + 25, enemy.y, 1, 50)
        screen.draw.filled_rect(crosshairs, "green")
        screen.draw.text("Enemies destroyed: " + str(sremaining-remaining) + "/" + str(sremaining), (5, 5), color="black")

def update():
    global score, pfired, lives, nextshots, cremaining, remaining
    if True:
        if pfired == True:
            guess = randint(0, 99)
            while str(guess) in compshots:
                guess = randint(0, 99)
            if len(nextshots) > 0:
                guess = nextshots[0]
                nextshots.remove(guess)
            while str(guess) in compshots:
                if len(nextshots) > 0:
                    guess = nextshots[0]
                    nextshots.remove(guess)
                else:
                    guess = randint(0, 99)
            for i in range(0, len(cbackboard)-1):
                try:
                    if cbackboard[i] == "!" and cbackboard[i+1] == "!" and cfired[i] != "no" and cfired[i+1] != "no":
                        nextshots.insert(0, i+2)
                        nextshots.insert(0, i-1)
                        if i+2 in compshots:
                            nextshots.remove(i+2)
                        if i-1 in compshots:
                            nextshots.remove(i-1)
                    elif cbackboard[i] == "!" and cbackboard[i+10] == "!" and cfired[i] != "no" and cfired[i+1] != "no":
                        nextshots.insert(0, i+20)
                        nextshots.insert(0, i-10)
                        if i+20 in compshots:
                            nextshots.remove(i+20)
                        if i-10 in compshots:
                            nextshots.remove(i-10)
                except:
                    pass
            compshots.append(str(guess))
            enemy.x = cbricks[guess].x
            enemy.y = cbricks[guess].y
            #sleep(1.2)
            for i in range(0, len(cbricks)):
                    if cbricks[i].colliderect(enemy):
                        if cbackboard[i] == "!" and cfired[i] == "no":
                            lives -=1
                            sounds.kaboom.play()
                            nextshots = [guess-1, guess+1, guess + 10, guess-10]
                        else:
                            sounds.miss.play()
                        cfired[i] = "yes"
            pfired = False
            sleep(0.1)
        import pygame
        x, y = pygame.mouse.get_pos()
        player.x = x -25
        player.y = y -25
        player.x = int(50 * round(float(player.x)/50))
        player.y = int(50 * round(float(player.y)/50))
        if pygame.mouse.get_pressed()[0]:
            for i in range(0, len(bricks)):
                if bricks[i].colliderect(player):
                    if backboard[i] == "!" and fired[i] == "no":
                        score +=1
                        sounds.kaboom.play()
                    else:
                        sounds.miss.play()
                    if fired[i] == "no":
                        pfired = True
                    fired[i] = "yes"
