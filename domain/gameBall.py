from domain.gameEntity import GameEntity
from constants import SCREEN_HEIGHT, SCREEN_WIDTH

class GameBall(GameEntity):
    def __init__(self, positionX, positionY, width, height, color, ballSpeed):
        super().__init__(positionX, positionY, width, height, color)
        self.ballSpeed = ballSpeed

    def isCollidingWithPaddle(self, gamePaddleList):
        for gamePaddle in gamePaddleList:
            if self.entityRect.colliderect(gamePaddle):
                print("hey, we collided")
                entityIntersection = self.entityRect.clip(gamePaddle) #get the overlapping area of the intersecting objects
                #if we collide horizontally, go opposite x. Otherwise, opposite y
                if entityIntersection.width < entityIntersection.height:
                    if (self.ballSpeed[0] > 0): #depending on the ball's movement direction make sure we push the ball outside of the paddle, snapping it to the outmost part of the paddle
                        self.entityRect.right = gamePaddle.left
                    else:
                        self.entityRect.left = gamePaddle.right
                    self.ballSpeed[0] = -self.ballSpeed[0]
                else: 
                    if (self.ballSpeed[1] > 0):
                        self.entityRect.bottom = gamePaddle.top - 7
                    else:
                        self.entityRect.top = gamePaddle.bottom + 7
                    self.ballSpeed[1] = -self.ballSpeed[1]

    def isCollidingWithScreen(self, scoreBoard):
        #left collision
        if self.entityRect.x < 0: 
            self.ballSpeed[0] = -self.ballSpeed[0]
            scoreBoard.updateScorePoints("P2")
        
        #top collision
        if self.entityRect.y < 0: 
            self.ballSpeed[1] = -self.ballSpeed[1]

        #right collision
        if self.entityRect.x + self.entityRect.width > SCREEN_WIDTH: 
            self.ballSpeed[0] = -self.ballSpeed[0]
            scoreBoard.updateScorePoints("P1")

        #bottom collision
        if self.entityRect.y + self.entityRect.height > SCREEN_HEIGHT: 
            self.ballSpeed[1] = -self.ballSpeed[1] 

    def collisionCalc(self, gamePaddleList, scoreBoard):
        self.isCollidingWithPaddle(gamePaddleList)
        self.isCollidingWithScreen(scoreBoard)

    def moveBall(self):
        self.updateEntityPosition(self.ballSpeed[0], self.ballSpeed[1])
        