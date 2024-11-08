# Leap Year API

Une API Django pour déterminer si une année est bissextile, avec des fonctionnalités d'historique des appels. Cette API fournit trois endpoints :
- Vérification d'une année bissextile.
- Vérification d'une plage d'années pour identifier les années bissextiles.
- Historique des appels aux deux premiers endpoints.

## Prérequis

- Python 3.8+
- Django 3.2+
- Django REST Framework

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/ProxTricky/leap-year-api.git
    cd leapyear_api
    ```

2. Créez et activez un environnement virtuel :
    ```bash
    poetry shell
    ```

3. Installez les dépendances :
    ```bash
    poetry install
    ```

4. Créez les migrations et appliquez-les pour créer les tables nécessaires :
    ```bash
    python manage.py migrate
    ```

## Usage

1. Lancez le serveur de développement :
```bash
python manage.py runserver
```

2. Utilisez les endpoints suivants :

   - **Vérification d'une année** :  
     `GET /api/leap-year/<année>/`
     - Ex : `/api/leap-year/2020/`
     - Réponse : `{ "year": 2020, "is_leap": true }`
   
   - **Vérification d'une plage d'années** :  
     `GET /api/leap-year-range/<année-début>/<année-fin>/`
     - Ex : `/api/leap-year-range/2000/2020/`
     - Réponse : `{ "start_year": 2000, "end_year": 2020, "leap_years": [2000, 2004, 2008, 2012, 2016, 2020] }`

   - **Historique des appels** :  
     `GET /api/history/`
     - Réponse : `{"history": [{"endpoint": "date", "input_data": "2020", "result": {"year": 20 20, "is_leap": true}, "created_at": "YYYY-MM-DD HH:MM:SS UTC"}, ...]}`

## Tests

Pour exécuter les tests unitaires, utilisez la commande suivante :
    ```bash
    python manage.py test
    ```

Structure du projet

`leapyear_checker/models.py` : modèle LeapYearHistory pour stocker l'historique des appels.

`leapyear_checker/views.py` : vues pour chaque endpoint.

`leapyear_checker/tests.py` : tests unitaires pour vérifier le fonctionnement des endpoints.

`leapyear_checker/utils.py` : logique pour déterminer si une année est bissextile.


Exemples de réponse

   - **Vérification d'une année** :
        Requête : /api/leap-year/2024/
        Réponse :
```json 
{ "year": 2024, "is_leap": true }
```

   - **Vérification d'une plage d'années** :
        Requête : /api/leap-year-range/2000/2024/
        Réponse : 
```json
{ "start_year": 2000, "end_year": 2024, "leap_years": [2000, 2004, 2008, 2012, 2016, 2020, 2024] }
```

   - **Historique des appels** :
        Requête : /api/history/
        Exemple de réponse :

        ```json
        {
          "history": [
            {
              "endpoint": "date",
              "input_data": "2020",
              "result": {"year": 2020, "is_leap": true},
              "created_at": "2024-10-30 10:15:30 UTC"
            },
            {
              "endpoint": "range",
              "input_data": "2000-2024",
              "result": {"start_year": 2000, "end_year": 2024, "leap_years": [2000, 2004, 2008, 2012, 2016, 2020, 2024]},
              "created_at": "2024-10-30 10:16:00 UTC"
            }
          ]
        }
        ```

Auteurs

Développé par ProxTricky.
