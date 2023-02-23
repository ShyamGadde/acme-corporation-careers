import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

db_conn_str = f'mysql+pymysql://{os.getenv("PS_USERNAME")}:{os.getenv("PASSWORD")}@{os.getenv("HOST")}/{os.getenv("DATABASE")}?charset=utf8mb4'

engine = create_engine(
    db_conn_str,
    connect_args={
        'ssl': {'ssl_ca': "/etc/ssl/cert.pem"}
    },
)

def get_all_jobs():
    with engine.connect() as conn:
        return conn.execute(text("SELECT * FROM jobs"))

def get_job_details(job_id):
    with engine.connect() as conn:
        return conn.execute(text("SELECT * FROM jobs WHERE id = :job_id"), {"job_id": job_id}).first()
