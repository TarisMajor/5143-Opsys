import requests
import json
import os
from rich import print
from cpu_jobs import getJob, getBurst, getBurstsLeft, getJobsLeft
def getConfig(client_id):
    return {
        "client_id": client_id,
        "min_jobs": 1,
        "max_jobs": 1,
        "min_bursts": 10,
        "max_bursts": 50,
        "min_job_interval": 1,
        "max_job_interval": 5,
        "burst_type_ratio": 0.5,
        "min_cpu_burst_interval": 15,
        "max_cpu_burst_interval": 50,
        "min_io_burst_interval": 30,
        "max_io_burst_interval": 70,
        "min_ts_interval": 5,
        "max_ts_interval": 5,
        "prioritys": [1,2,3,4,5]
    }

def init(config):
    """
    This function will initialize the client and return the `client_id` and `session_id`
    """
    route = f"http://profgriffin.com:8000/init"
    r = requests.post(route,json=config)
    if r.status_code == 200:
        response = r.json()
        return response
    else:
        print(f"Error: {r.status_code}")
        return None
    
def Scheduler():
    
    ReadyQueue = []
    WaitingQueue = []
    IO_Queue = []
    FinishedQueue = []
    Running = []
    
    preliminary_jobs = {}
    
    client_id = "StrombusGigas"
    config = getConfig(client_id)
    base_url = 'http://profgriffin.com:8000/'
    response = init(config)
    
    start_clock = response['start_clock']
    session_id = response['session_id']

    clock = start_clock   