# Module de lecture/ecriture du port série
# Port série COM
# Vitesse de baud : 9600
# Timeout en lecture : 1 sec
# Timeout en écriture : 1 sec
from serial import *

port_number: str
type_programme: str
type_OS: str


def Fin():
	print("Programme terminé")


def Recoit(port: Serial):
	while True:
		ligne = None
		ligne = port.read(128)
		if ligne is not None:
			print(ligne)


def Envoie(port):
	nombre = input("Entrez un nombre : ")
	port.write(nombre.encode('utf-8'))


type_programme = input("Lecture (1) ou écriture (2) ?")
type_OS = input("Linux (1) ou Windows (2) ?")


port_number = input("N° port COM ? ")
if type_OS == "1":
	port_number = "/dev/tty" + port_number
elif type_OS == "2":
	port_number = "COM" + port_number

with Serial(port=port_number, baudrate=9600, timeout=1, writeTimeout=1) as port_serie:
	if port_serie.isOpen():
		print("Port " + port_serie.port + " ouvert")

		if type_programme == "1":
			Envoie(port_serie)
		elif type_programme == "2":
			Recoit(port_serie)

	Fin()
