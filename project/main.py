# Impor
from flask import Flask, render_template, request

app = Flask(__name__)


# Halaman Utama
@app.route('/')
def index():
    return render_template('index.html')

# Artikel 1
@app.route('/artikel1')
def artikel1():
    return render_template('artikel.html')

# Artikel 2
@app.route('/artikel2')
def artikel2():
    return render_template('artikel2.html')

# Artikel 3
@app.route('/artikel3')
def artikel3():
    return render_template('artikel3.html')

# Artikel 4
@app.route('/artikel4')
def artikel4():
    return render_template('artikel4.html')

app.run(debug=True)
