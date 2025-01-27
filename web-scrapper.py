import requests
from bs4 import BeautifulSoup
import csv

# Hacemos el request a la página de la liga para obtener el html
response = requests.get("https://www.laliga.com/laliga-easports/clasificacion")

# Utilizamos BeautifulSoup para leer el contenido del html
soup = BeautifulSoup(response.content, 'html5lib')

equipos = []

# Buscamos todos los contenedores con información sobre los equipos
table = soup.find_all('div', class_="styled__ContainerAccordion-sc-e89col-11 czlpZs")

# Cojemos las 20 primeras entradas (por algún motivo el find_all devuelve la misma lista 3 veces)
table = table[0:20]

# Inicializamos la secuencia en la que vamos a obtener los datos
seq = ['pos','team','pts', 'PJ', 'PG', 'PE', 'PP', 'GF', 'GC', 'DG']

for entry in table:
    dicAux = []
    for n,row in enumerate(entry.find('div', class_="styled__StandingTabBody-sc-e89col-0 isRHqh")):

        # N==1 es el nombre del equipo, que será la 'key' de nuestro diccionario
        dicAux.append(row.p.text)
    
    # Inicializamos la entrada 'name' con los datos obtenidos
    equipos.append(dicAux)

# Nombre del archivo donde guardamos la información
filename = 'datosLaLiga.csv'

# Creamos el archivo y guardamos la información
with open(filename, 'w', newline='') as csvfile:
    csvWriter = csv.writer(csvfile, delimiter='|')
    csvWriter.writerows([seq])
    csvWriter.writerows(equipos)
    print("Los datos han sido escritos con exito")
