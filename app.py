from flask import Flask, jsonify, render_template

from database import get_all_jobs

app = Flask(__name__)

company_name = "Acme Corporation"


@app.route('/')
def index():
    return render_template("index.html", jobs=get_all_jobs(), company_name=company_name)


@app.route('/api/jobs')
def api_jobs():
    return jsonify(list(map(dict, get_all_jobs().mappings())))
