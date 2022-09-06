from gpiozero import Button, LED
from signal import pause
from time import sleep

led = LED(25)
button = Button(24)
while True:
    if button.is_pressed:
        print("pressed")
        led.on()
        
    else:
        print("not")
        led.off()
 


