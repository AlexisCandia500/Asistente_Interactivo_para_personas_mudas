import pyaudio
import numpy as np
import time

sample_rate = 44100
chunk_size = 2048
volume_threshold = 0.005  # Umbral de volumen para considerar como sonido interno

# Variable global para almacenar el flujo de audio
audio_stream = None

# Función para detener el flujo de audio y cerrar PyAudio
def stop_audio_stream():
    global audio_stream
    if audio_stream:
        audio_stream.stop_stream()
        audio_stream.close()

# Función para detectar el sonido interno
def detect_internal_sound(system_name=None):
    global audio_stream
    p = pyaudio.PyAudio()

    # Abre un flujo de entrada de audio
    audio_stream = p.open(format=pyaudio.paInt16,
                          channels=1,
                          rate=sample_rate,
                          input=True,
                          frames_per_buffer=chunk_size)

    start_time = time.time()

    while True:
        # Lee un fragmento de audio
        audio_data = np.frombuffer(audio_stream.read(chunk_size), dtype=np.int16)

        # Calcula el promedio del valor absoluto de las muestras
        average_volume = np.mean(np.abs(audio_data)) / 32768.0

        # Si el volumen supera el umbral, se considera como sonido interno
        if average_volume > volume_threshold:
            elapsed_time = time.time() - start_time
            if system_name:
                print(f"Se ha detectado reproducción en {system_name} en {elapsed_time:.2f} segundos.")
            else:
                print(f"Se ha detectado reproducción en {elapsed_time:.2f} segundos.")
            break

    # Detener el flujo de audio y cerrar PyAudio de manera ordenada
    stop_audio_stream()
    p.terminate()

if __name__ == "__main__":
    detect_internal_sound("Sistema Giroscopio")
