import pyaudio
import numpy as np
import time

sample_rate = 44100
chunk_size = 2048
volume_threshold = 0.05  # Umbral de volumen para considerar como sonido interno

# Función para detectar el sonido interno
def detect_internal_sound(system_name):
    p = pyaudio.PyAudio()

    # Abre un flujo de entrada de audio
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk_size)

    start_time = time.time()

    while True:
        # Lee un fragmento de audio
        audio_data = np.frombuffer(stream.read(chunk_size), dtype=np.int16)

        # Calcula el promedio del valor absoluto de las muestras
        average_volume = np.mean(np.abs(audio_data)) / 32768.0

        # Si el volumen supera el umbral, se considera como sonido interno
        if average_volume > volume_threshold:
            elapsed_time = time.time() - start_time
           # print(f"Se ha detectado  {elapsed_time:.2f} segundos.") 
            print(f"Se ha detectado reproducción en {system_name} en {elapsed_time:.2f} segundos.")
            break

if __name__ == "__main__":
    detect_internal_sound("Sistema Optikey")
    #detect_internal_sound()
