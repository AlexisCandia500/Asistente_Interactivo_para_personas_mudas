import threading
import tkinter as tk
from principal import InterfazDividida
from pruebarapidez import detect_internal_sound, stop_audio_stream

def run_principal():
    app = InterfazDividida(tk.Tk())
    app.root.mainloop()

def run_pruebarapidez():
    detect_internal_sound("Sistema Giroscopio")

if __name__ == "__main__":
    # Crear los hilos con daemon=True
    thread1 = threading.Thread(target=run_principal, daemon=True)
    thread2 = threading.Thread(target=run_pruebarapidez, daemon=True)

    thread1.start()
    thread2.start()

    # Esperar a que ambos hilos terminen o el programa principal se cierre
    thread1.join()
    thread2.join()

    # Detener el flujo de audio y cerrar PyAudio al salir
    stop_audio_stream()
