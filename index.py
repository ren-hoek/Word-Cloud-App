from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

#Needs setting as CSRF_ENABLED=True for flask-wtf. Keep secret_key, secret
app.secret_key = ''

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/data')
def data():
    with open('wordc.json', 'r') as json_file:
        data = json.load(json_file) 
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
