# Updated Flask API to include both the predicted winner and loser in the response

from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load and prepare the data, and train the model
df = pd.read_csv('/Users/ihsane/Desktop/Victory Vision Analytics/Vision-Victory-Analytics/API-&-scripts/merged_weather_rugby_final.csv', delimiter=';')

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

# For local testing
if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Changed the port to 5001 to avoid conflicts

# Print out the first part of the code to ensure it's displaying correctly
print(app.route)
