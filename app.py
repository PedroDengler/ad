from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def mostrar_universidad():
    universidad = {
        'titulo': 'Universidad de Buenos Aires - UBA',
        'imagen': 'img.jpg',
        'descripcion': 'UBA es una universidad argentina.',
        'carreras': ['Informatica', 'Biologia', '...'],
    }
    return render_template('index.html', universidad=universidad)

if __name__ == '__main__':
    app.run(debug=True)