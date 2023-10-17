from flask import Flask, request, jsonify
from flask_cors import CORS

from script_pronoFINAL import combined_win_rate_method

app = Flask(__name__)
CORS(app)

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
