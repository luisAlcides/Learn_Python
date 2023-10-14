# Timer lass
from pygame import time


class Timer:

    def __init__(self, timeInSeconds, nickname=None, callback=None):
        self.timeInSeconds = timeInSeconds
        self.nickname = nickname
        self.callback = callback
        self.savedSecondsElapsed = 0.0
        self.running = False

    def start(self, newTimeInSeconds=None):
        if newTimeInSeconds != None:
            self.timeInSeconds = newTimeInSeconds
        self.running = True
        self.startTime = time.time()

    def update(self):
        if not self.running:
            return False
        self.savedSecondsElapsed = time.time() - self.startTime

        if self.savedSecondsElapsed < self.timeInSeconds:
            return False  # running but hasn't reached limit

        else:  # timer has finished
            self.running = False
            if self.callBack is not None:
                self.callBack(self.nickname)
            return True  # True here means that the timer has ended

    def getTime(self):
        if self.running:
            self.savedSecondsElapsed = time.time() - self.startTime

        return self.savedSecondsElapsed

    def stop(self):
        self.getTime()  # remembers final
        self.running = False
