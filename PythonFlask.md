TP : Créer une Application Web Simple avec Flask

Objectif : 

Créer une application web simple qui affiche une page d'accueil avec un message de bienvenue et une page "À propos" avec des informations sur vous.

Prérequis :

- Connaissance de base en Python
- Installation de Python sur votre machine
- Installation de Flask (vous pouvez l'installer via pip : pip install Flask)
- Installation de Git sur votre machine
- créer un dépôt GitHub

Étapes

1. Créer la Structure du Projet

- Créez un dossier pour votre projet.
- Initialiser votre dépôt git.
- À l'intérieur de ce dossier, créez un fichier nommé app.py.

2. Écrire le Code de l'Application

- Ouvrez app.py et ajoutez le code suivant :

``` python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur ma page d'accueil !"

@app.route('/about')
def about():
    return "À propos de moi : Je suis en train d'apprendre à développer des applications web avec Flask !"

if __name__ == '__main__':
    app.run(debug=True)
```

3.  Ajoutez le fichier à Git et faites un premier commit

4. A propos

- Créer une Branche pour la Page "À Propos"
- Modifiez app.py pour ajouter la route "À propos" :

``` python
@app.route('/about')
def about():
    return "À propos de moi : Je suis en train d'apprendre à développer des applications web avec Flask !"
``` 

5. Committez les modifications.

6. Fusionner la Branche about-page dans le main

Créer la Structure du Projet

Créez un dossier pour votre projet.
À l'intérieur de ce dossier, créez un fichier nommé app.py.
Écrire le Code de l'Application

Ouvrez app.py et ajoutez le code suivant :
Copier

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur ma page d'accueil !"

@app.route('/about')
def about():
    return "À propos de moi : Je suis en train d'apprendre à développer des applications web avec Flask !"

if __name__ == '__main__':
    app.run(debug=True)
```

7. Exécuter l'Application

Ouvrez un terminal et naviguez jusqu'au dossier de votre projet.

Exécutez la commande suivante pour démarrer l'application :
```bash
python app.py
```

Ouvrez un navigateur web et allez à l'adresse http://127.0.0.1:5000/ pour voir votre page d'accueil.

Allez à l'adresse http://127.0.0.1:5000/about pour voir la page "À propos".