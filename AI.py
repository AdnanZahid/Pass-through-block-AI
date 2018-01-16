import Game
import random

def createGame():

    game = Game.PongGame()
    
    count = 0

    [ kWindowWidth, kBallXSpeed ] = game.getWindowWidthAndBallXSpeed()

    [ kWindowHeight, kBallYSpeed ] = game.getWindowHeightAndBallYSpeed()

    h, a, w = kWindowWidth / kBallXSpeed, kWindowHeight/ kBallYSpeed, 2;
    Matrix = [[[0 for x in range(w)] for y in range(a)] for z in range(h)]

    while(True):

        [ballXDirection, ballYDirection, kPaddleWidth, kPaddleHeight, kBallWidth, kBallHeight, paddle1XPosition, paddle1YPosition, ballXPosition, ballYPosition] = game.getNextFrame(game.action)

        bX1 = ballXPosition
        bX2 = ballXPosition + kBallWidth

        bY1 = ballYPosition
        bY2 = ballYPosition + kBallHeight

        pX1 = paddle1XPosition
        pX2 = paddle1XPosition + kPaddleWidth

        pY1 = paddle1YPosition
        pY2 = paddle1YPosition + kPaddleHeight

        count += 1

        xFrame = ballXPosition / kBallXSpeed
        yFrame = ballYPosition / kBallYSpeed

        action0 = Matrix[xFrame][yFrame][0]
        action1 = Matrix[xFrame][yFrame][1]

        if action0 == action1:
            game.action  = random.randint(0, 1)
        elif action0 > action1:
            game.action  = 0
        else:
            game.action  = 1

        if (not(bX2 < pX1 or bX1 > pX2 or bY2 < pY1 or bY1 > pY2)):
            Matrix[xFrame][yFrame][game.action] += 10

        if (not game.getGameOver()):
            Matrix[max(0, xFrame - ballXDirection)][max(0, yFrame - ballYDirection)][game.action] += Matrix[xFrame][yFrame][game.action] * 0.5

        else:
            Matrix[max(0, xFrame - ballXDirection)][max(0, yFrame - ballYDirection)][game.action] -= 10
            game.resetBall()
            # break

        # print(Matrix)
        game.updateMatrix(Matrix)

def main():
    createGame()

if __name__ == "__main__":
	main()






























