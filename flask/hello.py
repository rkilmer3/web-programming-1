from flask import Flask 
from json import JSONEncoder

app = Flask(__name__)

@app.route("/")
def hello_world():
    me = "Rosa"
    return f"<p>Hello, {me} from the World!</p>"

@app.route("/goodbye")
def goodbye_world():
    me = "Rosa"
    return f"<p>Goodbye, {me} from the World! Come back soon!</p>"

@app.route("/hello")
def hello_world2():
    me = "Rosa"
    return f"<p>Hello, {me} from the World!</p>"

@app.route("/data")
def get_data():
    data = [
        {"name:":"suzy":"type":"dog"},
        {"name:":"sandy":"type":"cat"}
    ]
    return jsonify(data)