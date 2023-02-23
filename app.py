from flask import Flask, render_template, jsonify


app = Flask(__name__)

company_name = "Acme Corporation"
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'salary': 'Rs. 12,00,000'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Pune, India',
        'salary': 'Rs. 14,00,000'
    },
]


@app.route('/')
def index():
    return render_template("index.html", jobs=JOBS, company_name=company_name)


@app.route('/api/jobs')
def api_jobs():
    return jsonify(JOBS)
