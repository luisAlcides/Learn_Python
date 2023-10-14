import sys

from pygame.locals import *
from Game import *
from Constants import *

# Constants


# Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()


# Load assets
background = pygwidgets.Image(window, (0, 0), 'images/background.png')
newGameButton = pygwidgets.TextButton(window, (20, 530), 'New Game', width=100, height=45)
higherButton = pygwidgets.TextButton(window, (540, 520), 'Higher', width=120, height=55)
lowerButton = pygwidgets.TextButton(window, (340, 520), 'Lower', width=120, height=55)
quitButton = pygwidgets.TextButton(window, (880, 530), 'Quit', width=100, height=45)

# Initialize variables
game = Game(window)

# Loop forever
while True:
    # Check for handle event
    for event in pygame.event.get():
        if ((event.type == QUIT)
                or ((event.type == KEYDOWN) and (event.key == K_ESCAPE))
                or (quitButton.handleEvent(event))):
            pygame.quit()
            sys.exit()

        if newGameButton.handleEvent(event):
            game.reset()
            lowerButton.enable()
            higherButton.enable()

        if higherButton.handleEvent(event):
            gameOver = game.hitHigherOrLower(HIGHER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()
        if lowerButton.handleEvent(event):
            gameOver = game.hitHigherOrLower(LOWER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()

        # Clear the window
        background.draw()

        # draw the window elements
        # Tell the game to draw itself
        game.draw()
        # Draw remaining user interface components
        newGameButton.draw()
        higherButton.draw()
        lowerButton.draw()
        quitButton.draw()

        # update the window
        pygame.display.update()

        # slow  things down a bit
        clock.tick(FRAMES_PER_SECOND)