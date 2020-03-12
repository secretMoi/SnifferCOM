# Module de lecture/ecriture du port série
# Port série COM
# Vitesse de baud : 9600
# Timeout en lecture : 1 sec
# Timeout en écriture : 1 sec
from serial import *

port_number: str


def Fin():
	print("Programme terminé")


def Recoit(port: Serial):
	ligne = port.read(128)
	print(ligne)


def Envoie(port):
	nombre = input("Entrez un nombre : ")
	port.write(nombre.encode('utf-8'))


port_number = input("N° port COM ? ")
port_number = "COM" + port_number

with Serial(port=port_number, baudrate=9600, timeout=1, writeTimeout=1) as port_serie:
	if port_serie.isOpen():
		print("Port " + port_serie.port + " ouvert")

		Envoie(port_serie)
		Recoit(port_serie)

	Fin()
