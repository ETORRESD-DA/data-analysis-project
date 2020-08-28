
#Libraries import
import csv
from datetime import datetime
import requests
import pandas as pd

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


#Programa
entrada=input(f'Desea descargar la base de datos covid{URL_BASE} escriba (Y) si:  ')
if entrada == "Y":
    print("Comienza Analisis Covid tweter")
    df_covid= pd.read_csv(descargar_archivo(URL_BASE))
    print(f'Archivo leido de url {URL_BASE}')
else:
    print(f'Comienza Analisis Covid tweter información leida de repositorio local {FILENAME}')
    df_covid = pd.read_csv(FILENAME)

print(df_covid.head(10))

    




