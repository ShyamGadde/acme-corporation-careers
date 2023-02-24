import locale

from flask import Flask, jsonify, render_template, request

from database import get_all_jobs, get_job_details

app = Flask(__name__)

company_name = "Acme Corporation"


@app.route("/")
def index():
    return render_template("index.html", jobs=get_all_jobs(), company_name=company_name)


@app.route("/api/jobs")
def api_jobs():
    return jsonify(list(map(dict, get_all_jobs().mappings())))


@app.route("/job/<int:job_id>")
def apply(job_id):
    if job_details := get_job_details(job_id):
        return render_template("apply.html", job_details=job_details)
    return render_template("404.html")


@app.route("/job/<int:job_id>/apply")
def handle_apply(job_id):
    pass


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.template_filter("locale")
def _jinja2_locale_filter(value):
    # locale.setlocale(locale.LC_ALL, 'en_IN')
    locale.setlocale(locale.LC_ALL, "")
    return locale.format_string("%d", value, grouping=True)
