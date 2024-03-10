from flask import (
    Flask,
    jsonify
)
from flask_cors import CORS

from outlook import outlook

service = Flask(__name__)

@service.route("/api/v1/parsemsg", methods=["GET"])
def msgfile():
    o = outlook.OutlookMsg("./data/ap.msg")
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