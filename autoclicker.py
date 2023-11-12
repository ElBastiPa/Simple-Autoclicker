import pyautogui
from pynput.keyboard import *

cadencia = 0.001
iniciar = Key.f1
pausar = Key.f2
salir = Key.esc

pause = True
running = True

def on_press(key):
    global running, pause

    if key == iniciar:
        pause = False
        print("Iniciado")
    elif key == pausar:
        pause = True
        print("Pausado")
    elif key == salir:
        running = False
        print("Salida")

def mostrarControles():
    print("\t Velocidad = " + str(cadencia) + ' segundos' + '\n')
    print("\t F1 = Iniciar")
    print("\t F2 = Pausar")
    print("\t F3 = Salir")
    print('Presione F1 para iniciar...')

def click():
    lis = Listener(on_press=on_press)
    lis.start()

    mostrarControles()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = cadencia
    lis.stop()


if __name__ == "__main__":
    click()