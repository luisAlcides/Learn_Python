class TV:
    def __init__(self):
        self.isOn = False
        self.isMuted = False
        # Some default list of channels
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44,54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 100
        self.volume = self.VOLUME_MAXIMUM
        
    
    def power(self):
        self.isOn = not self.isOn # toggle
        
    
    def volumeUp(self):
        if not self.isOn:
            return 
        if self.isMuted:
            self.isMuted = False
            
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1
            
    
    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False # changing the volume while muted unmutes the sound
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1
            
    
    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0 # wrap around to the first channel
            
    
    def channelDown(self):
        if not self.isOn:
            return
        
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1 # wrap around to the top channel
            
    
    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted
        
    
    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel) # if the newChannel is not in our list of channels, don't do anything
            
            
    def showInfo(self):
        print()
        print('TV Status:')
        if self.isOn:
            print(' TV is: On')
            print(' Channel is:', self.channelList[self.channelIndex])
            if self.isMuted:
                print(' Volume is:', self.volume, '(sound is muted)')
            else:
                print(' Volume is:', self.volume)
        else:
            print(' TV is: Off')    
            
            

if __name__ == '__main__':
    # Two TV objects with calls to their methods
    tv1 = TV() # create a TV object
    tv2 = TV() # create another TV object
    
    # Turn both TVs on
    tv1.power()
    tv2.power()
    
    # Raise the volume of tv1
    tv1.volumeUp()
    tv1.volumeUp()
    
    # Raise the volume of tv2
    tv2.volumeUp()
    tv2.volumeUp()
    tv2.volumeUp()
    tv2.volumeUp()
    
    # Change TV2's channel, the mute it
    tv2.setChannel(44)
    tv2.mute()
    
    # Now display both TVs
    tv1.showInfo()
    tv2.showInfo() 