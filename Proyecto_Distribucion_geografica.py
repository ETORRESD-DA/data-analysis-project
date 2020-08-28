
#Libraries import
import csv
from datetime import datetime
import requests
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt


# CONSTANTES
#Url de descarga de csv
URL_BASE='http://galileoguzman.com/data/covid19_tweets.csv'
FILENAME='covid19_tweets'
FILENAME='tmp/covid19_tweets.csv'


# FUNTIONS
#descargar de una url
def descargar_archivo(DATASET_URL):
    # Fetching data
    response = requests.get(DATASET_URL)
    # Saving data
    if response.status_code == 200:
        response_content = response.content
        filename = f'tmp/{FILENAME}.csv'
        with open(filename, 'wb') as csv:
            csv.write(response_content)
            # Finishing script
            print('Download ready')
            return filename
    return None


#Funcion agrupa data frame 
def agrupa_ubicación_geografica():
    df_agrupado=df_covid.groupby(['user_location']).size().reset_index(name="count")
    return df_agrupado

#Funcion ordena data frame
def ordena_ubicación_geografica(df_agrupado):
    df_ordenado=df_agrupado.sort_values(['count'],ascending=[False])
    df_ordenado=df_ordenado.iloc[0:230,]
    return df_ordenado

#funcion grafica data frame
def grafica_ubicación_geografica(df_ordenado):
    df_ordenado.plot(kind='bar',x='user_location',y='count')
    return plt.show()


#Programa
entrada=input(f'Desea descargar la base de datos covid{URL_BASE} escriba (Y) si:  ')
#IF que controla si queremos descargar de la url o utilizarel archivo que se descargo antes
if entrada == "Y":
    print("Comienza Analisis Covid tweter")
    df_covid= pd.read_csv(descargar_archivo(URL_BASE))
    print(f'Archivo leido de url {URL_BASE}')
else:
    print(f'Comienza Analisis Covid tweter información leida de repositorio local {FILENAME}')
    df_covid = pd.read_csv(FILENAME)

df_agrupado= agrupa_ubicación_geografica()
df_ordenado= ordena_ubicación_geografica(df_agrupado)
grafica_ubicación_geografica(df_ordenado)
print(df_ordenado)
