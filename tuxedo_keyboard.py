# to set color to red :  sudo echo "0xFF0000" >> color_left
import os
from os import system

path = "/sys/devices/platform/tuxedo_keyboard/"
color_file = "color_left"
brightness_file = "brightness"
state_file = "state"

def rgb_to_hex(rgb):
        return '%02x%02x%02x' % rgb
def setcolor(color):
    os.system('echo "0x'+color+'" >> '+path+color_file)
def setgrightness(brightness):
    os.system('echo "'+str(brightness)+'" >> '+path+brightness_file)
def setcstate(state):
    os.system('echo "'+str(state)+'" >> '+path+state_file)


