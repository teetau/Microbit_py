# kellotaulupeli
'''
Alkuun arvotaan kellonaika ja näytetään se numerona.
Sen jälkeen a- ja b-nappia painamalla kierretään
kellonkuvia kunnes numeroa vastaava löytyy.
Tarkistus tapahtuu ravistamalla.
oikea vastaus -> hymynaama
väärä vastaus -> surunaama
'''

from microbit import *
import random
# luodaan kellotaulut
kuvat = [Image.CLOCK1, Image.CLOCK2, Image.CLOCK3, Image.CLOCK4, Image.CLOCK5, Image.CLOCK6,
Image.CLOCK7, Image.CLOCK8, Image.CLOCK9, Image.CLOCK10, Image.CLOCK11, Image.CLOCK12]
lista = -1
# Arvotaan kysyttävä kellonaika ja näytetään se
kysymys = random.randint(1, 12)
display.scroll(kysymys)
sleep(500)
display.show("?")
# tarkkaillaan nappien painalluksia ja ravistusta
while True: 
    gesture = accelerometer.current_gesture()
    if button_a.was_pressed():
        lista = lista -1
        sleep(100)
        if lista < 0:  # tarkistetaan että lista menee ympäri
            lista = 11
        display.show(kuvat[lista])
    elif button_b.was_pressed():
        lista = lista +1
        sleep(100)
        if lista > 11:  # tarkistetaan että lista menee ympäri
            lista = 0
        display.show(kuvat[lista])
    elif gesture == "shake":  # vastaustoiminto eli hypätään ulos
       break
# tarkistetaan vastaus
kysymys = kysymys -1  # listakin alkaa nollasta joten otetaan yksi pois       
if lista == kysymys:
    display.show(Image.HAPPY)
else:
    display.show(Image.SAD)