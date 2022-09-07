from gpiozero import Button, PWMLED
from time import sleep

led = LED(25)
button = Button(24)
value = 0
while True:
    if button.is_pressed:
        print("pressed")
        if value >= 0.95:
		value = 0
		print(value)
	else:
		value = value + 0.05
		print(value)
		sleep(0.1)
	led.value = value
        
    else:
        print("not")
        led.value = 0
	value = 0
	print(value)
 


