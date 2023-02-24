import locale

from flask import Flask, jsonify, render_template, request

from database import get_all_jobs, get_job_details, upload_application

app = Flask(__name__)

COMPANY_NAME = "Acme Corporation"


@app.route("/")
def index():
    return render_template("index.html", jobs=get_all_jobs(), company_name=COMPANY_NAME)


@app.route("/api/jobs")
def api_jobs():
    return jsonify(list(map(dict, get_all_jobs().mappings())))


@app.route("/job/<int:job_id>")
def apply(job_id):
    if job_details := get_job_details(job_id):
        return render_template("apply.html", job_details=job_details, company_name=COMPANY_NAME)
    return render_template("404.html"), 404


@app.route("/job/<int:job_id>/apply", methods=["POST"])
def handle_apply(job_id):
    upload_application(job_id, request.form)
    return render_template("apply_success.html", company_name=COMPANY_NAME)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.template_filter("indian_number")
def _jinja2_locale_filter(value):
    digits = list(str(value))
    for i in reversed(range(-3, -len(digits), -2)):
        digits.insert(i, ',')
    return ''.join(digits)
