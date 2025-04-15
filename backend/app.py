from flask import Flask, render_template, request, redirect, url_for, send_file
import os

# Crée l'application Flask
app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Exemple d'action déclenchée par un bouton
@app.route('/convert', methods=['POST'])
def convert_file():
    # Ici tu appelleras tes fonctions de conversion
    # Exemple fictif :
    print("Conversion déclenchée !")
    return redirect(url_for('index'))

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'backend/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "Aucun fichier envoyé", 400
    file = request.files['file']
    if file.filename == '':
        return "Nom de fichier vide", 400
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    print(f"Fichier reçu : {file_path}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
