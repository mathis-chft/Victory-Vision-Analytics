# Importation des bibliothèques nécessaires
import pandas as pd
from collections import defaultdict
from datetime import datetime

# La fonction pour calculer les taux de victoire pour toutes les équipes
def calculate_weighted_win_rates_all_teams(filtered_df, weather_filter, temperature_filter, wind_filter, pressure_filter):
    # Partie 1 : Calculer les taux de victoire sans appliquer aucun filtre
    no_filter_win_rates = calculate_win_rates(filtered_df)
    
    # Partie 2 : Appliquer les filtres et calculer les taux de victoire
    # Appliquer le filtre météorologique si activé par l'utilisateur
    if weather_filter == 'True':
        filtered_df = filtered_df[filtered_df['precipitation_mm'] > 4.0]

    # Appliquer le filtre de température si spécifié par l'utilisateur
    if temperature_filter != 'None':
        if temperature_filter == 'Hot':
            filtered_df = filtered_df[filtered_df['avg_temp_c'] > 25]
        elif temperature_filter == 'Medium':
            filtered_df = filtered_df[(filtered_df['avg_temp_c'] >= 10) & (filtered_df['avg_temp_c'] <= 25)]
        elif temperature_filter == 'Cold':
            filtered_df = filtered_df[filtered_df['avg_temp_c'] < 10]

    # Appliquer le filtre de vent si spécifié par l'utilisateur
    if wind_filter != 'None':
        if wind_filter == 'Strong':
            filtered_df = filtered_df[filtered_df['avg_wind_speed_kmh'] > 40]
        elif wind_filter == 'Medium':
            filtered_df = filtered_df[(filtered_df['avg_wind_speed_kmh'] >= 20) & (filtered_df['avg_wind_speed_kmh'] <= 40)]
        elif wind_filter == 'Light':
            filtered_df = filtered_df[filtered_df['avg_wind_speed_kmh'] < 20]

    # Appliquer le filtre de pression si spécifié par l'utilisateur
    if pressure_filter != 'None':
        if pressure_filter == 'High':
            filtered_df = filtered_df[filtered_df['avg_sea_level_pres_hpa'] > 1020]
        elif pressure_filter == 'Medium':
            filtered_df = filtered_df[(filtered_df['avg_sea_level_pres_hpa'] >= 1010) & (filtered_df['avg_sea_level_pres_hpa'] <= 1020)]
        elif pressure_filter == 'Low':
            filtered_df = filtered_df[filtered_df['avg_sea_level_pres_hpa'] < 1010]

    # Calculer les taux de victoire avec les filtres appliqués
    with_filter_win_rates = calculate_win_rates(filtered_df)
    
    return no_filter_win_rates, with_filter_win_rates

# Fonction pour calculer les taux de victoire
def calculate_win_rates(df):
    segmented_weighted_wins = defaultdict(float)
    total_games = defaultdict(int)
    current_date = datetime.now()  # Cette ligne n'est plus nécessaire

    for _, row in df.iterrows():
        home_team = row['home_team']
        away_team = row['away_team']
        home_score = row['home_score']
        away_score = row['away_score']
        match_date = row['date']  # Cette ligne n'est plus nécessaire
        
        years_diff = (current_date - match_date).days // 365  # Cette ligne n'est plus nécessaire
        coef = 1  # Nous avons fixé le coefficient à 1 pour donner la même valeur à tous les matchs
        
        total_games[home_team] += 1 * coef
        total_games[away_team] += 1 * coef
        
        if home_score > away_score:
            segmented_weighted_wins[home_team] += 1 * coef
        elif away_score > home_score:
            segmented_weighted_wins[away_team] += 1 * coef

    all_teams_win_rates = {team: round((segmented_weighted_wins[team] / total_games[team]) * 100, 1) if total_games[team] != 0 else 0 for team in total_games.keys()}

    return all_teams_win_rates

df_path = '/Users/ihsane/Desktop/Victory Vision Analytics/Vision-Victory-Analytics/API-and-scripts/merged_weather_rugby_final.csv'
df = pd.read_csv(df_path, sep=';')
df['date'] = pd.to_datetime(df['date'])

# Application des filtres
weather_filter = 'True'
temperature_filter = 'None'
wind_filter = 'None'
pressure_filter = 'None'

# Calcul des taux de victoire pour toutes les équipes avec les données fournies
no_filter_win_rates, with_filter_win_rates = calculate_weighted_win_rates_all_teams(
    df, weather_filter, temperature_filter, wind_filter, pressure_filter)

# Impression des taux de victoire pour toutes les équipes
print("Weighted Win Rates for All Teams (No Filters):")
for team, win_rate in sorted(no_filter_win_rates.items(), key=lambda x: x[1], reverse=True):  # Trié par taux de victoire
    print(f"{team}: {win_rate}%")

print("\nWeighted Win Rates for All Teams (With Filters):")
for team, win_rate in sorted(with_filter_win_rates.items(), key=lambda x: x[1], reverse=True):  # Trié par taux de victoire
    print(f"{team}: {win_rate}%")




# Importation de la bibliothèque Plotly
import plotly.express as px  

# Créer un DataFrame à partir des taux de victoire non filtrés, triés par taux de victoire
teams_sorted_by_no_filter = sorted(no_filter_win_rates.keys(), key=lambda x: no_filter_win_rates[x], reverse=True)

# Utilisation des taux de victoire calculés pour créer un DataFrame
data = {
    'Teams': teams_sorted_by_no_filter,
    'No Filters': [no_filter_win_rates[team] for team in teams_sorted_by_no_filter],
    'With Filters': [with_filter_win_rates[team] for team in teams_sorted_by_no_filter]
}

win_rates_df = pd.DataFrame(data)

# Affichage du DataFrame pour vérifier les données
print(win_rates_df)

# Mise en forme du DataFrame pour avoir une colonne indiquant si les données sont avec ou sans filtres
melted_df = pd.melt(win_rates_df, id_vars=['Teams'], var_name='Condition', value_name='Win Rate')

# Création d'un graphique radar pour visualiser les taux de victoire avec et sans filtres
fig = px.line_polar(melted_df, r='Win Rate', theta='Teams', color='Condition', line_close=True, range_r=[0, 100])
fig.update_traces(fill='toself')

# Affichage du graphique
fig.show()









