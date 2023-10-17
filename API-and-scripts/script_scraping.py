import requests
from bs4 import BeautifulSoup

# URL de la page à scraper
url = 'https://www.betclic.fr/coupe-du-monde-2023-s5/coupe-du-monde-2023-c34'

# Faire une requête HTTP pour obtenir le contenu de la page
response = requests.get(url)
if response.status_code == 200:
    print("Successfully retrieved the webpage")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Trouver les éléments spécifiques contenant les informations de paris
    matches = soup.find_all("a", class_="cardEvent")
    if not matches:
        print("No matches found. Check the selector.")
    
    for i, match in enumerate(matches):
        
        # Récupération des équipes
        teams = match.find_all("div", class_="scoreboard_contestantLabel")
        if len(teams) >= 2:
            home_team = teams[0].text
            away_team = teams[1].text
        else:
            print("Teams not found in this match. Skipping...")
            continue
        
        # Récupération des cotes
        odds = match.find_all("sports-selections-selection", class_="oddButton")
        if len(odds) == 3:
            home_team_odds = odds[0].find("span", class_="oddValue").text
            draw_odds = odds[1].find("span", class_="oddValue").text
            away_team_odds = odds[2].find("span", class_="oddValue").text
            print(f"{home_team} vs {away_team} - Home Odds: {home_team_odds} - Draw Odds: {draw_odds} - Away Odds: {away_team_odds}")
        else:
            print("Odds not found or incomplete for this match. Skipping...")
else:
    print("Failed to retrieve the webpage")
