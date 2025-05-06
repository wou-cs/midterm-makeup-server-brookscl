from flask import Flask, abort, request


app = Flask(__name__)


@app.route("/api/upper/<string:value>", methods=["GET"])
def upper(value):
    return {'result': value.upper()}


@app.route("/api/lower/<string:value>", methods=["GET"])
def lower(value):
    return {'result': value.lower()}
