### **Etapes/décisions prises :**

- **Trier et lire les informations**
    
    → Nous avons commencé par tenter des trier les données du .parquet en gardant seulement les jours ou il y a eu des matchs. 
    
    → Puis seulement les jour ou il y a eu des matchs dans les villes ou il y a eu des matchs.
    
    - Problème → Pour certains match, il n’y a pas de ligne dans le .parquet correspondante, ducoup on perd des matchs.
    - Solution → Enrichir le rugby.csv en rajoutant les infos météo du parquet
    
    → Virer la colonne “sunshine_total_min” car elle ne contient que des “NaN”
    
    → Virer les colonnes “station_id”, car elle ne sert à rien
    
    → Virer les colonnes “city_name” car il y a déja “city”
    
    → Création du script de scraping sur Betclic
    
    - Choix de la library “****BeautifulSoup”****
        
        <aside>
        ❓ **ChatGPT** **- pourquoi beautiful soup et pas scrapy ? quelle différence ?**
        
        **`BeautifulSoup`** et **`Scrapy`** sont deux bibliothèques populaires pour le web scraping en Python, mais elles sont conçues avec des objectifs légèrement différents et offrent des niveaux de fonctionnalités différents.
        
        ### **BeautifulSoup :**
        
        1. **Facilité d'utilisation** : BeautifulSoup est souvent plus facile à utiliser pour les débutants. Il permet d'extraire rapidement des données à partir de pages web sans trop de configuration.
        2. **Souplesse** : Vous pouvez utiliser BeautifulSoup en conjonction avec plusieurs bibliothèques de requêtes HTTP comme **`requests`** pour récupérer le contenu des pages web.
        3. **Analyse HTML** : BeautifulSoup est principalement axé sur l'extraction de données à partir de documents HTML et XML. Il ne gère pas lui-même les requêtes HTTP.
        4. **Usage** : Idéal pour des projets de petite à moyenne envergure ou pour des tâches de scraping ponctuelles.
        5. **Synchronicité** : BeautifulSoup fonctionne de manière synchrone. Cela signifie qu'il attend la fin d'une opération avant de passer à la suivante.
        
        ### **Scrapy :**
        
        1. **Robustesse** : Scrapy est plus robuste et est conçu pour des projets de scraping à grande échelle. Il peut manipuler plusieurs requêtes en parallèle et offre de nombreuses fonctionnalités.
        2. **Framework complet** : Contrairement à BeautifulSoup qui est une bibliothèque, Scrapy est un framework complet qui gère les requêtes HTTP, le middleware, etc.
        3. **Asynchronicité** : Scrapy utilise l'asynchronicité pour gérer plusieurs requêtes simultanément, ce qui peut rendre le scraping plus rapide.
        4. **Pipelines de données** : Scrapy facilite le stockage des données extraites en les passant à travers un "pipeline" que vous pouvez personnaliser.
        5. **Contrôle** : Scrapy offre un niveau de contrôle plus fin sur le processus de scraping grâce à des fonctionnalités telles que les règles de robots, les requêtes retardées, les agents utilisateurs et plus encore.
        6. **Utilisation en production** : Idéal pour des projets plus complexes qui nécessitent un contrôle granulaire et une grande capacité de personnalisation.
        
        ### **Résumé**
        
        - Utilisez **`BeautifulSoup`** si vous avez besoin d'un outil simple et rapide pour extraire des données à partir de quelques pages web.
        - Utilisez **`Scrapy`** si vous avez besoin d'un framework complet pour un scraping à grande échelle, avec des fonctionnalités avancées et une grande flexibilité.
        
        Chacun a ses avantages et ses inconvénients, et le meilleur choix dépend des besoins spécifiques de votre projet.
        
        </aside>
        

- **Création des script win rate & win rate AvB**
    
    → Création du script win rate
    
    → Création du script win rate “equipe A” VS “equipe B” pour prendre en compte les précédentes confrontations entre deux équipes
    
    → Appliquer les coef sur le win rate ( on réduit l’importance du coef de chaque année en appliquant un cube à chaque coefficient pour calculer le coefficient de l’année suivante avec un horizon de 10ans max )
    
    → Appliquer les coef sur le win rate “equipe A” VS “equipe B” ( on réduit l’importance du coef en multipliant le coef au carré à chaque match ( en commençant par coef 0.9 au premier match ) pour valoriser les matchs les plus récents tout en comptabiliser les anciens avec un horizon de 10ans max )
    

- **Ajout de filtres liées à la météo**
    
    → Ajout de 4 filtres sur le script win rate avant de calculer les win rates
    
    → Nous avons maintenant un script python capable de calculer les win rates de chaque équipe en appliquant un coefficient et des filtres liées à la météo
    

- **Création du script final ( wilwin score )**
    
    → Combinaison des deux script en un seul ( winrate & winrate AvB ) avec réadaptation du codes des variables des inputs et de l’output.
    
    → Calcul de la moyenne des deux winrates pour créer le wilwin score.
    
    → Fonction pour mettre le wilwin score sur 100 et ainsi voir les scores comme des pourcentages de chances de gagner.
    
    → Potentiel vainqueur = l’équipe avec le willwin score le plus élevé.
    

- **Création d’une API avec Flask**
    
    → pip3 install Flask
    
    → création d’un fichier “app.py” liée à mon script (utilisation de Flask pour créer un route, etc…)
    
    → « FLASK_APP=[app.py](http://app.py/) » dans le terminal.
    
    → Tapez « flask run » appuyez sur Entrée.
    

- **Algorithme classique VS Algo de machine learning**
    
    https://www.youtube.com/watch?v=RC7GTAKoFGA
    
    ![Capture d’écran 2023-10-12 à 22.51.27.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/d79c49c4-adf5-47f2-bb0a-462fdc8d4e83/1728cc45-690f-452a-8aac-58b7ac973bb7/Capture_decran_2023-10-12_a_22.51.27.png)
    
    **Le machine learning c’est la base de l’IA**
    
    Ce n’est pas l’humain qui trouve les règles, c’est la machine qui le fait en se basant sur ce qu’elle vas apprendre. (machine learning) - Elle apprend à partir de données qu’on lui donne.
    
    ****Types d'Algorithmes de Machine Learning****
    
    1. **Régression Linéaire**: Utile pour des problèmes de prédiction où la sortie est continue et linéairement dépendante des entrées.
    2. **Régression Logistique**: Utilisé pour des problèmes de classification binaires.
    3. **Arbres de Décision**: Bon pour la classification et la régression, mais peut être sujet au surapprentissage.
    4. **Forêts Aléatoires**: Une évolution des arbres de décision qui améliore la généralisation.
    5. **K-Plus Proches Voisins (K-NN)**: Utile pour la classification et la régression, et fonctionne bien pour des petits ensembles de données.
    6. **Machine à Vecteurs de Support (SVM)**: Utilisé pour la classification et, dans certains cas, la régression.
    7. **Réseaux de Neurones**: Convient pour des problèmes complexes comme la reconnaissance d'images ou le traitement du langage naturel.
    8. **Ensemble Learning (Boosting, Bagging)**: Combine plusieurs modèles pour améliorer les performances.
    9. **Clustering (K-means, Hiérarchique)**: Utilisé pour regrouper des données non étiquetées en fonction de leurs similarités.
    
    **Python pour le Machine Learning**
    
    Python est un excellent choix pour le machine learning. Des bibliothèques comme scikit-learn, TensorFlow, et PyTorch sont très populaires.
    

- **Machine learning**
    
    
    → **Un K-NN aurait pu être pas mal si ont avant plus de data sur les matchs (joueurs, etc..)**
    
    **(**Si vous pensez que des matchs similaires ont des résultats similaires, K-NN pourrait être une option.)
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d79c49c4-adf5-47f2-bb0a-462fdc8d4e83/03544dff-dbed-4fa5-b344-6a91e4266346/Untitled.png)
    
    → **Prédire le score avec une régression linéaire**
    
    La // est le type d’algo de machine learning le plus simple pour débuter
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d79c49c4-adf5-47f2-bb0a-462fdc8d4e83/278405a7-0a69-4156-8632-c63f89229077/Untitled.png)
    
    → **Prédire le vainqueur avec une régression logistique**
    
    Lorsque le résultat est binaire
    
    ![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d79c49c4-adf5-47f2-bb0a-462fdc8d4e83/a1284ae6-8220-4091-b49c-298c3b0af1f0/Untitled.png)
    
    **Question :** Les regression ne se basent donc que sur un facteur ? Si ont veut mettre plusieurs facteurs, doit-on faire plusieurs regressions ?
    
    **Réponse :** ont pu faire des multi…
    
    **Problème :** les lignes ou il n’y à pas de données météorologiques sont problématique pour faire notre algo de machine learning
    
    **Solutions :** supprimer les lignes non complètes - les compléter avec un moy de temp, pluie, etc… - Les completer avec un algo de machine learning K-NN ( plus proche voisin )
    
    On vas commencer par faire un algo simplifié en supprimant les lignes. (même si cela revient à supprimer 44% du dataset, car 236 lignes sur 536).
    
    Par la suite on fera un K-NN
    
    **Enfaite, le système n’était pas du tout fiable avec les 236 lignes**
    
    Le modèle de régression linéaire a un *R*2 de environ 0.089 sur l'ensemble de test. Le *R*2 est une mesure de la qualité du modèle ; un *R*2 proche de 1 indique que le modèle explique une grande partie de la variance dans les données, tandis qu'un *R*2 proche de 0 indique le contraire.
    
    Dans ce cas, le *R*2 assez faible suggère que le modèle n'est pas très bon pour expliquer les scores des matchs de rugby. Il est possible que la prédiction du score d'un match de rugby soit une tâche complexe qui nécessite un modèle plus avancé ou plus de variables explicatives.
    
    **Tentons le K-NN**
    
    Préparation :
    
    Conversion des saisons en valeur binaire pour pouvoir la prendre en compte
    
    Séparation des données années, moi et jour et conversion pour les prendre en compte
    
    Suppression puis reintégration des équipes A et B car pas d’impact sur la météo
    
    Test :
    
    “Le modèle de régression linéaire sur les données imputées a un *R*2 d'environ 0.215 sur l'ensemble de test. C'est une amélioration par rapport au *R*2 de 0.089 que nous avions obtenu précédemment sur les données sans imputation.
    
    Bien que ce ne soit toujours pas proche de 1, cette augmentation du *R*2 suggère que l'imputation k-NN a eu un effet positif sur la performance du modèle.”
    
    Mais en fait c’était une feinte, les données météo on mal été réadapter pour le ML
    
    **Ok, on recommence tout avec un algo de fôret alétoire cette fois.**
    
    ****→ pip3 install scikit-learn (bibiliothèque open source)
    
    → script_ml.py → un script qui utilise la bibiliothèque scikit-learn pour …
    
    Dans ce script, les matchs domicile et extérieur sont comptabilisé différemment et toutes les lignes qui ne comprenaient pas de données météos ne sont pas prise en compte
    
    → script_ml_neutral.py → ne pas tenir compte de domicile ou extérieur
    
    → script_ml_neutral10.py → tenir compte seulement de 10 dernière années
    

- **Graphiques python**
    
    
    → Utilisation de la bibliothèque plotly
    
    → Intégration d’un code de création de graphique radar à la fin du script “script_winrate_n.py”. Un script tiré de notre script principale mais qui calcule tout les winrates de toutes les équipes sans filtre et avec les filtres au choix.
    
    → Link plotly avec l’API Flask
    
    → Intégration front
    

- **Intégrer les côtes sur le front**
    
    
    → Reprendre le script de scraping simple
    
    → Ajouter l’option d’entrer deux équipes en input pour ne recevoir que leurs côtes correspondante en output
    
    → Renvoyé les données en dictionnaire python
    
    → Créer un dictionnaire pour traduire le nom des équipe ( anglais en input, fr pour la recherche sur betclic, anglais en output )
    
    → Intégration du script dans un api flask ( le même que mon script de wilwin score et de ML )
    
    → Intégration de l’API sur le front 
    

- **PySpark**
    
    
    Installation de pyspark via le terminal
    Installation de java via leurs site + configuration via le terminal
    

- **Animation des scores avec vueNumber**
    
    
    → 
    
    [Animated Percent in CSS](https://codepen.io/CarterLi/pen/dyMrzpz)
    
