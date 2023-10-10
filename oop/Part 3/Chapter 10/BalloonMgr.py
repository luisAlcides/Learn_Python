# BalloonMgr class
import pygame
import random
from pygame.locals import *
import pygwidgets
from BalloonConstants import *
from Balloon import *


# BalloonMgr manages a list of Balloon objects
class BalloonMgr:
    def __init__(self, window, maxWidth, maxHeight):
        self.window = window
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.balloonList = None
        self.nPopped = None
        self.nMissed = None
        self.score = 0

    def start(self):
        self.balloonList = []
        self.nPopped = 0
        self.nMissed = 0
        self.score = 0

        for balloonNum in range(0, N_BALLOONS):
            randomBalloonClass = random.choice((BalloonSmall, BalloonMedium, BalloonLarge))
            balloon = randomBalloonClass(self.window, self.maxWidth, self.maxHeight, balloonNum)
            self.balloonList.append(balloon)

    def handleEvent(self, event):
        if event.type == MOUSEBUTTONDOWN:
            # Go 'reversed' so topmost balloon gets popped
            for balloon in reversed(self.balloonList):
                wasHit, nPoints = balloon.clickedInside(event.pos)
                if wasHit:
                    if nPoints > 0:  # remove this balloon
                        self.balloonList.remove(balloon)
                        self.nPopped = self.nPopped + 1
                        self.score = self.score + nPoints
                        return  # no need to check other

    def update(self):
        for balloon in self.balloonList:
            status = balloon.update()
            if status == BALLOON_MISSED:
                # Balloon went of the top, remove it
                self.balloonList.remove(balloon)
                self.nMissed = self.nMissed + 1

    def getScore(self):
        return self.score

    def getCountPopped(self):
        return self.nPopped

    def getCountMissed(self):
        return self.nMissed

    def draw(self):
        for balloon in self.balloonList:
            balloon.draw()
