# Importation des bibliothèques nécessaires
import pandas as pd
import plotly.express as px

# Données des taux de victoire pondérés pour toutes les équipes, avec et sans filtres
teams = [
    "New Zealand", "South Africa", "England", "France", "Australia",
    "Wales", "Ireland", "Scotland", "Argentina", "Italy"
]

no_filters_win_rates = [75.5, 60.4, 52.9, 50.1, 47.2, 47.1, 42.8, 38.8, 26.0, 9.8]
with_filters_win_rates = [86.3, 45.5, 55.4, 58.1, 41.2, 59.3, 41.2, 25.6, 28.6, 6.2]

# Création d'un DataFrame pour stocker les données
data = {
    "Teams": teams,
    "No Filters": no_filters_win_rates,
    "With Filters": with_filters_win_rates
}

df = pd.DataFrame(data)

# Création d'un graphique radar pour les données sans filtres
fig_no_filters = px.line_polar(df, r='No Filters', theta='Teams', line_close=True,
                               title='Weighted Win Rates for All Teams (No Filters)')
fig_no_filters.update_traces(fill='toself')

# Création d'un graphique radar pour les données avec filtres
fig_with_filters = px.line_polar(df, r='With Filters', theta='Teams', line_close=True,
                                 title='Weighted Win Rates for All Teams (With Filters)')
fig_with_filters.update_traces(fill='toself')

# Afficher les graphiques
fig_no_filters.show()
fig_with_filters.show()

# Si nécessaire, vous pouvez également exporter les graphiques en tant que fichiers HTML
# fig_no_filters.write_html('radar_chart_no_filters.html')
# fig_with_filters.write_html('radar_chart_with_filters.html')
