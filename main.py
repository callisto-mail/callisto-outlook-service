from flask import (
    Flask,
    jsonify
)
from flask_cors import CORS

service = Flask(__name__)



if __name__ == "__main__":
    service.run()