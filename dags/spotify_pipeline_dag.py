from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import subprocess


default_args = {
    "owner": "Rushi",
    "start_date": datetime(2026, 3, 6)
}

dag = DAG(
    dag_id="spotify_playlist_pipeline",
    default_args=default_args,
    schedule=None,
    catchup=False
)


def run_pipeline():
    subprocess.run(["python", "/opt/airflow/scripts/main.py"], check=True)

run_task = PythonOperator(
    task_id="run_spotify_pipeline",
    python_callable=run_pipeline,
    dag=dag
)

