from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import zipfile
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/endpoint": {"origins": "http://localhost:5000"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/",methods=["GET"])
def home():
    return jsonify("Home")


@app.route("/endpoint",methods=["POST","OPTIONS"])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def endpoint():
    file = request.files['file']
    email = request.form['email']
    address = request.form['address']

    file_like_object = file.stream._file
    zipfile_ob = zipfile.ZipFile(file_like_object)
    file_names = zipfile_ob.namelist()
    print(file_names)
    return jsonify("success")


if __name__ == "__main__":
    app.run(port=5000, debug=True)