from flask import Flask, jsonify

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

def run():
    app.run(debug=True)

@app.route('/', methods=['GET'])
def index():
    return jsonify('this is the index page')
