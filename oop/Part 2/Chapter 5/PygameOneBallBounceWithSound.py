# pygame demo 4 - one image, bounce around the window using (x, y) coords

import pygame, sys, random
from pygame.locals import *


BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

ballImage = pygame.image.load('images/ball.png')
bounceSound = pygame.mixer.Sound('sounds/bounce.wav')
pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.play(-1, 0.0)

ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if (ballX < 0 ) or (ballX >= MAX_WIDTH):
        xSpeed = -xSpeed
        bounceSound.play()
        
    if (ballY < 0) or (ballY >= MAX_HEIGHT):
        ySpeed = -ySpeed
        bounceSound.play()
        
    
    ballX += xSpeed
    ballY += ySpeed
    
    window.fill(BLACK)
    
    window.blit(ballImage, (ballX, ballY))
    
    pygame.display.update()
    
    clock.tick(FRAMES_PER_SECOND)