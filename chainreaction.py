#By Idevrutahc@gmail.com
#-- --#
import pygame
import sys
from math import *

pygame.init()
#-- Keep grid in square dimensions --#
width = 480
height = 480
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#--RGB value to colors --#
background = (21, 25, 25)
border = (208, 211, 212)
red = (231, 30, 30)
white = (246, 246, 247)
violet = (170, 24, 232)
yellow = (252, 210, 42)
green = (27, 239, 69)

#--Customize player-color here  --1,2,3,4 --#
playerColor = [red, green, violet, yellow, white]

font = pygame.font.SysFont("Calibri", 33)

blocks = 40

noPlayers = 4

pygame.display.set_caption("Chain Reaction %d Player" % noPlayers)

score = []
for i in range(noPlayers):
    score.append(0)

players = []
for i in range(noPlayers):
    players.append(playerColor[i])

d = blocks//2 - 2

cols = int(width//blocks)
rows = int(height//blocks)

grid = []

# Quit or Close the Game Window
def close():
    pygame.quit()
    sys.exit()

# Class for Each Spot in Grid
class Spot():
    def __init__(self):
        self.color = border
        self.neighbors = []
        self.noAtoms = 0

    def addNeighbors(self, i, j):
        if i > 0:
            self.neighbors.append(grid[i - 1][j])
        if i < rows - 1:
            self.neighbors.append(grid[i + 1][j])
        if j < cols - 1:
            self.neighbors.append(grid[i][j + 1])
        if j > 0:
            self.neighbors.append(grid[i][j - 1])

# Make the Grid cells start with "Empty or 0"
def initializeGrid():
    global grid, score, players
    score = []
    for i in range(noPlayers):
        score.append(0)

    players = []
    for i in range(noPlayers):
        players.append(playerColor[i])

    grid = [[]for _ in range(cols)]
    for i in range(cols):
        for j in range(rows):
            newObj = Spot()
            grid[i].append(newObj)
    for i in range(cols):
        for j in range(rows):
            grid[i][j].addNeighbors(i, j)

# Draw the Grid in Pygame Window   
def drawGrid(currentIndex):
    r = 0
    c = 0
    for i in range(width//blocks):
        r += blocks
        c += blocks
        pygame.draw.line(display, players[currentIndex], (c, 0), (c, height))
        pygame.draw.line(display, players[currentIndex], (0, r), (width, r))

# Update grid / current grid view
def showPresentGrid(vibrate = 1):
    r = -blocks
    c = -blocks
    padding = 1
    for i in range(cols):
        r += blocks
        c = -blocks 
        for j in range(rows):
            c += blocks
            if grid[i][j].noAtoms == 0:
                grid[i][j].color = border
            elif grid[i][j].noAtoms == 1:
                pygame.draw.ellipse(display, grid[i][j].color, (r + blocks/2 - d/2 + vibrate, c + blocks/2 - d/2, d, d))
            elif grid[i][j].noAtoms == 2:
                pygame.draw.ellipse(display, grid[i][j].color, (r + 5, c + blocks/2 - d/2 - vibrate, d, d))
                pygame.draw.ellipse(display, grid[i][j].color, (r + d/2 + blocks/2 - d/2 + vibrate, c + blocks/2 - d/2, d, d))
            elif grid[i][j].noAtoms == 3:
                angle = 90
                x = r + (d/2)*cos(radians(angle)) + blocks/2 - d/2
                y = c + (d/2)*sin(radians(angle)) + blocks/2 - d/2
                pygame.draw.ellipse(display, grid[i][j].color, (x - vibrate, y, d, d))
                x = r + (d/2)*cos(radians(angle + 90)) + blocks/2 - d/2
                y = c + (d/2)*sin(radians(angle + 90)) + 5
                pygame.draw.ellipse(display, grid[i][j].color, (x + vibrate, y, d, d))
                x = r + (d/2)*cos(radians(angle - 90)) + blocks/2 - d/2
                y = c + (d/2)*sin(radians(angle - 90)) + 5
                pygame.draw.ellipse(display, grid[i][j].color, (x - vibrate, y, d, d))

    pygame.display.update()

# Increase the Atom when Clicked
def addAtom(i, j, color):
    grid[i][j].noAtoms += 1
    grid[i][j].color = color
    if grid[i][j].noAtoms >= len(grid[i][j].neighbors):
        overFlow(grid[i][j], color)
    
# Split the Atom when reaches the critical mass
def overFlow(cell, color):
    showPresentGrid()
    cell.noAtoms = 0
    for m in range(len(cell.neighbors)):
        cell.neighbors[m].noAtoms += 1
        cell.neighbors[m].color = color
        if cell.neighbors[m].noAtoms >= len(cell.neighbors[m].neighbors):
            overFlow(cell.neighbors[m], color)

# Checking if Any Player has WON!
def isPlayerInGame():
    global score
    playerScore = []
    for i in range(noPlayers):
        playerScore.append(0)
    for i in range(cols):
        for j in range(rows):
            for k in range(noPlayers):
                if grid[i][j].color == players[k]:
                    playerScore[k] += grid[i][j].noAtoms
    score = playerScore[:]

# GAME OVER
def gameOver(playerIndex):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    gameLoop()

        text = font.render("Player %d Won!" % (playerIndex + 1), True, white)
        text2 = font.render("Press \'r\' to Reset!", True, white)

        display.blit(text, (width/3, height/3))
        display.blit(text2, (width/3, height/2 ))

        pygame.display.update()
        clock.tick(60)


def checkWon():
    num = 0
    for i in range(noPlayers):
        if score[i] == 0:
            num += 1
    if num == noPlayers - 1:
        for i in range(noPlayers):
            if score[i]:
                return i

    return 9999

# Main Loop
def gameLoop():
    initializeGrid()
    loop = True

    turns = 0
    
    currentPlayer = 0

    vibrate = .5

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                i = x/blocks
                j = y/blocks
                if grid[int(i)][int(j)].color == players[currentPlayer] or grid[int(i)][int(j)].color == border:
                    turns += 1
                    addAtom(int(i), int(j), players[currentPlayer])
                    currentPlayer += 1
                    if currentPlayer >= noPlayers:
                        currentPlayer = 0
                if turns >= noPlayers:
                    isPlayerInGame()
                
        
        display.fill(background)
        # Vibrate the Atoms in their Cells
        drawGrid(currentPlayer)
        showPresentGrid(vibrate)
        
        pygame.display.update()

        res = checkWon()
        if res < 9999:
            gameOver(res)

        clock.tick(20)

gameLoop()      
