##from sense_hat import SenseHat
##sense = SenseHat()
##sense.set_rotation = 180
from GetColor import get_color

def Ex5B():
    r_int = get_color("red")
    b_int = get_color("blue")
    g_int = get_color("green")
    msg_color = (r_int, b_int, g_int)
    ##sense.show_message("This is the color.", text_colour=msg_color)

Ex5B()