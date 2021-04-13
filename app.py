from flask import Flask, jsonify
from core import file_manager, parsers

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

def run():
    app.run(debug=True)

@app.route('/', methods=['GET'])
def index():
    return jsonify('this is the index page')

@app.route('/batting', methods=['GET'])
def batting():    
    data = parsers.clean_reference_files(file_manager.read_csv('reference_batting.csv', header=True))
    return jsonify(data)

@app.route('/pitching', methods=['GET'])
def pitching():    
    data = parsers.clean_reference_files(file_manager.read_csv('reference_pitching.csv', header=True))
    return jsonify(data)