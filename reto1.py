# Dado un fichero excel con nombres y correos (columna nombre y columna email), 
# realiza un script en Python que devuelva los mails únicos de la columna email.
import pandas as pd 

file = pd.read_excel('mails.xlsx', usecols='B:B')

print(file)