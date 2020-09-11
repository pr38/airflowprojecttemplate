from airflowprojecttemplate.tasks import task1, task2, clean_output

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator


from datetime import datetime, timedelta

# change dag_version to completely reset the job/dag
dag_version = "01"

email_address_list = []

dag_name = "airflowprojecttemplate"
start_date = datetime(2020, 7, 1)
owner = "dummy_owner"
schedule_interval = "1 10 1 * *"


default_args = {
    "owner": owner,
    "depends_on_past": False,
    "start_date": start_date,
    "email": email_address_list,
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 2,
    "catchup": True,
    "retry_delay": timedelta(minutes=5)
}


dag = DAG(
    "%s_v%s" % (dag_name, dag_version),
    default_args=default_args,
    max_active_runs=1,
    schedule_interval=schedule_interval
)

task1_task = PythonOperator(
    task_id="task1", python_callable=task1, provide_context=True, dag=dag
)

task2_task = PythonOperator(
    task_id="task2", python_callable=task2, provide_context=True, dag=dag
)

clean_output_task = PythonOperator(
    task_id="clean_output", python_callable=clean_output, provide_context=True, dag=dag
)


EMAIL_CONTENT = """
<h2>Job Completion Report: </h2>
<p>
    DAG: {{ params.dag_name }} <br/>
    task: {{ task_instance_key_str }} <br/>
    owner: {{ task.owner}} <br/>
    Host: {{ ti.hostname }} <br/>
    Log file: {{ ti.log_filepath }} <br/>
    Log: <a href="{{ ti.log_url }}">Link</a> <br/>
    STATE: {{ ti.state }}
    execution_date: {{ ti.execution_date }} <br/>
    try_number: {{ ti.try_number }} <br/>
    start_date: {{ ti.start_date }} <br/>
    duration: {{ ti.duration }} <br/>
    
</p>
"""

email_task = EmailOperator(
    task_id="email_for_" + dag_name,
    to=email_adress_list,
    params={"dag_name": dag_name},
    subject="Airflow report on DAG {{ params.dag_name }}  completion {{ds}}",
    html_content=EMAIL_CONTENT,
    dag=dag,
)

clean_output_task >> task1_task >> task2_task >> email_task
