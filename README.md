# airflowprojecttemplate
My personal template for building Airflow jobs/dags.

This repo/folder should be placed in the airflow dag folder. 
All files not intended to be directly scanned by the airflow scheduler should be placed in the task subfolder(ie: .sql and .jar files).

Alot of my experinace with airflow has been baked into this template.

I have also placed some comments on the implcit assuptions airflow regarding tasks/dags architecture in my task file; said comments should be usefull to anyone trying to learn airflow.