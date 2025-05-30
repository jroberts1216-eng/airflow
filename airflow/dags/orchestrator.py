import sys
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Append the path where your custom modules (like insert_records.py) live
sys.path.append('/opt/airflow/api-request')

def safe_main_callable():
    from insert_records import main
    return main()

default_args = {
    'description': 'A DAG to orchestrate data',
    'start_date': datetime(2025, 5, 29),
    'catchup': False
}

dag = DAG(
    dag_id='weather-api-orchestrator',
    default_args=default_args,
    schedule_interval=timedelta(minutes=5)
)

with dag:
    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=safe_main_callable
    )
