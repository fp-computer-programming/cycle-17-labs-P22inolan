# Author: IBN (AMDG) 4/12/2022

class TV_remote:
    """ TV_remote class represents a TV remote """

    def __init__(self, channel=0, volume_level=0, on=False):
        """ Create a new TV remote with channel 0, volume level 0, off """
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
    
    def __str__(self):
        "Returns a string of the attributes of the tv remote "
        return " The channel is {0}, the volume is {1}, and the TV being on is {2}".format(self.channel, self.volume_level, self.on)
    
    def turn_on(self):
        """ turns the tv on """
        self.on = True
    
    def turn_off(self):
        """ turns the tv off """
        self.on = False
    
    def volume_up(self):
        """ turns the volume up 1 """
        self.volume_level += 1
    
    def volume_down(self):
        """ turns the volume down 1 """
        self.volume_level -= 1
    
    def channel_up(self):
        """ changes the channel up 1 """
        self.channel += 1
    
    def channel_down(self):
        """ changes the channel down 1 """
        self.channel -= 1

my_remote = TV_remote()
my_remote.channel_up()
my_remote.turn_on()
my_remote.volume_up()
print(my_remote)
