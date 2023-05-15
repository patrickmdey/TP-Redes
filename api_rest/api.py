from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Define las métricas que deseas recopilar
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Latencia de las solicitudes')
REQUEST_TOTAL = Counter('request_total', 'Cantidad total de solicitudes')

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
