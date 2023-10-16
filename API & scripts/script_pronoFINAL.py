# Importing necessary libraries
import pandas as pd
from itertools import combinations
from datetime import datetime
from collections import defaultdict

# Function for Method 1 (from script_pronoVS.py)
def calculate_weighted_win_rates_method1(home_team, away_team, filtered_df):
    specific_match_df = filtered_df[((filtered_df['home_team'] == home_team) & (filtered_df['away_team'] == away_team)) |
                                    ((filtered_df['home_team'] == away_team) & (filtered_df['away_team'] == home_team))]
    specific_match_df = specific_match_df.sort_values('date', ascending=False)
    home_wins = 0
    away_wins = 0
    home_weighted_wins = 0.0
    away_weighted_wins = 0.0
    coef = 0.9

    for _, match in specific_match_df.iterrows():
        winner = 'home' if match['home_score'] > match['away_score'] else 'away'
        if winner == 'home':
            if match['home_team'] == home_team:
                home_wins += 1
                home_weighted_wins += coef
            else:
                away_wins += 1
                away_weighted_wins += coef
        else:
            if match['away_team'] == home_team:
                home_wins += 1
                home_weighted_wins += coef
            else:
                away_wins += 1
                away_weighted_wins += coef
        coef = coef ** 2  # Squaring the coefficient at each iteration

    total_games = home_wins + away_wins
    total_coefficients_sum = sum([0.9 ** (2 ** i) for i in range(total_games)])    
    weighted_home_win_rate = round((home_weighted_wins / total_coefficients_sum) * 100, 2) if total_coefficients_sum != 0 else 0
    weighted_away_win_rate = round((away_weighted_wins / total_coefficients_sum) * 100, 2) if total_coefficients_sum != 0 else 0

    # Determine the potential winner based on the higher weighted win rate
    potential_winner = home_team if weighted_home_win_rate > weighted_away_win_rate else away_team

    return weighted_home_win_rate, weighted_away_win_rate, total_games, potential_winner

# Function for Method 2 (from script_prono.py)
def calculate_weighted_win_rates_method2(home_team, away_team, filtered_df, weather_filter, temperature_filter, wind_filter, pressure_filter):
    # Apply weather filter if enabled by the user
    if weather_filter == 'True':
        filtered_df = filtered_df[filtered_df['precipitation_mm'] > 4.0]

    # Apply temperature filter if specified by the user
    if temperature_filter != 'None':
        if temperature_filter == 'Hot':
            filtered_df = filtered_df[filtered_df['avg_temp_c'] > 25]
        elif temperature_filter == 'Medium':
            filtered_df = filtered_df[(filtered_df['avg_temp_c'] >= 10) & (filtered_df['avg_temp_c'] <= 25)]
        elif temperature_filter == 'Cold':
            filtered_df = filtered_df[filtered_df['avg_temp_c'] < 10]

    # Apply wind filter if specified by the user
    if wind_filter != 'None':
        if wind_filter == 'Strong':
            filtered_df = filtered_df[filtered_df['avg_wind_speed_kmh'] > 40]
        elif wind_filter == 'Medium':
            filtered_df = filtered_df[(filtered_df['avg_wind_speed_kmh'] >= 20) & (filtered_df['avg_wind_speed_kmh'] <= 40)]
        elif wind_filter == 'Light':
            filtered_df = filtered_df[filtered_df['avg_wind_speed_kmh'] < 20]

    # Apply pressure filter if specified by the user
    if pressure_filter != 'None':
        if pressure_filter == 'High':
            filtered_df = filtered_df[filtered_df['avg_sea_level_pres_hpa'] > 1020]
        elif pressure_filter == 'Medium':
            filtered_df = filtered_df[(filtered_df['avg_sea_level_pres_hpa'] >= 1010) & (filtered_df['avg_sea_level_pres_hpa'] <= 1020)]
        elif pressure_filter == 'Low':
            filtered_df = filtered_df[filtered_df['avg_sea_level_pres_hpa'] < 1010]

    # Filtering for the two input teams
    filtered_teams_df = filtered_df[(filtered_df['home_team'].isin([home_team, away_team])) | (filtered_df['away_team'].isin([home_team, away_team]))]

    # Initialize dictionaries to store the "segmented weighted" wins and total games for each team
    segmented_weighted_wins = defaultdict(float)
    total_games = defaultdict(int)
    total_raw_games = defaultdict(int)

    # Define the current date (assuming the most recent match date is today's date)
    current_date = datetime.now()

    # Iterate through each row in the filtered DataFrame
    for index, row in filtered_teams_df.iterrows():
        home_team_ = row['home_team']
        away_team_ = row['away_team']
        home_score = row['home_score']
        away_score = row['away_score']
        match_date = row['date']
        
        # Calculate the years difference between the match date and current date
        years_diff = (current_date - match_date).days // 365
        
        # Calculate the coefficient based on the years difference, cubed
        coef = 0.8 ** (3 * years_diff)
        
        # Update total games count
        total_games[home_team_] += 1 * coef
        total_games[away_team_] += 1 * coef

        # Update total raw games count (without any weighting)
        total_raw_games[home_team_] += 1  # Ajoutez cette ligne ici
        total_raw_games[away_team_] += 1  # Et cette ligne aussi
        
        # Update segmented weighted wins count based on the scores and coefficient
        if home_score > away_score:
            segmented_weighted_wins[home_team_] += 1 * coef
        elif away_score > home_score:
            segmented_weighted_wins[away_team_] += 1 * coef

    # Calculate segmented weighted win rates
    team1_win_rate = round((segmented_weighted_wins[home_team] / total_games[home_team]) * 100, 1)
    team2_win_rate = round((segmented_weighted_wins[away_team] / total_games[away_team]) * 100, 1)
    team1_matches_count = int(total_games[home_team])
    team2_matches_count = int(total_games[away_team])
    
    # Utilisez total_raw_games pour obtenir le nombre total de matchs
    team1_matches_count = total_raw_games[home_team]
    team2_matches_count = total_raw_games[away_team]
    
    # Determine the potential winner based on the higher weighted win rate
    potential_winner = home_team if team1_win_rate > team2_win_rate else away_team

    return team1_win_rate, team2_win_rate, team1_matches_count, team2_matches_count, potential_winner
    # The function will return team1_win_rate, team2_win_rate, team1_matches_count, team2_matches_count, potential_winner


def calculate_wilwin_score(average_win_rate_home, average_win_rate_away):
    total_average_win_rate = average_win_rate_home + average_win_rate_away
    wilwin_score_home = (100 * average_win_rate_home) / total_average_win_rate
    wilwin_score_away = (100 * average_win_rate_away) / total_average_win_rate
    return round(wilwin_score_home, 2), round(wilwin_score_away, 2)


# Combined function
def combined_win_rate_method(home_team, away_team, df_path, weather_filter, temperature_filter, wind_filter, pressure_filter):
    # Read the original CSV file and filter data (common to both methods)
    filtered_df = pd.read_csv(df_path, sep=';')
    filtered_df['date'] = pd.to_datetime(filtered_df['date'])
    start_date = datetime(2013, 1, 1)
    end_date = datetime(2023, 12, 31)
    filtered_df = filtered_df[(filtered_df['date'] >= start_date) & (filtered_df['date'] <= end_date)]
    
    # Method 1: Call the function for the first method
    weighted_home_win_rate1, weighted_away_win_rate1, total_games1, potential_winner1 = calculate_weighted_win_rates_method1(home_team, away_team, filtered_df)
    
    # Method 2: Call the function for the second method
    # For now, let's not apply any weather, temperature, wind, or pressure filters
    team1_win_rate2, team2_win_rate2, team1_matches_count2, team2_matches_count2, potential_winner2 = calculate_weighted_win_rates_method2(home_team, away_team, filtered_df, weather_filter, temperature_filter, wind_filter, pressure_filter)


    # Combine the results into a single dictionary
    combined_dict = {
        'status': 'Success',
        'teams': {
            home_team: {
                'method1': {
                    'win_rate': weighted_home_win_rate1,
                    'matches_count': total_games1
                },
                'method2': {
                    'win_rate': team1_win_rate2,
                    'matches_count': team1_matches_count2
                }
            },
            away_team: {
                'method1': {
                    'win_rate': weighted_away_win_rate1,
                    'matches_count': total_games1
                },
                'method2': {
                    'win_rate': team2_win_rate2,
                    'matches_count': team2_matches_count2
                }
            }
        },
        'potential_winner': {
            'method1': potential_winner1,
            'method2': potential_winner2
        }
    }

    # Calcul de la moyenne des taux de victoire pour chaque équipe
    average_win_rate_home_team = (weighted_home_win_rate1 + team1_win_rate2) / 2
    average_win_rate_away_team = (weighted_away_win_rate1 + team2_win_rate2) / 2

    # Calcul du Wilwin score pour chaque équipe
    wilwin_score_home, wilwin_score_away = calculate_wilwin_score(average_win_rate_home_team, average_win_rate_away_team)

    # Déterminer le vainqueur potentiel final
    final_potential_winner = home_team if average_win_rate_home_team > average_win_rate_away_team else away_team

    # Ajouter ces nouvelles données à votre dictionnaire de résultats
    combined_dict['teams'][home_team]['average_win_rate'] = average_win_rate_home_team
    combined_dict['teams'][away_team]['average_win_rate'] = average_win_rate_away_team
    combined_dict['teams'][home_team]['wilwin_score'] = wilwin_score_home
    combined_dict['teams'][away_team]['wilwin_score'] = wilwin_score_away
    combined_dict['final_potential_winner'] = final_potential_winner

    return combined_dict


if __name__ == "__main__":
    home_team = input("Entrez le nom de la première équipe: ")
    away_team = input("Entrez le nom de la deuxième équipe: ")
    weather_filter = input("Filtre météo (True/False): ")
    temperature_filter = input("Filtre de température (Hot/Medium/Cold/None): ")
    wind_filter = input("Filtre de vent (Strong/Medium/Light/None): ")
    pressure_filter = input("Filtre de pression (High/Medium/Low/None): ")
    df_path = "/Users/ihsane/Desktop/Victory Vision Analytics/merged_weather_rugby_final.csv"
    result = combined_win_rate_method(home_team, away_team, df_path, weather_filter, temperature_filter, wind_filter, pressure_filter)    
    print(result)



