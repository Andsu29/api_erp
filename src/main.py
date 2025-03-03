from routes.main import app
from flask_cors import CORS


CORS(app)  # Permite todas as origens
# CORS(app, origins=["http://localhost:5173"])

if __name__ ==  '__main__':
    app.run(host='0.0.0.0', port=8000)