# airflowprojecttemplate
My personal template for building Airflow jobs/dags.

This repo/folder should be placed in the Airflow dag folder. 
All files not intended to be directly scanned by the airflow scheduler should be placed in the task subfolder(ie: .sql and .jar files).

Alot of my experinaces with airflow has been baked into this template.

I have also placed some comments in my task file on the implcit assuptions airflow makes regarding tasks/dags architecture; said comments should be useful to anyone trying to learn Airflow.
  
