from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite acesso de qualquer origem

# Importe e inicialize as rotas
from app.routes import init_routes
init_routes(app)

@app.route('/')
def home():
    return "Servidor Flask funcionando!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)