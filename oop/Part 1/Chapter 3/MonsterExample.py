import random

class Monster:
    def __init__(self, nRows, nCols, maxSpeed):
        self.nRows = nRows 
        self.nCols = nCols
        self.myRow = random.randrange(self.nRows) # chooses a random row
        self.myCol = random.randrange(self.nCols) # chooses a random column
        self.mySpeedX = random.randrange(-maxSpeed, maxSpeed + 1)
        self.mySpeedY = random.randrange(-maxSpeed, maxSpeed + 1)
        
    
    def move(self):
        self.myRow = (self.myRow + self.mySpeedY) % self.nRows
        self.myCol = (self.myCol + self.mySpeedX) % self.nCols


if __name__=='__main__':
    N_MONSTERS = 20
    N_ROWS = 100
    N_COLS = 200
    MAX_SPEED = 5
    monsterList = []
    
    for i in range(N_MONSTERS):
        monsterList.append(Monster(N_ROWS, N_COLS, MAX_SPEED))
    
    for monster in monsterList:
        monster.move()