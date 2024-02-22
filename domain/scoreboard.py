import pygame
from constants import WINNING_SCORE, SCREEN_HEIGHT, SCREEN_WIDTH

class ScoreBoard():
    def __init__(self, gameScreen):
        self.hudFont = pygame.font.Font(None, 75)
        self.infoFont = pygame.font.Font(None, 50)
        self.playerOneScore = 0
        self.playerTwoScore = 0
        self.playerWinner = "P0"
        self.gameScreen = gameScreen

    def updateScorePoints(self, playerToRecievePoint):
        if playerToRecievePoint == "P1":
            self.playerOneScore += 1
        elif playerToRecievePoint == "P2":
            self.playerTwoScore += 1

        if self.playerOneScore == WINNING_SCORE:
            self.playerWinner = "P1"
        if self.playerTwoScore == WINNING_SCORE:
            self.playerWinner = "P2"
        
        self.refreshScoreText()


        if self.playerWinner in ["P1", "P2"]:
            print("whe")
            self.placeText(True, "center", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, f"{self.playerWinner} Win!", "white")
    
    def resetScoreBoard(self):
        self.playerOneScore = 0
        self.playerTwoScore = 0
        self.playerWinner = "P0"
        self.refreshScoreText()
        self.updateScorePoints("P0")

    def refreshScoreText(self):
        self.placeText(False, "left", 0, 0, f"{self.playerOneScore}", "white")
        self.placeText(False, "right", SCREEN_WIDTH, 0, f"{self.playerTwoScore}", "white")

    def placeText(self, useInfoFont, orientation, positionX, positionY, stringToPlace, color):
        if useInfoFont:
            renderedText = self.infoFont.render(stringToPlace, False, color)
        else:
            renderedText = self.hudFont.render(stringToPlace, False, color)

        if orientation == "center":
            self.gameScreen.blit(renderedText, (positionX - renderedText.get_width()/2, positionY - renderedText.get_height()/2)) #place center of text at given location
        elif orientation == "left":
            self.gameScreen.blit(renderedText, (positionX, positionY))
        else: #oriented to right
            self.gameScreen.blit(renderedText, (positionX - renderedText.get_width(), positionY))