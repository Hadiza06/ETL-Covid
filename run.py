import requests
import pandas as pd
from datetime import datetime
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("etl_covid.log", mode="a", encoding="utf-8")
    ]
)

logger = logging.getLogger("ETL_Covid")
logger.info("Début du script ETL")
# URL de l'API
url = "https://disease.sh/v3/covid-19/countries"
# Envoyer une requête GET
response = requests.get(url)
# Vérifier le statut de la réponse
if response.status_code == 200:
   # Extraire les données au format JSON
   data = response.json()
   logger.info("API appelée avec succès")
   #print(data)
else:
   print(f"Erreur : {response.status_code}")
   logger.error(f"Erreur API : {response.status_code}")


df = pd.DataFrame(data)
# Selecting specific columns by name

selected_columns = df[['country', 'cases', 'deaths', 'recovered', 'active', 'critical', 'population','casesPerOneMillion','deathsPerOneMillion']].copy()
print(selected_columns)

selected_columns['taux_mortalite'] = selected_columns['deaths'] / selected_columns['cases'] * 100
selected_columns['taux_guerison'] = selected_columns['recovered'] / selected_columns['cases'] * 100

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f"covid_{timestamp}.csv"
selected_columns.to_csv(file_name, index=False)
logger.info(f"CSV sauvegardé : {file_name} - {len(selected_columns)} lignes")


print(f"Taux de mortalité : {selected_columns['taux_mortalite'].mean():.2f}%")
print(f"Taux de guérison : {selected_columns['taux_guerison'].mean():.2f}%")







