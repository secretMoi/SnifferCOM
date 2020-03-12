# Module de lecture/ecriture du port série
# Port série COM
# Vitesse de baud : 9600
# Timeout en lecture : 1 sec
# Timeout en écriture : 1 sec
from serial import *

port_number: str
type_OS: str


def Fin():
	print("Programme terminé")


def Recoit(port: Serial):
	ancienneDonnees: bool = True
	trouve: bool = False  # tant qu'aucune donnée n'est reçue

	while trouve is False:
		ligne = port.read(128)

		if ligne != b'':  # si aucune données reçues
			print(ligne)
			ancienneDonnees = True
			trouve = True
		if ancienneDonnees is True:
			print("Attente des données")
			ancienneDonnees = False


def Envoie(port):
	nombre = input("Entrez un nombre : ")
	port.write(nombre.encode('utf-8'))


type_OS = input("Linux (1) ou Windows (2) ou Linux USB(3) ?")


port_number = input("N° port série ? ")
if type_OS == "1":
	port_number = "/dev/tty" + port_number
elif type_OS == "2":
	port_number = "COM" + port_number
elif type_OS == "3":
	port_number = "/dev/ttyUSB" + port_number

with Serial(port=port_number, baudrate=9600, timeout=1, writeTimeout=1) as port_serie:
	if port_serie.isOpen():
		print("Port " + port_serie.port + " ouvert")

		Envoie(port_serie)
		Recoit(port_serie)

	Fin()
