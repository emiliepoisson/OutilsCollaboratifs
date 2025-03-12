import folium
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur ma page d'accueil !"

@app.route('/calcul', methods=['GET', 'POST'])
def calculette():
    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Erreur : Division par zéro"

    return render_template('calculette.html', result=result)

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        # Récupérer la sélection de l'utilisateur
        destination = request.form.get('destination')
        # Création d'une carte centrée sur Calais
        m = folium.Map(location=[50.95, 1.85], zoom_start=13)
        # Ajouter un marqueur pour Calais
        folium.Marker([50.95, 1.85], popup='Calais ici !').add_to(m)
        # Ajouter des marqueurs et un chemin en fonction de la sélection
        if destination == 'gareC':
            folium.Marker([50.955, 1.855], popup='Gare de Calais').add_to(m)
            folium.PolyLine([(50.95, 1.85), (50.955, 1.855)], color="blue", dash_array='5').add_to(m)
        elif destination == 'plage':
            folium.Marker([50.96, 1.845], popup='Plage de Calais').add_to(m)
            folium.PolyLine([(50.95, 1.85), (50.96, 1.845)], color="red", dash_array='5').add_to(m)
        elif destination == 'gareF':
            folium.Marker([50.93, 1.85], popup='Gare de Calais Frethun').add_to(m)
            folium.PolyLine([(50.95, 1.85), (50.93, 1.85)], color="green", dash_array='5').add_to(m)
        # Sauvegarder la carte dans le dossier static
        m.save('static/map.html')
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
