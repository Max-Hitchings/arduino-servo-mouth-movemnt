import serial
import time

arduinoData =  serial.Serial('com4',9600)

def turn90():
    arduinoData.write(b'180')

def turn0():
    arduinoData.write(b'20')

#time.sleep(0.7)

#while True:
#    data = input("0 or 1  ")
#    if data == "0":
#        turn0()
#    else:
#        turn90()

while True:
    input_value = input('Enter : ')
    arduinoData.write(input_value.encode())