from gpiozero import Button, LED
from time import sleep

button1 = Button(25)
button2 = Button(8)
button3 = Button(7)

green = LED(17)
yellow = LED(27)


def greenLED(status):
    if status == 1:
        green.on()
    else:
        green.off()


def yellowLED(status):
    if status == 1:
        yellow.on()
    else:
        yellow.off()


def pollButtons():
    if button1.is_pressed:
        return 1

    if button2.is_pressed:
        return 2

    if button3.is_pressed:
        return 3
