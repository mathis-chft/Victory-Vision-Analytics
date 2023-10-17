import requests
from bs4 import BeautifulSoup

# Dictionnaire pour mapper les noms des équipes en anglais aux noms en français
team_names_mapping = {
    "Argentina": "Argentine",
    "Australia": "Australie",
    "England": "Angleterre",
    "France": "France",
    "Ireland": "Irlande",
    "Italy": "Italie",
    "New Zealand": "Nouvelle-Zélande",
    "Scotland": "Écosse",
    "South Africa": "Afrique du Sud",
    "Wales": "Pays de Galles"
}

# Demander à l'utilisateur d'entrer les noms des équipes
team1 = input("Enter the name of the first team: ").strip()
team2 = input("Enter the name of the second team: ").strip()

# Convertir les noms des équipes en français
team1_french = team_names_mapping.get(team1, team1)
team2_french = team_names_mapping.get(team2, team2)

# URL de la page à scraper
url = 'https://www.betclic.fr/coupe-du-monde-2023-s5/coupe-du-monde-2023-c34'

# Faire une requête HTTP pour obtenir le contenu de la page
response = requests.get(url)
odds_dict = {}  # Dictionnaire pour stocker les cotes
if response.status_code == 200:
    print("Webpage successfully retrieved")
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Trouver les éléments spécifiques contenant les informations de paris
    matches = soup.find_all("a", class_="cardEvent")
    if not matches:
        print("No matches found. Check the selector.")
    
    found = False  # Indicator to check if the match was found
    for match in matches:
        # Récupération des équipes
        teams = match.find_all("div", class_="scoreboard_contestantLabel")
        if len(teams) >= 2:
            teamA = teams[0].text.strip()
            teamB = teams[1].text.strip()

            # Vérifier si les équipes correspondent à celles entrées par l'utilisateur
            if (teamA.lower() == team1_french.lower() and teamB.lower() == team2_french.lower()) or (teamA.lower() == team2_french.lower() and teamB.lower() == team1_french.lower()):
                found = True  # Le match a été trouvé
                
                # Récupération des cotes
                odds = match.find_all("sports-selections-selection", class_="oddButton")
                if len(odds) == 3:
                    odds_teamA = odds[0].find("span", class_="oddValue").text.strip()
                    draw_odds = odds[1].find("span", class_="oddValue").text.strip()
                    odds_teamB = odds[2].find("span", class_="oddValue").text.strip()

                    # Remplir le dictionnaire avec les cotes
                    odds_dict[team1] = odds_teamA
                    odds_dict["Draw"] = draw_odds
                    odds_dict[team2] = odds_teamB
                else:
                    print("Odds not found or incomplete for this match.")
                break  # Sortir de la boucle car le match a été trouvé

    if not found:
        print(f"No match found for {team1} vs {team2}.")
    else:
        print(odds_dict)  # Imprimer le dictionnaire des cotes
else:
    print("Failed to retrieve the webpage")
