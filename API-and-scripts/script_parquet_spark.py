from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date
from pyspark.sql.types import DateType

# Créer une session Spark
spark = SparkSession.builder \
    .appName('Rugby Weather Analysis') \
    .getOrCreate()

# Charger le jeu de données météorologiques avec l'option de rebasage datetime
weather_df = spark.read.option("datetimeRebaseMode", "CORRECTED").parquet("daily_weather.parquet")


# Charger le jeu de données des matchs de rugby
rugby_df = spark.read.csv("rugby dataset.csv", header=True, inferSchema=True)

# Convertir la colonne de la date en format standard
weather_df = weather_df.withColumn("date", to_date(col("date"), "yyyy-MM-dd"))
rugby_df = rugby_df.withColumn("date", to_date(col("date"), "dd/MM/yyyy"))

# Identifier les villes et les dates où les matchs de rugby ont lieu
rugby_cities_dates = rugby_df.select("date", "city").distinct()

# Fusionner les deux jeux de données sur la base de la date et de la ville
merged_df = rugby_df.join(weather_df.withColumnRenamed("city_name", "city"), ["date", "city"], 'left')

# Afficher le nouvel ensemble de données fusionnées
merged_df.show()

# Sauvegarder le nouvel ensemble de données dans un fichier
#merged_df.write.csv("SPARK5merged_rugby_weather.csv", header=True)

merged_df.coalesce(1).write.csv("SPARK6merged_rugby_weather.csv", header=True)




