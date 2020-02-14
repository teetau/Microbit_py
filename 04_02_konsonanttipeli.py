from microbit import *
import random
# konsonanttipeli
# peli kyselee kuuluuko tietty kirjain konsonantteihin
# vai vokaaleihin
# kirjaimet ovat omissa listoissaan
vokal = ["A", "E", "I", "O", "U", "Y"]
konso = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M"]
konso2 = ["N", "P", "Q", "R", "S", "T", "V", "X", "Z"]
pisteet = 0
display.scroll("A on vokaali", delay = 80)
display.scroll("B on konsonantti", delay = 80)

while True:
    nayta = random.randint(0, 2)
    
    if nayta == 0:
        display.show(random.choice(vokal))
        sleep(1000)
        if button_a.was_pressed():
            display.show(Image.HAPPY)
            pisteet = pisteet + 1
        else:
            display.show(Image.SAD)
            sleep(500)
            break
    if nayta == 1:
        display.show(random.choice(konso))
        sleep(1000)
        if button_b.was_pressed():
            display.show(Image.HAPPY)
            pisteet = pisteet + 1
        else:
            display.show(Image.SAD)
            sleep(500)
            break
    if nayta == 2:
        display.show(random.choice(konso2))
        sleep(1000)
        if button_b.was_pressed():
            display.show(Image.HAPPY)
            pisteet = pisteet + 1
        else:
            display.show(Image.SAD)
            sleep(500)
            break
            
display.clear()
display.scroll(pisteet)
sleep(3000)
display.clear()