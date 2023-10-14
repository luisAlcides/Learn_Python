import pyghelpers
import pygame
import sys
from pygwidgets import *

TIMER_LENGHT = 100
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Define your widgets
headerMessage = DisplayText(window, (100, 100), 'Header Message', fontSize=36, textColor=WHITE)
startButton = TextButton(window, (100, 200), text='Start', fontSize=24, width=120)
clickMeButton = TextButton(window, (100, 300), text='Click Me', fontSize=24, width=120)
timerMessage = DisplayText(window, (100, 400), 'Timer Message', fontSize=36, textColor=WHITE)

# Simple timer example
timer = pyghelpers.Timer(TIMER_LENGHT)  # create a Timer object

# Loop forever
while True:
    # Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if startButton.handleEvent(event):
            timer.start()  # start the timer
            startButton.disable()
            timerMessage.show()
            print('Starting timer')

        if clickMeButton.handleEvent(event):
            print('Other button was clicked')

    if timer.update():
        startButton.enable()
        timerMessage.hide()
        print('Timer ended')

    window.fill(WHITE)

    # draw all screen elements
    headerMessage.draw()
    startButton.draw()
    clickMeButton.draw()
    timerMessage.draw()

    # update the screen
    pygame.display.update()

    # slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
