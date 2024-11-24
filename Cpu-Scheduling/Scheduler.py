import requests
import json
from rich import print
from cpu_jobs import getJob, getBurst, getBurstsLeft, getJobsLeft
from job import Job

def getConfig(client_id):
    return {
        "client_id": client_id,
        "min_jobs": 10,
        "max_jobs": 30,
        "min_bursts": 10,
        "max_bursts": 20,
        "min_job_interval": 5,
        "max_job_interval": 10,
        "burst_type_ratio": 0.7,
        "min_cpu_burst_interval": 5,
        "max_cpu_burst_interval": 10,
        "min_io_burst_interval": 5,
        "max_io_burst_interval": 15,
        "min_ts_interval": 1,
        "max_ts_interval": 1,
        "priority_levels": [1]
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
    
if __name__ == "__main__":
    
    ReadyQueue = []
    WaitingQueue = []
    IO_Queue = []
    FinishedQueue = []
    Running = []
    NewQueue = []
    
    preliminary_jobs = {}
    
    client_id = "strombus"
    config = getConfig(client_id)
    base_url = 'http://profgriffin.com:8000/'
    response = init(config)
    
    print(response)
    
    start_clock = response['start_clock']
    session_id = response['session_id']

    clock = start_clock   
    
    totalTime = 0
    
    Working = True
    
    once = 0
    
    while(Working == True):
        jobsleft = getJobsLeft(client_id, session_id) # Gets an integer
        
        response = None
        
        if once < 1:
            once += 1
            num_jobs = jobsleft
            print(num_jobs)

        if jobsleft == 0:
            pass
        else:
            response = getJob(client_id,session_id,clock)
            if response and response['success']:
                if response['data']:
                    for data in response['data']:
                        job_id = data['job_id']
                        if job_id not in preliminary_jobs:
                            # example data
                            # {
                            #   "job_id": 1,
                            #   "session_id": 9,
                            #   "arrival_time": 5275,
                            #   "priority": 1
                            # }
                            preliminary_jobs[job_id] = {'data': data, 'bursts':{}}
                        
                    for job_id in preliminary_jobs:
                        
                        burstsleft = getBurstsLeft(client_id, session_id, job_id) # Recieves an integer
                        if not burstsleft:
                            continue
                        for i in range(burstsleft):
                            bresp = getBurst(client_id, session_id, job_id) # recieves a dictionary
                            if isinstance(bresp, dict) and 'success' in bresp and bresp['success']:
                                #"data": {
                                #     "burst_id": 1,
                                #     "burst_type": "CPU",
                                #     "duration": 1
                                #   }
                                burst = bresp['data'] #gets the burst id, burst type and duration
                                bid = burst['burst_id']
                                preliminary_jobs[job_id]['bursts'][bid] = burst
                            
                    for job_id in preliminary_jobs:
                        job = preliminary_jobs[job_id]
                        if 'bursts' in job:
                            data = job['bursts']
                            arrival_time = job['data']['arrival_time']
                            id = job['data']['job_id']
                            priority =job['data']['priority']
                            temp_type = []
                            temp_time = []
                            for burst_id in data:
                                temp_type.append(data[burst_id]['burst_type'])
                                temp_time.append(data[burst_id]['duration'])
                                
                            burst_type = temp_type
                            burst_time = temp_time
                            
                            # Creates a new job
                            newjob = Job(id, arrival_time, burst_type, burst_time, priority)
                            print(f'Job {id} Arrived at {arrival_time}')
                            print(f'Bursts: {burst_type} Duration: {burst_time}')
                            NewQueue.append(newjob)
                    preliminary_jobs.clear()
        
        if len(NewQueue) > 0:
            for job in NewQueue:
                ReadyQueue.append(job)
                NewQueue.remove(job)
        
        if len(ReadyQueue) > 0:
            for job in ReadyQueue:
                if len(Running) == 0:
                    Running.append(job)
                    ReadyQueue.remove(job)
                    
                else:
                    job.increment_wait_time()
    
        
        for job in Running:
            if job.get_burst_type() == "IO":
                WaitingQueue.append(job)
                Running.remove(job)
                continue
            
            if job.get_burst_type() == "CPU":
                if job.get_burst_time() == 0:
                    job.get_next_burst()
                    WaitingQueue.append(job)
                    Running.remove(job)
                    continue
                    
                else:
                    job.decrement_burst_time()
                    if job.get_burst_time() == 0:
                        job.get_next_burst()
                        WaitingQueue.append(job)
                        Running.remove(job)
                        continue
                    
            if job.get_burst_type() == "EXIT":
                job.set_exit_time(clock)
                FinishedQueue.append(job)
                Running.remove(job)
                print(f'Job {job.get_id()} Finished at {job.get_exit_time()}')
                
                  
        for job in WaitingQueue:
            if job.get_burst_type() == "IO":
                if len(IO_Queue) == 0:
                    IO_Queue.append(job)
                    WaitingQueue.remove(job)
                else:
                    job.increment_wait_time()
            
            else:
                ReadyQueue.append(job)
                WaitingQueue.remove(job)
        
              
        for job in IO_Queue:
            
            if job.get_burst_time() == 0:
                job.get_next_burst()
                ReadyQueue.append(job)
                IO_Queue.remove(job)
                
            else:
                job.decrement_burst_time()
                if job.get_burst_time() == 0:
                    job.get_next_burst()
                    ReadyQueue.append(job)
                    IO_Queue.remove(job)
        
              
        if len(FinishedQueue) == num_jobs:
            Working = False
        
        clock += 1
        totalTime += 1
    
    for job in FinishedQueue:
        print(f'Job {job.get_id()} Waited {job.get_wait_time()} ticks, Arrived at {job.get_arrival_time()} and Finished at {job.exit_time}')
        print("")
        
    print(f'Total Time: {totalTime}')