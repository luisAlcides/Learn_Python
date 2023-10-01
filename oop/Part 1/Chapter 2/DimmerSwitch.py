class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0
        
    
    def turnOn(self):
        self.switchIsOn = True
        
    
    def turnOff(self):
        self.switchIsOn = False
        
    
    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1
            
    
    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1
            
            
    def show(self):
        print("The switch is", self.switchIsOn)
        if self.switchIsOn:
            print("The brightness level is", self.brightness)
        else:
            print("The brightness level is 0")
        
        

if __name__ == '__main__':
    oDimmer =  DimmerSwitch()
    
    oDimmer.turnOn()
    oDimmer.raiseLevel()
    oDimmer.raiseLevel()
    oDimmer.show()