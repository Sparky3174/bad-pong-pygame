import pygame

class GameEntity:
    def __init__(self, centerX, centerY, width, height, color):
        self.color = color
        self.entityRect = pygame.Rect(centerX - width/2, centerY- height/2, width, height)
    def updateEntityPosition(self, amountX, amountY):
        self.entityRect.x += amountX
        self.entityRect.y += amountY
    def drawEntity(self, screen):
        pygame.draw.rect(screen, self.color, self.entityRect)