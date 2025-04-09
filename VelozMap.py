#!/usr/bin/env python3
# ==============================================
#                🚀 VelozMap  🚀
# ----------------------------------------------
#  Autor: Nicolás Farias Peredo
#  Descripción: Escaneo Nmap personalizado en 
#               modo discreto, medio o rápido.
#  Uso: python3 escaneo.py {discreto|medio|rapido} <IP>
#  Versión: 1.0
# ==============================================
import sys
import subprocess
import pyfiglet
import argparse
from colorama import init, Fore, Back

init(autoreset=True)

banner = pyfiglet.figlet_format("VelozMap")
print(banner)

# Configuración de argparse para recibir los argumentos
parser = argparse.ArgumentParser(description="VelozMap: Herramienta de escaneo Nmap personalizado")
parser.add_argument("modo", choices=["discreto", "medio", "rapido"], help="Modo de escaneo: discreto, medio o rápido.")
parser.add_argument("ip", help="IP o rango de IPs a escanear.")
args = parser.parse_args()


#Verificación de parametros correctos
if len(sys.argv) != 3:
    print("Uso: python3 velozmap.py {discreto|medio|rapido}")
    sys.exit(1)


# Modo de escaneo y IP
modo = sys.argv[1]
ip = sys.argv[2]


#comandos de nmap segun el modo elegido.
if modo == "discreto":
    print(f"[*] Iniciando escaneo discreto en {ip}...")
    comando = ["nmap", "-sS", "-sV", "-T0", "-Pn", "--scan-delay", "1s", ip]

elif modo == "medio":
    print(f"[*] Iniciando escaneo medio en {ip}...")
    comando = ["nmap", "-sS", "-sV", "-T3", "-Pn", ip]

elif modo == "rapido":
    print(f"[*] Iniciando escaneo rápido en {ip}...")
    comando = ["nmap", "-sS", "-sV", "-T5", "--max-retries", "2", "--min-rate", "1000", "-Pn", ip]

else:
    print("Modo no válido. Usa: discreto, medio o rapido.")
    sys.exit(1)

# Lanzamiento de escaneo
try:
    subprocess.run(comando)
except FileNotFoundError:
    print("Error: nmap no está instalado o no se logra encontrar.")