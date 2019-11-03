import serial
import time

arduino_rec=serial.Serial('Com5',9600)

while True:
    if (arduino_rec.inWaiting()>0):
        myData=arduino_rec.readline()
        print(myData)
