# app.py
from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo
estudiantes = [
    {
        'nombre': 'Rodrigo Ovalle',
        'carnet': '1557020',
        'universidad': 'Universidad Rafael Landivar',
        'facultad': 'Ingeniería',
        'curso': 'Sistemas operativos'
    }
]

@app.route('/')
def index():
    return render_template('index.html', estudiantes=estudiantes)

if __name__ == '__main__':
    app.run(debug=True)