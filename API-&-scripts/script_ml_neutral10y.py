
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

# Filter the dataset to include only matches from 2013 onwards
df_clean = df_clean[df_clean['date'] >= '2013-01-01']

# Create a new column to indicate the winner
df_clean['winner'] = 'draw'
df_clean.loc[df_clean['home_score'] > df_clean['away_score'], 'winner'] = 'home'
df_clean.loc[df_clean['home_score'] < df_clean['away_score'], 'winner'] = 'away'

# Label encode team names
le = LabelEncoder()
df_clean['team1_encoded'] = le.fit_transform(df_clean['home_team'])
df_clean['team2_encoded'] = le.fit_transform(df_clean['away_team'])

# Double the dataset by switching team1 and team2 and the corresponding winners
df_doubled = df_clean.copy()
df_doubled[['team1_encoded', 'team2_encoded']] = df_doubled[['team2_encoded', 'team1_encoded']]
df_doubled['winner'] = df_doubled['winner'].replace({'home': 'away', 'away': 'home'})

# Combine the original and doubled datasets
df_combined = pd.concat([df_clean, df_doubled], ignore_index=True)

# Define features (X) and target (y)
X = df_combined[['team1_encoded', 'team2_encoded']]
y = df_combined['winner']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Function to make a prediction for a given match
def predict_winner(team1, team2, model, label_encoder):
    # Encode the team names
    team1_encoded = label_encoder.transform([team1])[0]
    team2_encoded = label_encoder.transform([team2])[0]
    
    # Prepare the feature vector
    feature_vector = [[team1_encoded, team2_encoded]]
    
    # Make the prediction
    prediction = model.predict(feature_vector)[0]
    
    # Convert the prediction to team names
    if prediction == 'home':
        prediction = team1
    elif prediction == 'away':
        prediction = team2
    else:
        prediction = 'Draw'
    
    return prediction

if __name__ == "__main__":
    # Ask the user for the team names
    team1 = input("Please enter the name of the first team: ")
    team2 = input("Please enter the name of the second team: ")
    
    # Make a sample prediction
    predicted_winner = predict_winner(team1, team2, rf_classifier, le)
    print(f"The predicted winner for the match between {team1} and {team2} is: {predicted_winner}")
