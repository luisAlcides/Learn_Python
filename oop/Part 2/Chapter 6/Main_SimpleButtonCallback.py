import pygame, sys
from pygame.locals import *
from SimpleButton import *


GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

# Define a function to be used as a "callback"
def myCallBackFunction():
    print('User pressed Button B, called myCallBackFucntion')
    


# Defina a class with a method to be used as a "callback"
class CallBackTest:
    # snipped any othher methods in this class
    
    def myMethod(self):
        print('User pressed ButtonC, called myMethod of the CallBackTest object')
        
    
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

callBackTest = CallBackTest()

buttonA = SimpleButton(window, (20, 20), 'images/buttonAUp.png', 'images/buttonADown.png')

# specifying a function to call back
buttonB = SimpleButton(window, (200, 20), 'images/buttonBUp.png', 'images/buttonBDown.png', callback=myCallBackFunction)

# specifying a function to call back
buttonC = SimpleButton(window, (150, 60), 'images/buttonCUp.png', 'images/buttonCDown.png', callback=callBackTest.myMethod)

counter = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        
        # Pass the event to the button, see if it has been clicked on
        if buttonA.handleEvent(event):
            print('User pressed button A, handled in the main loop')
            
        # ButtonB and buttonC have callback
        # no need tocheck result of these calls
        buttonB.handleEvent(event)
        buttonC.handleEvent(event)
    
    counter += 1
    window.fill(GRAY)
    
    buttonA.draw()
    buttonB.draw()
    buttonC.draw()
    
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)        
