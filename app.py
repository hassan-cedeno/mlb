from flask import Flask, jsonify


from core import controller

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

def run():
    app.run(debug=True)

@app.route('/', methods=['GET'])
def index():
    return jsonify('this is the index page')

@app.route('/batting', methods=['GET'])
def batting():    
    return jsonify(controller.get_batting_players())

@app.route('/pitching', methods=['GET'])
def pitching():    
    return jsonify(controller.get_pitching_players())

@app.route('/active_players', methods=['GET'])
def active_players():
    data = controller.get_active_players()
    return jsonify({'batting': {'players': data.get('batting'), 'size': len(data.get('batting'))}, 'pitching': {'players': data.get('pitching'), 'size': len(data.get('pitching'))}})