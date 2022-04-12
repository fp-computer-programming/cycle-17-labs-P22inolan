# Author: IBN (AMDG) 4/12/2022

class TV_remote:
    """ TV_remote class represents a TV remote """

    def __init__(self, channel=0, volume_level=0, on=False):
        """ Create a new TV remote with channel 0, volume level 0, off """
        self.channel = channel
        self.volume_level = volume_level
        self.on = on
    
    def __str__(self):
        "Returns a string of the attributes of the TV remote "
        return " The channel is {0}, the volume is {1}, and the TV being on is {2}".format(self.channel, self.volume_level, self.on)

my_remote = TV_remote()
print(my_remote)

