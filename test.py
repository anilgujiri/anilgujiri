# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 19:26:32 2022

@author: anilgujiri18
"""

from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.operators.dummy_operator import DummyOperator
import ftplib
import socket

str_dt=datetime(2022,8,17)
sch_intvl='00 5 * * *'

default_args = {
    'owner': 'airflow',
    'start_date': str_dt,
    'depends_on_past': False,
}

count = 0

def func():
    return 1+2

with DAG(dag_id='bhuvitest',  default_args=default_args) as main_dag:
    
        
    bhuvitest = PythonOperator(task_id='python_task', python_callable=func,dag = main_dag)

    bhuvitest2 = PythonOperator(task_id='python_task2', python_callable=func,dag = main_dag)
    
    dummy = [DummyOperator(task_id=str('dummy'+str(i)), trigger_rule="one_success", dag=main_dag) for i in range(2)]
    
    bhuvitest3 = PythonOperator(task_id='python_task3', python_callable=func,dag = main_dag)
    
    bhuvitest4 = PythonOperator(task_id='python_task4', python_callable=func,dag = main_dag)    


bhuvitest >> dummy[0]
bhuvitest2 >> dummy[0]
dummy[0] >> bhuvitest3
dummy[0] >> bhuvitest4 
bhuvitest3 >> dummy[1]
bhuvitest4 >> dummy[1]
