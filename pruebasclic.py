import tkinter as tk
from tkinter import ttk
import threading
import time

class InterfazDividida:
    def __init__(self, root):
        self.root = root
        self.tiempo_inicial = None
        self.clics = 0  # Contador de clics
        
   
        self.iniciar_temporizador()

    

    def iniciar_temporizador(self):
        self.tiempo_inicial = time.time()
        # Crear un hilo para el temporizador
        threading.Thread(target=self.actualizar_tiempo).start()

    def reiniciar_temporizador(self):
        self.clics += 1  # Incrementar el contador de clics
        if self.clics % 2 == 0:  # Reiniciar solo en el segundo clic
            #SE HA HECHO CLIC EN EL BOTON
            print(f" {self.boton_clicado_nombre}")
            self.tiempo_inicial = time.time()
        
    def actualizar_tiempo(self):
        while True:
            if self.tiempo_inicial is not None:
                tiempo_actual = int(time.time() - self.tiempo_inicial)
                print(f"Tiempo transcurrido: {tiempo_actual} segundos")

            # Esperar 1 segundo antes de la próxima actualización
            time.sleep(1)
                
    def boton_izquierdo_clicado(self, numero_boton):
        if numero_boton == 0:
            self.mostrar_botones_SALUDOS()
            self.boton_clicado_nombre ="Seleccionado con CameraMouse2018"
        elif numero_boton == 1:
            self.mostrar_botones_DESPEDIDAS()
            self.boton_clicado_nombre ="Seleccionado con CameraMouse2018"
        elif numero_boton == 2:
            self.mostrar_botones_RESPUESTAS()
            self.boton_clicado_nombre ="Seleccionado con CameraMouse2018"
        elif numero_boton == 3:
            self.mostrar_botones_NECESIDADES()
            self.boton_clicado_nombre ="Seleccionado con CameraMouse2018"
        elif numero_boton == 4:
            self.mostrar_botones_AYUDA()
            self.boton_clicado_nombre ="Seleccionado con CameraMouse2018"
        elif numero_boton == 5:
            self.mostrar_botones_CONFIRMACION()
            self.boton_clicado_nombre ="Seleccionado con CameraMouse2018"
        elif numero_boton == 6:
            self.mostrar_botones_INTERACCION()
            self.boton_clicado_nombre ="Seleccionado con CameraMouse2018"
        elif numero_boton == 7:
            self.mostrar_botones_PREGUNTAS()
            self.boton_clicado_nombre ="Seleccionado con CameraMouse2018"

        # Actualizar tiempo al hacer clic
      
        self.reiniciar_temporizador()
        
    def boton_derecho_clicado(self, nombre_boton):
        print(nombre_boton)
        # Llama a la función que falta, reemplázala con la acción que desees realizar
        # boton_clicado(nombre_boton)
        self.tiempo_inicial = None
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazDividida(root)
        # Configurar el estilo para los botones (debería estar antes del mainloop)
    root.style = ttk.Style()
    root.style.configure('Boton.TButton', font=('Helvetica', 16), background='#008000', foreground='white',
                         borderwidth=5, relief='ridge', focuscolor='#008000')
    root.mainloop()
    
