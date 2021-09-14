from flask import Flask, url_for, redirect, render_template, request
from server import get_pokemon

app = Flask(__name__)
app.secret_key = 'cfe8w7r56489[;´0-=6'

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        return render_template('index.html')
    except:
        return redirect(url_for('error'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    try:
        if request.method == 'GET':
            return redirect(url_for('error'))
        
        if request.method == 'POST':
            pokemon = request.form['pokemon']
            result = get_pokemon(pokemon)

            if 'Error' in result:
                return redirect(url_for('error'))

            return render_template(
                'search.html',
                data=result
            )

    except:
        return redirect(url_for('error'))

@app.route('/error', methods=['GET', 'POST'])
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)