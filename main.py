from flask import (
    Flask,
    request,
    jsonify,
)
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

from outlook import outlook

service = Flask(__name__)

@service.route("/api/v1/parsemsg", methods=["POST"])
def msgfile():
    file = request.files["file"]
    if file:
        o = outlook.OutlookMsg(file)
        data = {
            "header" : o.get_header(),
            "sender" : o.get_sender(),
            "date" : o.get_date(),
            "subject" : o.get_subject(),
            "body" : o.get_body()
        }
        return jsonify(data)

if __name__ == "__main__":
    service.run()