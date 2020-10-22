from flask import Flask, request, jsonify, abort
import time
import pickle as pickle

#model = pickle.load(open("../Model/model.pkl", "rb"))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return '<h1>SEEM LOS API</h1>'

@app.route('/model', methods=['GET'])
def model():
    return {
        'Author' : 'Emmanuel',
        'Team' : 'BSE20-25'
    }

@app.route('/forecast', methods=['POST'])
def forecast():
    return {
        'Author' : 'Emmanuel',
        'Team' : 'BSE20-25'
    }

if __name__ == '__main__':
    app.run(debug=True)

# export FLASK_DEBUG = 1
# flask run