# to set color to red :  sudo echo "0xFF0000" >> color_left
import os
from os import system

path = "/sys/devices/platform/tuxedo_keyboard/leds/rgb:kbd_backlight"
color_file = "/multi_intensity"
brightness_file = "/brightness"

def rgb_to_hex(rgb):
        return '%02x%02x%02x' % rgb
def hex_to_rgb(hex):
        return tuple(int(hex[i:i+2], 16) for i in (0, 2 ,4))
def setcolor(color):
    os.system('echo '+color+' >> '+path+color_file)
def setgrightness(brightness):
    os.system('echo "'+str(brightness)+'" >> '+path+brightness_file)
#def setcstate(state):
#    os.system('echo "'+str(state)+'" >> '+path+state_file)


