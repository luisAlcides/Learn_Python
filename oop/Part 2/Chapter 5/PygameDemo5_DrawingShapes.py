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
    
    window.fill(pygame.color.Color('black'))
    
    # Draw a box
    pygame.draw.line(window, pygame.color.Color('blue'), (20,20), (60,20), 4) # top
    pygame.draw.line(window, pygame.color.Color('blue'), (20, 20), (20, 60), 4) # left
    pygame.draw.line(window, pygame.color.Color('blue'), (20, 60), (60, 60), 4) # right
    pygame.draw.line(window, pygame.color.Color('blue'), (60, 20), (60, 60), 4) # bottom
    
    # Draw an X in the box
    pygame.draw.line(window, pygame.color.Color('blue'), (20, 20), (60, 60), 1)
    pygame.draw.line(window, pygame.color.Color('blue'), (20, 60), (60, 20), 1)
    
    # Draw a filled circle and an empty circle
    pygame.draw.circle(window, pygame.color.Color('green'), (250, 50), 30, 0) # filled
    pygame.draw.circle(window, pygame.color.Color('green'), (400, 50), 30, 2) # 2 pixel edge
    
    # Draw a filled rectangle and empty rectangle
    pygame.draw.rect(window, pygame.color.Color('red'), (250, 150, 100, 50), 0) # filled
    pygame.draw.rect(window, pygame.color.Color('red'), (400, 150, 100, 50), 1) # 1 pixel edge
    
    # Draw a filled ellipse and an empty ellipse
    pygame.draw.ellipse(window, pygame.color.Color('yellow'), (250, 250, 80, 400), 0) # filled
    pygame.draw.ellipse(window, pygame.color.Color('yellow'), (400, 250, 80, 40), 2) # 2 pixel edge
    
    # Draw a six-sided polygon
    pygame.draw.polygon(window, pygame.color.Color('purple'), ((240, 350), (350, 350), (410, 410), (350, 470), (240, 470), (170, 410)))
    
    # Draw an arc
    pygame.draw.arc(window, pygame.color.Color('blue'), (20, 400, 100, 100), 0, 2, 5)
    
    # Draw anti-aliased lines: a single line, then a list of points
    pygame.draw.aalines(window, pygame.color.Color('blue'), True, ((580, 400), (587, 450), (595, 460), (595, 460), (600, 444)), 1)
    
    pygame.display.update()
    
    clock.tick(FRAMES_PER_SECOND)
    
    # pygame.draw.aaline(window, color, startpos, endpos, blend=True)
    # pygame.draw.arc(window, color, rect, angle_start, angle_stop, width=0)
    # pygame.draw.circle(window, color, pos, radius, width=0)
    # pygame.draw.ellipse(window, color, rect, width=0)
    # pygame.draw.line(window, color, startpos, endpos, width=1)
    # pygame.draw.lines(window, color, closed, points, width=1)
    # pygame.draw.polygon(window, color, pointslist, width=0)
    # pygame.draw.rect(window, color, rect, width=0)


