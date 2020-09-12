import time


def task1(ds, **kwargs):
    """
    Use the execution_datetime Pendulum/datetime object for determine what time-range of data to pull, i.e. query date injection.
    The assumption that all (non-logging) datetime info that a job uses comes from Airflow directly, is what allows Airflow to backfill.
    Airflow assumes that the datetime it feeds the task is for the start of the time-rage of the data being processed.
    For example, a monthly job scheduled for the first day of the month triggered on August first will pass July first date-time info to its tasks.
    Furthermore, Airflow will refer to that run as the July run in the gui/portal.
    """

    execution_datetime = kwargs["execution_date"]

    # do stuff with execution_datetime

    time.sleep(1)


def task2(ds, **kwargs):
    execution_datetime = kwargs["execution_date"]

    # do stuff with execution_datetime

    time.sleep(1)


def clean_output(ds, **kwargs):
    """
    Use the clean_output tasks to remove all data that would have been outputted if the dag was executed with the same execution_datetime.
    The clean_output tasks will be run before all other tasks.
    This ensures that data is not double filled when an Airflow dag run is reran/cleared.
    The ability to easily rerun a dag is one of the main advantages of Airflow.
    """

    execution_datetime = kwargs["execution_date"]

    # do stuff with execution_datetime

    time.sleep(1)
