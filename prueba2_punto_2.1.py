import requests
import csv

# Realizar la solicitud al endpoint
response = requests.get("https://dummyjson.com/quotes")
data = response.json()

# Obtener los valores de los campos "autor" y "texto"
quotes = data["quotes"]
authors = [quote["author"] for quote in quotes]
texts = [quote["quote"] for quote in quotes]

# Guardar los valores en un archivo CSV
with open("endpoint.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter="\t")
    writer.writerow(["Autor", "Texto"])  # Escribir la cabecera del archivo
    writer.writerows(zip(authors, texts))  # Escribir los valores de los campos

print("Archivo CSV creado exitosamente.")
