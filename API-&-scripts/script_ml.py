
# Importing necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('/Users/ihsane/Desktop/Victory Vision Analytics/Vision-Victory-Analytics/API-&-scripts/merged_weather_rugby_final.csv', delimiter=';')

# Drop unnecessary columns
columns_to_drop = ['competition', 'stadium', 'city', 'country', 'neutral', 'world_cup', 'season',
                   'avg_temp_c', 'min_temp_c', 'max_temp_c', 'precipitation_mm', 'snow_depth_mm',
                   'avg_wind_dir_deg', 'avg_wind_speed_kmh', 'peak_wind_gust_kmh', 'avg_sea_level_pres_hpa']
df_clean = df.drop(columns=columns_to_drop)

# Create a new column to indicate the winner
df_clean['winner'] = 'draw'
df_clean.loc[df_clean['home_score'] > df_clean['away_score'], 'winner'] = 'home'
df_clean.loc[df_clean['home_score'] < df_clean['away_score'], 'winner'] = 'away'

# Label encode team names
le = LabelEncoder()
df_clean['home_team_encoded'] = le.fit_transform(df_clean['home_team'])
df_clean['away_team_encoded'] = le.fit_transform(df_clean['away_team'])

# Define features (X) and target (y)
X = df_clean[['home_team_encoded', 'away_team_encoded']]
y = df_clean['winner']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_classifier.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Function to make a prediction for a given match
def predict_winner(home_team, away_team, model, label_encoder):
    # Encode the team names
    home_team_encoded = label_encoder.transform([home_team])[0]
    away_team_encoded = label_encoder.transform([away_team])[0]
    
    # Prepare the feature vector
    feature_vector = [[home_team_encoded, away_team_encoded]]
    
    # Make the prediction
    prediction = model.predict(feature_vector)[0]
    
    return prediction


if __name__ == "__main__":
    # Demander à l'utilisateur les noms des équipes
    home_team = input("Veuillez entrer le nom de l'équipe à domicile : ")
    away_team = input("Veuillez entrer le nom de l'équipe à l'extérieur : ")
    
    # Faire une prédiction en utilisant les noms des équipes saisis
    predicted_winner = predict_winner(home_team, away_team, rf_classifier, le)

    # Convertir la prédiction en nom d'équipe
    if predicted_winner == 'home':
        predicted_winner = home_team
    elif predicted_winner == 'away':
        predicted_winner = away_team
    else:
        predicted_winner = 'Match nul'

    print(f"Le vainqueur prédit pour le match entre {home_team} et {away_team} est : {predicted_winner}")


