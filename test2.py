# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 19:26:32 2022

@author: anilgujiri18
"""

from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.contrib.operators.ssh_operator import SSHOperator
import ftplib
import socket

str_dt=datetime(2022,8,17)
sch_intvl='00 5 * * *'

default_args = {
    'owner': 'airflow',
    'start_date': str_dt,
    'depends_on_past': False,
}

lines = []

with open('read.txt') as f:
    lines = [line.rstrip('\n') for line in f]


def func2():
    return 1+2

def func(**kwargs):
    taskname = None
    for i in range(len(lines)):
        if kwargs['tname'] in lines[i]:
            taskname = lines[i]
    
    t1 =  SSHOperator(ssh_conn_id='ssh_test_win',
                               task_id='Unzip_files',
                               command=taskname,
                               dag=main_dag)
    
    t1.execute(dict())

with DAG(dag_id='bhuvitest2',  default_args=default_args) as main_dag:

    bhuvitest = PythonOperator(task_id='python_task', python_callable=func,op_kwargs={'tname': 'taskname'},dag = main_dag)

    bhuvitest2 = PythonOperator(task_id='python_task', python_callable=func,op_kwargs={'tname': 'taskname2'},dag = main_dag)

bhuvitest >> bhuvitest2