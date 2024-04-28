from flask import Flask, render_template
from app import buscar_por_columna
from flask_cors import CORS
import socket
import os
from dotenv import load_dotenv


app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")
# Ruta para obtener datos por ID
@app.route('/datos/<int:id>', methods=['GET'])
def obtener_datos_por_id(id):
    resultado = buscar_por_columna(id)
    return resultado

# DOTENV
load_dotenv()


if __name__ == '__main__':
    _port = os.getenv('PORT')
    _host = os.getenv('HOST')
    ip_address = socket.gethostbyname(socket.gethostname())
    app.run(debug=False, host=_host, port=_port)
    print(f"Servidor flask corriendo en http://{ip_address}:{_port}")