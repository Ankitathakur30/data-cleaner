from flask import Blueprint, request, jsonify
import pandas as pd
import os
from config import UPLOAD_FOLDER

routes=Blueprint("routes", __name__)

@routes.route("/", methods=["GET"])
def home():
    return ["Welcome to the Data Cleaner Project.."]

@routes.route("/upload", methods=["GET"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"Error":"No file provided"}), 400
    file=request.files["file"]
    filepath=os.path.join(UPLOAD_FOLDER,file.filename)
    file.save(filepath)

    df=pd.read_csv(filepath)
    return jsonify({
        "rows": df.shape[0],
        "columns": list(df.columns)
    })