from flask import Blueprint, request, jsonify
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from config import UPLOAD_FOLDER
from utils.profiling import profile_data
from utils.issues import detect_issues

routes=Blueprint("routes", __name__)

@routes.route("/", methods=["GET"])
def home():
    return ["Welcome to the Data Cleaner Project.."]

@routes.route("/upload", methods=["POST"])
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

@routes.route("/profile",methods=["POST"])
def profile():
    if "file" not in request.files:
        return jsonify({"Error":"No file provided"}), 400
    file=request.files["file"]
    if file.filename=="":
        return {"Error":"No file selected"}, 400
    try:
        df=pd.read_csv(file)
        result=profile_data(df)
    except Exception as e:
        return{"Error":str(e)}, 500
    return jsonify(result)

@routes.route("/issues", methods=["POST"])
def issues_route():
    if "file" not in request.files:
        return{"Error":"No file"}, 400
    file=request.files["file"]
    df=pd.read_csv(file)
    result=detect_issues(df)
    return result