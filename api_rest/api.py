from flask import Flask, Response, request
from flask_cors import CORS
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from pymongo import MongoClient

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app)

# Define las métricas que deseas recopilar
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Latencia de las solicitudes')
REQUEST_TOTAL = Counter('request_total', 'Cantidad total de solicitudes')

# MONGO
client = MongoClient('mongo', 27017)
db = client.flask_db
players_db = db.players

@app.route('/players', methods=["POST"])
@REQUEST_LATENCY.time()
def create_player():
    # Incrementa el contador de solicitudes totales
    REQUEST_TOTAL.inc()

    # Get player name from body
    data = request.json
    
    # ADD PLAYER TO MONGO
    players_db.insert_one({'name': data.get('player'), 'score': 0})
    return {"player": data.get('player')}

@app.route('/players', methods=["GET"])
@REQUEST_LATENCY.time()
def get_player():
    # Incrementa el contador de solicitudes totales
    REQUEST_TOTAL.inc()

    players = players_db.find()
    players = list(map(lambda x: {'name': x.get('name'), 'score': x.get('score')}, players))
    return players

@app.route('/')
@REQUEST_LATENCY.time()
def hello_world():
    # Incrementa el contador de solicitudes totales
    REQUEST_TOTAL.inc()
    
    return '¡Hola, mundo!'

@app.route('/metrics')
def metrics():
    data = generate_latest()
    return Response(data, 200, content_type=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
