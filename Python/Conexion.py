import sys, serial
from Adafruit_IO import MQTTClient

ADAFRUIT_IO_USERNAME = "MatiasPizarro"
ADAFRUIT_IO_KEY = "aio_hXDO93A4VX7u1PWMRs8z6FUIrHyj"
ser = serial.Serial('COM2',9600)

def connected(client):
    client.subscribe('Curico')
    client.subscribe('Talca')

def disconnected(client):
    sys.exit(1)

def message(client,feed_id,payload):
    if(payload[0] == "1"):
        print('Esta lloviendo en la cuidad de {0}'.format(feed_id))
    elif (payload[0] == "0"):
        print('No esta lloviendo en la cuidad de {0}'.format(feed_id))
    else:
        print("Error al recibir el dato")


client = MQTTClient(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message

client.connect()
client.loop_background()   

while True:
    dato = ser.readline()
    dato = format(dato.decode('utf-8'))
    if(dato != ""):
        separado = dato.split(" ")
        if(separado[0] == "Curico"):
            client.publish('Curico',separado[1])
        elif(separado[0] == "Talca"):
            client.publish('Talca', separado[1])
        print(dato)
    else:
        print("no hay dato")

