from pynput.mouse import Controller, Listener, Button
from pynput.keyboard import Listener as KeyboardListener, Key

# Inicializar el controlador del ratón
mouse = Controller()

def on_press(key):
    if key == 1:  #Cambiado a Key.space para representar la tecla 1
        mouse.click(Button.left, 1)  # Clic izquierdo
    elif key == Key.alt:  # Cambiado a Key.alt para representar la tecla 2
        mouse.click(Button.right, 1)  # Clic derecho


