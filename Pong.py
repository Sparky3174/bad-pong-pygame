import pygame
import sys
from domain.gamePaddle import GamePaddle
from domain.gameBall import GameBall
from domain.scoreboard import ScoreBoard
from constants import *

pygame.init() #starts pygame

gameScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Makes a new window, returns a drawable "screen" derived from said window
pygame.display.set_caption("Pong!") # Names the new window "Pong!"
gameClock = pygame.time.Clock()

def initEntities():
    scoreBoard = ScoreBoard(gameScreen)

    playerOneMovementKeys = {"UP": getattr(pygame, "K_" + PLAYERONE_UP), "DOWN": getattr(pygame, "K_" + PLAYERONE_DOWN), "LEFT": getattr(pygame, "K_" + PLAYERONE_LEFT), "RIGHT": getattr(pygame, "K_" + PLAYERONE_RIGHT)}
    playerTwoMovementKeys = {"UP": getattr(pygame, "K_" + PLAYERTWO_UP), "DOWN": getattr(pygame, "K_" + PLAYERTWO_DOWN), "LEFT": getattr(pygame, "K_" + PLAYERTWO_LEFT), "RIGHT": getattr(pygame, "K_" + PLAYERTWO_RIGHT)}

    playerOnePaddle = GamePaddle((SCREEN_WIDTH/2) - (SCREEN_WIDTH / 3), (SCREEN_HEIGHT/2), 20, 100, PLAYERONE_COLOR, playerOneMovementKeys)
    playerTwoPaddle = GamePaddle((SCREEN_WIDTH/2) + (SCREEN_WIDTH / 3), (SCREEN_HEIGHT/2), 20, 100, PLAYERTWO_COLOR, playerTwoMovementKeys)
    print(f"playerOne pos: {playerOnePaddle.entityRect.center}")
    print(f"playerTwo pos: {playerTwoPaddle.entityRect.center}")

    gameBall = GameBall((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2), 10, 10, BALL_COLOR, [BALL_SPEED,BALL_SPEED])
    return playerOnePaddle, playerTwoPaddle, gameBall, scoreBoard

playerOnePaddle, playerTwoPaddle, gameBall, scoreBoard = initEntities()

def updateEntities(keysCurrentlyPressed):
    playerOnePaddle.movePaddleOnInput(keysCurrentlyPressed)
    playerTwoPaddle.movePaddleOnInput(keysCurrentlyPressed)

    gameBall.moveBall()
    gameBall.collisionCalc([playerOnePaddle.entityRect, playerTwoPaddle.entityRect], scoreBoard)

    playerOnePaddle.drawEntity(gameScreen)
    playerTwoPaddle.drawEntity(gameScreen)
    gameBall.drawEntity(gameScreen)
    
    
    
    scoreBoard.updateScorePoints("P0")


def pauseGame():
    gamePaused = True
    while gamePaused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == getattr(pygame, "K_" + PAUSE_KEY):
                gamePaused = False
                scoreBoard.playerWinner = "P0"
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

while True:
    gameScreen.fill("black") #Wipes current drawing from screen, prevents ghosting
    #scoreBoard.placeText(True, "center", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, "Test", "orange")

    if scoreBoard.playerWinner != "P0":
        scoreBoard.resetScoreBoard() #reset scoreBoard when a player wins
        pauseGame()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            pauseGame()
        
    keysCurrentlyPressed = pygame.key.get_pressed() # Get "pressed" status of all keys on keyboard as list
    updateEntities(keysCurrentlyPressed) # All entities perform their calculations & redraw to screen

    pygame.display.flip() #updates screen
    gameClock.tick(60) #waits 1/60th second (framerate limiter)