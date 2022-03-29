from tkinter import *
import tkinter.font as tkfont
from gpiozero import LED

# Declare coloured LED pins
green = LED(4)
blue = LED(17)
red = LED(27)

## Define GUI
window = Tk()
window.title("LED Toggle GUI")
window_font = tkfont.Font(family = 'Helvetica', size = 12, weight = "bold")

# Determine which LED to turn on
def led_toggle():
    # Turn off all LEDS
    turn_off_leds()
    # Get value stored in radio button variable
    led_value = led.get()
    # Turn on the selected LED
    if led_value == 1:
        green.on()
    if led_value == 2:
        blue.on()
    if led_value == 3:
        red.on()    

# Turn off all LEDs
def turn_off_leds():
    green.off()
    blue.off()
    red.off()

# Buttons
# Variable for the 3 radio buttons
led = IntVar()

# Green, blue, red radio buttons. Turn on only the selected LED
green_button = Radiobutton(window, text = "Green LED", variable = led, value = 1, command = led_toggle)
green_button.grid(row=0, column=1)

blue_button = Radiobutton(window, text = "Blue LED", variable = led, value = 2, command = led_toggle)
blue_button.grid(row=1, column=1)

red_button = Radiobutton(window, text = "Red LED", variable = led, value = 3, command = led_toggle)
red_button.grid(row=2, column=1)

# Loop window forever
window.mainloop()
