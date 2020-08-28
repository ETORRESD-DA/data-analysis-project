
#Libraries import
import csv
import requests
import pandas as pd
from datetime import datetime
#from datetime import datetime

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

#Funcion que resta fechas fecha  
def days_between(d1, d2):
    return abs(d2 - d1).days
#Calcular los dias de la fecha mas antigua hasta ahora
def days_since_first():
    return abs(datetime.now()-df_covid.Created.min()).days




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

#covertir las fechas de object  a date time
df_covid['Created'] = pd.to_datetime(df_covid['user_created'])
df_covid['Executed'] = pd.to_datetime(df_covid['date'])
#aplicaos la resta de fechas con la funcion oculta lambda
df_covid['Days_Dif']=df_covid.apply(lambda x:days_between(x["Executed"],x["Created"]),axis=1)
#ordenamos por los mas altos
df_covid=df_covid.sort_values(['Days_Dif'],ascending=[False])
#imprimir fecha de creacion, ejecucion y la diferencia entre estas
print(df_covid.loc[:,["Created","Executed","Days_Dif"]])

days_since=days_since_first()
print(f'Dias trasncurridos desdeel primer tweet: {days_since}')





