import pygame
from domain.gameEntity import GameEntity
from constants import PADDLE_SPEED

class GamePaddle(GameEntity):
    def __init__(self, positionX, positionY, width, height, color, movementKeys):
        super().__init__(positionX, positionY, width, height, color)
        self.movementKeys = movementKeys

    def movePaddleOnInput(self, keysCurrentlyPressed):
        if keysCurrentlyPressed[self.movementKeys["UP"]]:
            self.updateEntityPosition(0, -PADDLE_SPEED)
        if keysCurrentlyPressed[self.movementKeys["DOWN"]]:
            self.updateEntityPosition(0, PADDLE_SPEED)

    def paddleWouldBePastCenter(self, direction):
        if self.color == "blue" and direction == "RIGHT" and self.entityRect.x + PADDLE_SPEED > 375:
            return True
        elif self.color == "red" and direction == "LEFT" and self.entityRect.x - PADDLE_SPEED < 404:
             return True
        else:
            return False