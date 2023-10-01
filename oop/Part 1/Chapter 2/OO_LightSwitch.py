
class LightSwitch():
    def __init__(self):
        self.switchIsOn = False
        
    
    def turnOn(self):
        self.switchIsOn = True
        
    
    def turnOff(self):
        self.switchIsOn = False
        
    
    def show(self):
        print("The switch is", self.switchIsOn)


if __name__ == '__main__':
    oLightSwitch = LightSwitch()
    oLightSwitch.turnOn()
    oLightSwitch.show()
    