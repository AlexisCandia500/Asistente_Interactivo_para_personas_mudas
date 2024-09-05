import serial
import pyautogui

ser = serial.Serial('COM9', 9600)  # Reemplaza 'COMX' con el puerto COM correcto
while True:
    data = ser.readline().decode('utf-8').strip().split(',')
    if len(data) == 2:
        x, y = map(int, data)
        pyautogui.moveRel(x, y)
