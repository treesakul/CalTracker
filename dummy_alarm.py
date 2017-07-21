'''
from datetime import date
from apscheduler.schedulers import Scheduler

# Start the scheduler
sched = Scheduler()
sched.start()

# Define the function that is to be executed
def my_job(text):
    print (text)

# The job will be executed on November 6th, 2009
exec_date = date(2017, 5, 30)

# Store the job in a variable in case we want to cancel it
job = sched.add_date_job(my_job, exec_date, ['text'])
'''
from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler()
