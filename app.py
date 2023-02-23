from flask import Flask, jsonify, render_template

from database import get_all_jobs, get_job_details

app = Flask(__name__)

company_name = "Acme Corporation"


@app.route('/')
def index():
    return render_template("index.html", jobs=get_all_jobs(), company_name=company_name)


@app.route('/api/jobs')
def api_jobs():
    return jsonify(list(map(dict, get_all_jobs().mappings())))


@app.route('/job/<int:job_id>')
def apply(job_id):  # sourcery skip: use-named-expression
    job_details = get_job_details(job_id)
    if job_details:
        return render_template("apply.html", job_details=job_details)
    return render_template("404.html")
