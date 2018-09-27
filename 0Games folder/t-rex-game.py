from PIL import ImageGrab, ImageOps
import  pyautogui
import time
from numpy import *

class Coordenadas():
    botaoreplay = (723, 356)
    dinossauro = (500, 380) #360 em pe 377 abaixado

def restartGame():
    pyautogui.click(Coordenadas.botaoreplay)
    pyautogui.keyDown("down")

def pressSpace():
    x = 0.18
    pyautogui.keyUp("down")
    pyautogui.keyDown("space")
    print("Jump")
    time.sleep(0.20)
    pyautogui.keyUp("space")
    time.sleep(0.01)
    pyautogui.keyDown("down")



distancia = [130,   165,   185,   240,    310,      360]
area      = [1807,  2227,  2467,  3127,   3967,     4567]


def alou():
    global dist
    box=(Coordenadas.dinossauro[0],Coordenadas.dinossauro[1],\
    Coordenadas.dinossauro[0]+dist,Coordenadas.dinossauro[1]+12)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

def main():
    global dt
    global tempo
    global distancia
    global dist
    while True:
        tempof = time.time()
        dtempo = tempof - tempo
        print(dtempo)
        if dtempo < dt*30:
            dist = distancia[0]
            if(alou()!=area[0]):
                pressSpace()
        else:
            dist = distancia[1]
            print("Passaram-se 30 segundos")
            while True:
                tempof = time.time()
                dtempo = tempof - tempo
                print(dtempo)
                if dtempo < dt*40:
                    if(alou()!=area[1]):
                        pressSpace()
                else:
                    dist = distancia[2]
                    print("Passaram-se 40 segundos")
                    while True:
                        tempof = time.time()
                        dtempo = tempof - tempo
                        print(dtempo)
                        if dtempo < dt*70:
                            if(alou()!=area[2]):
                                pressSpace()
                        else:
                            dist = distancia[3]
                            print("Passaram-se 70 segundos")
                            while True:
                                tempof = time.time()
                                dtempo = tempof - tempo
                                print(dtempo)
                                if dtempo < dt*95:
                                        if(alou()!=area[3]):
                                            pressSpace()
                                else:
                                    dist = distancia[4]
                                    print("Passaram-se 95 segundos")
                                    while True:
                                        tempof = time.time()
                                        dtempo = tempof - tempo
                                        print(dtempo)
                                        if dtempo < dt*240:
                                            if(alou()!=area[4]):
                                                pressSpace()
                                        else:
                                            dist = distancia[5]
                                            print("Passaram-se 240 segundos")
                                            while True:
                                                tempof = time.time()
                                                dtempo = tempof - tempo
                                                print(dtempo)
                                                #if dtempo < dt*240:
                                                if(alou()!=area[5]):
                                                    pressSpace()

t0 = time.time();time.sleep(1);tf = time.time();dt = tf - t0
tempo = time.time()
print(t0)
main()
