import pygame
import random

# Define variables for game
kFPS = 60

# Size of window
kWindowHeight = 200
kWindowWidth = 500

# Size of paddle
kPaddleWidth = 50
kPaddleHeight = 60
kPaddlePadding = 10

# Size of ball
kBallWidth = 10
kBallHeight = 10

# Speed of paddle
kPaddleSpeed = 2

# Speed of ball
kBallXSpeed = 5
kBallYSpeed = 5

# RGB colors of paddle and ball
kWhiteColor = (255, 255, 255)
kBlackColor = (0, 0, 0)

# Initialize our screen
screen = pygame.display.set_mode((kWindowWidth, kWindowHeight))

def drawBall(ballXPosition, ballYPosition):
	ball = pygame.Rect(ballXPosition, ballYPosition, kBallWidth, kBallHeight)
	pygame.draw.rect(screen, kWhiteColor, ball)

def drawPaddle1(paddle1XPosition, paddle1YPosition):
	paddle1 = pygame.Rect(paddle1XPosition, paddle1YPosition, kPaddleWidth, kPaddleHeight)
	pygame.draw.rect(screen, kWhiteColor, paddle1)

def drawPaddle2(paddle2YPosition):
	paddle2 = pygame.Rect(kWindowWidth - kPaddlePadding - kPaddleWidth, paddle2YPosition, kPaddleWidth, kPaddleHeight)
	pygame.draw.rect(screen, kWhiteColor, paddle2)


def updateBall(paddle1YPosition, paddle2YPosition, ballXPosition, ballYPosition, ballXDirection, ballYDirection, action):

	# Update X and Y position
	ballXPosition += ballXDirection * kBallXSpeed
	ballYPosition += ballYDirection * kBallYSpeed

	# Update score
	score = 0

	# Check for a collision, if the ball hits the left side then switch direction
	if (ballXPosition <= 0):
		ballXDirection = 1
		score = -1

	# Check for a collision, if the ball hits the right side then switch direction
	elif (ballXPosition >= kWindowWidth - kBallWidth):
		ballXDirection = -1
		score = 1

	# Check for a collision, if the ball hits the left side then switch direction
	if (ballYPosition <= 0):
		ballYDirection = -1
		score = -1

	# Check for a collision, if the ball hits the right side then switch direction
	elif (ballYPosition >= kWindowHeight - kBallHeight):
		ballYDirection = 1
		score = 1

	if (action == 0):
		ballYDirection = 1
	else:
		ballYDirection = -1

	return [ score, paddle1YPosition, paddle2YPosition, ballXPosition, ballYPosition, ballXDirection, ballYDirection ]

def drawColor(x, y, color):

	if (color > 0):
		print(color)

	coloredPixel = pygame.Rect(x * kBallXSpeed, y * kBallYSpeed, kBallXSpeed, kBallYSpeed)
	
	if color >= 0:
		rgb = min(color, 255)
		pygame.draw.rect(screen, (0, rgb, 0), coloredPixel)
	else:
		rgb = max(abs(color), 255)
		pygame.draw.rect(screen, (rgb, 0, 0), coloredPixel)

def drawColoredPixels(Matrix):

	for i in range(0, kWindowWidth / kBallXSpeed):
		for j in range(0, kWindowHeight / kBallYSpeed):

			# print(i, j, Matrix[i][j][0])

			drawColor(i, j, Matrix[i][j][0] + Matrix[i][j][1])

class PongGame:
	def __init__(self):
		
		# Keep score
		self.tally = 0

		# Initialize positions of paddle
		self.paddle1XPosition = kWindowWidth/2 - kPaddleWidth/2
		self.paddle1YPosition = kWindowHeight/2 - kPaddleHeight/2
		self.paddle2YPosition = kWindowHeight/2 - kPaddleHeight/2

		# Ball direction definition
		self.ballXDirection = 1
		self.ballYDirection = 1

		# Starting point
		self.ballXPosition = 0
		self.ballYPosition = kWindowHeight/2 - kBallHeight/2

		h, a, w = kWindowWidth / kBallXSpeed, kWindowHeight/ kBallYSpeed, 2;
		self.localMatrix = [[[0 for x in range(w)] for y in range(a)] for z in range(h)]

		self.action = 0

	def resetBall(self):
		# Starting point
		self.ballXPosition = 0
		self.ballYPosition = kWindowHeight/2 - kBallHeight/2		

	def getWindowWidthAndBallXSpeed(self):

		return [ kWindowWidth, kBallXSpeed ]

	def getWindowHeightAndBallYSpeed(self):

		return [ kWindowHeight, kBallYSpeed ]

	def getGameOver(self):

		# Check for a collision, if the ball hits the left side then switch direction
		if (self.ballYPosition <= 0 or self.ballYPosition >= kWindowHeight - kBallHeight):
			return True
		else:
			return False

	def updateMatrix(self, Matrix):
		self.localMatrix = Matrix
		# print(Matrix)

	def getNextFrame(self, action):
		pygame.event.pump()
		score = 0

		drawColoredPixels(self.localMatrix)
		
		# self.paddle1YPosition = updatePaddle1(action, self.paddle1YPosition)
		drawPaddle1(self.paddle1XPosition, self.paddle1YPosition)
		
		# self.paddle2YPosition = updatePaddle2(self.paddle2YPosition, self.ballYPosition)
		# drawPaddle2(self.paddle2YPosition)

		# Update variables by updating ball position
		[score, self.paddle1YPosition, self.paddle2YPosition, self.ballXPosition, self.ballYPosition, self.ballXDirection, self.ballYDirection] = updateBall(self.paddle1YPosition, self.paddle2YPosition, self.ballXPosition, self.ballYPosition, self.ballXDirection, self.ballYDirection, action)

		drawBall(self.ballXPosition, self.ballYPosition)

		imageData = pygame.surfarray.array3d(pygame.display.get_surface())
		pygame.display.flip()

		self.tally += score

		# print "Tally is " + str(self.tally)

		return [self.ballXDirection, self.ballYDirection, kPaddleWidth, kPaddleHeight, kBallWidth, kBallHeight, self.paddle1XPosition, self.paddle1YPosition, self.ballXPosition, self.ballYPosition]





















