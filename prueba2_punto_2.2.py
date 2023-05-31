import csv
from collections import Counter
import re

# Abrir el archivo CSV
with open('endpoint.csv', 'r') as file:
    # Crear un lector CSV
    reader = csv.DictReader(file, delimiter='\t')
    
    # Crear una lista para almacenar las palabras
    words = []
    
    # Recorrer cada fila del archivo
    for row in reader:
        # Obtener el texto de la fila actual
        text = row['Texto']
        
        # Dividir el texto en palabras utilizando expresiones regulares
        words.extend(re.findall(r'\b\w+\b', text))
        
    # Definir una lista de artículos y conectores a excluir
    excluded_words = ['a', 'an', 'the', 'and', 'or', 'but', 'of', 'in', 'on', 'at']
    
    # Contar la frecuencia de las palabras excluyendo las palabras de la lista de exclusión
    word_counts = Counter(word for word in words if word.lower() not in excluded_words)
    
    # Obtener las diez palabras más repetidas
    top_ten_words = word_counts.most_common(10)
    
    # Imprimir el ranking top ten de las palabras más repetidas
    print("Ranking top ten de las palabras más repetidas:")
    for word, count in top_ten_words:
        print(f"{word}: {count} veces")
