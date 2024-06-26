from datetime import datetime,timedelta


from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'nash5657',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)

}
def get_name(ti):
    ti.xcom_push(key='first_name',value='Nash')
    ti.xcom_push(key='last_name',value='5657')

def get_age(ti):
    ti.xcom_push(key='age',value=19)


def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name',key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name',key='last_name')
    age = ti.xcom_pull(task_ids='get_age',key='age')
    print(f"Hello World from {first_name}{last_name} and I am {age} years old")

with DAG(
    default_args=default_args,
    dag_id='create_dag_with_python_operator_v06',
    description='My first DAG with Python Operator',
    start_date=datetime(2024, 6, 26),
    schedule_interval='@daily'

) as dag:
    task1 = PythonOperator(
        task_id='first_task',
        python_callable=greet,
        #op_kwargs={'age':25}
    )
    
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )
    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )
    [task2,task3]>>task1
