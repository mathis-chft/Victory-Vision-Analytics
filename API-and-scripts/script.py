import pandas as pd

# Charger les données à partir des fichiers .parquet et .csv
weather_df = pd.read_parquet('daily_weather.parquet')
rugby_df = pd.read_csv('rugby dataset.csv')

# Convertir la colonne 'date' en type de données datetime dans les deux DataFrames
weather_df['date'] = pd.to_datetime(weather_df['date'])
rugby_df['date'] = pd.to_datetime(rugby_df['date'])

# Créer un ensemble de villes concernées par les matchs de rugby
cities_concerned = set(rugby_df['city'].unique())

# Filtrer les matchs de rugby par les villes concernées
filtered_rugby_df = rugby_df[rugby_df['city'].isin(cities_concerned)]

# Fusionner les données météorologiques avec les matchs de rugby en fonction de la date et de la ville
merged_df = filtered_rugby_df.merge(weather_df, left_on=['date', 'city'], right_on=['date', 'city_name'], how='left')

# Afficher le DataFrame fusionné
print(merged_df)

# Sauvegarder le DataFrame fusionné dans un fichier CSV
merged_df.to_csv('merged_rugby_weather.csv', index=False)
