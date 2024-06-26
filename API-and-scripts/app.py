from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
from script_pronoFINAL import combined_win_rate_method
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
CORS(app)

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

@app.route('/api/calculate_win_rate', methods=['POST'])
def calculate_win_rate():
    try:
        data = request.json
        home_team = data.get('home_team')
        away_team = data.get('away_team')
        weather_filter = data.get('weather_filter')
        temperature_filter = data.get('temperature_filter')
        wind_filter = data.get('wind_filter')
        pressure_filter = data.get('pressure_filter')
        df_path = data.get('df_path')

        if not all([home_team, away_team, df_path]):
            return jsonify({'status': 'Error', 'message': 'Missing required parameters'}), 400

        result = combined_win_rate_method(home_team, away_team, df_path, weather_filter, temperature_filter, wind_filter, pressure_filter)
        return jsonify(result)

    except Exception as e:
        return jsonify({'status': 'Error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/api/get_odds', methods=['GET'])
def get_odds():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    # Convertir les noms des équipes en français
    team1_french = team_names_mapping.get(team1, team1)
    team2_french = team_names_mapping.get(team2, team2)

    # URL de la page à scraper
    url = 'https://www.betclic.fr/coupe-du-monde-2023-s5/coupe-du-monde-2023-c34'
    response = requests.get(url)
    odds_dict = {}  # Dictionnaire pour stocker les cotes

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        matches = soup.find_all("a", class_="cardEvent")

        if not matches:
            return jsonify({"error": "No matches found"}), 404

        found = False
        for match in matches:
            teams = match.find_all("div", class_="scoreboard_contestantLabel")
            if len(teams) >= 2:
                teamA = teams[0].text.strip()
                teamB = teams[1].text.strip()

                if (teamA.lower() == team1_french.lower() and teamB.lower() == team2_french.lower()) or (teamA.lower() == team2_french.lower() and teamB.lower() == team1_french.lower()):
                    found = True
                    odds = match.find_all("sports-selections-selection", class_="oddButton")
                    if len(odds) == 3:
                        odds_teamA = odds[0].find("span", class_="oddValue").text.strip()
                        draw_odds = odds[1].find("span", class_="oddValue").text.strip()
                        odds_teamB = odds[2].find("span", class_="oddValue").text.strip()

                        odds_dict[team1] = odds_teamA
                        odds_dict["Draw"] = draw_odds
                        odds_dict[team2] = odds_teamB
                    break

        if not found:
            return jsonify({"error": f"No match found for {team1} vs {team2}"}), 404
        return jsonify(odds_dict)

    return jsonify({"error": "Failed to retrieve the webpage"}), 500

# Load and prepare the data, and train the model
df = pd.read_csv('../API-and-scripts/merged_weather_rugby_final.csv', delimiter=';')

# Prepare data and train model
def prepare_and_train_model(df):
    # Similar preprocessing as in the provided script
    columns_to_drop = ['competition', 'stadium', 'city', 'country', 'neutral', 'world_cup', 'season',
                       'avg_temp_c', 'min_temp_c', 'max_temp_c', 'precipitation_mm', 'snow_depth_mm',
                       'avg_wind_dir_deg', 'avg_wind_speed_kmh', 'peak_wind_gust_kmh', 'avg_sea_level_pres_hpa']
    df_clean = df.drop(columns=columns_to_drop)
    df_clean = df_clean[df_clean['date'] >= '2013-01-01']
    df_clean['winner'] = 'draw'
    df_clean.loc[df_clean['home_score'] > df_clean['away_score'], 'winner'] = 'home'
    df_clean.loc[df_clean['home_score'] < df_clean['away_score'], 'winner'] = 'away'
    
    # Label encoding
    le = LabelEncoder()
    df_clean['team1_encoded'] = le.fit_transform(df_clean['home_team'])
    df_clean['team2_encoded'] = le.fit_transform(df_clean['away_team'])

    df_doubled = df_clean.copy()
    df_doubled[['team1_encoded', 'team2_encoded']] = df_doubled[['team2_encoded', 'team1_encoded']]
    df_doubled['winner'] = df_doubled['winner'].replace({'home': 'away', 'away': 'home'})

    df_combined = pd.concat([df_clean, df_doubled], ignore_index=True)

    X = df_combined[['team1_encoded', 'team2_encoded']]
    y = df_combined['winner']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X_train, y_train)
    
    return rf_classifier, le

model, label_encoder = prepare_and_train_model(df)

# Prediction route
@app.route('/api/predict_winner', methods=['POST'])
def predict_winner():
    data = request.json
    team1 = data.get('team1')
    team2 = data.get('team2')

    # Encode the team names
    team1_encoded = label_encoder.transform([team1])[0]
    team2_encoded = label_encoder.transform([team2])[0]

    # Prepare the feature vector
    feature_vector = [[team1_encoded, team2_encoded]]

    # Make the prediction
    prediction = model.predict(feature_vector)[0]

    # Prepare the response
    response = {}
    if prediction == 'home':
        response["winner"] = team1
        response["loser"] = team2
    elif prediction == 'away':
        response["winner"] = team2
        response["loser"] = team1
    else:
        response["winner"] = 'Draw'
        response["loser"] = 'Draw'

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
