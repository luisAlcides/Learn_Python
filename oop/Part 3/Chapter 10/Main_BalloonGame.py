# Balloon game main code

import sys, random, pygame, pygwidgets
from pygame.locals import *
from BallonMgr import *
from BalloonConstants import *

BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
PANEL_HEIGHT = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

scoreDisplay = pygwidgets.DisplayText(window, (10, USABLE_WINDOW_HEIGHT + 25), 'Score: 0',
                                      textColor=BLACK, backgroundColor=None, width=140, fontSize=24)
statusDisplay = pygwidgets.DisplayText(window, (180, USABLE_WINDOW_HEIGHT + 25), '',
                                       textColor=BLACK, backgroundColor=None, width=300, fontSize=24)
startButton = pygwidgets.TextButton(window, (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10), 'start')

balloonMgr = BalloonMgr(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)
playing = False  # wait until user clicks Start

while True:
    nPointsEarned = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if playing:
            balloonMgr.handleEvent(event)
            theScore = balloonMgr.getScore()
            scoreDisplay.setValue('Score: ' + str(theScore))
        elif startButton.handleEvent(event):
            balloonMgr.start()
            scoreDisplay.setValue('Score: 0')
            playing = True
            startButton.disable()

    if playing:
        balloonMgr.update()
        nPopped = balloonMgr.getCountPopped()
        nMissed = balloonMgr.getCountMissed()
        statusDisplay.setValue('Popped: ' + str(nPopped) + ' Missed: ' + str(nMissed) + ' Out of: ' + str(N_BALLOONS))

        if (nPopped + nMissed) == N_BALLOONS:
            playing = False
            startButton.enable()

    window.fill(BACKGROUND_COLOR)

    if playing:
        balloonMgr.draw()
    pygame.draw.rect(window, GRAY, pygame.Rect(0, USABLE_WINDOW_HEIGHT, WINDOW_WIDTH, PANEL_HEIGHT))
    scoreDisplay.draw()
    statusDisplay.draw()
    startButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)