from flask import Flask, render_template, jsonify
from database import load_jobs


app = Flask(__name__)

company_name = "Acme Corporation"


@app.route('/')
def index():
    return render_template("index.html", jobs=load_jobs(), company_name=company_name)


@app.route('/api/jobs')
def api_jobs():
    return jsonify(list(load_jobs()))
