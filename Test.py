import serial
import time

arduinoData =  serial.Serial('com7',9600)

#def turn90():
#    arduinoData.write(b'180')
#
#def turn0():
#    arduinoData.write(b'20')

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
    print(input_value.encode())
    #if input_value == "1":
    #    arduinoData.write(b'1')
    #    time.sleep(0.2)
    #    arduinoData.write(b'0')
    #elif input_value == "2":
    #    arduinoData.write(b'2')
    #else:
    #    arduinoData.write(b'10')
    #arduinoData.write(input_value.encode())