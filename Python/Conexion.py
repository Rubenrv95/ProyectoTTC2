import serial

ser = serial.Serial('COM2',9600)

while True:
    dato = ser.readline()
    dato = format(dato.decode('utf-8'))
    print(dato)