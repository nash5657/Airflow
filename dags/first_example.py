
from datetime import datetime,timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'nash5657',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)

}


with DAG(
    dag_id='first_example_v3',
    default_args=default_args,
    description='My first DAG',
    start_date=datetime(2024, 6, 26,2),
    schedule_interval='@daily'
         
         
         ) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command='echo "Hello World"'
    )
    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo "I am the second task"'
    )
    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo "I am the third task"'
    )
    task1.set_downstream(task2)
    task1.set_downstream(task3)