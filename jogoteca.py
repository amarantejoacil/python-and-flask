from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def ola():
    lista = ['Tetris', 'Super Mario', 'Pokemon Gold']
    return render_template('lista.html', titulo='Jogos', jogos=lista)

# trecho da app
#app.run(host='0.0.0.0', port=8080)
app.run()