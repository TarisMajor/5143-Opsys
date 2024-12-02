class Job:
    def __init__(self, id, arrival_time, burst_type, burst_time, priority):
        """
        Initializes a job with its id, arrival time, burst time, and priority
        :param id: Unique identifier for job
        :param arrival_time: Time the job arrived in the ready queue
        :param burst_time: Amount of CPU time the job requires
        :param priority: Priority of the job
        """
        self.id = id
        self.arrival_time = arrival_time
        self.burst_type = burst_type
        self.burst_time = burst_time
        self.priority = priority
        self.wait_time = 0
        self.exit_time = 0
        self.cpu_time = 0
        self.ML_wait_time = 0
    
    def decrement_burst_time(self):
        self.burst_time[0] -= 1
        
    def increment_cpu_time(self):
        self.cpu_time += 1
        
    def get_cpu_time(self):
        return self.cpu_time
    
    def reset_cpu_time(self):
        self.cpu_time = 0
    def set_exit_time(self, exit_time):
        self.exit_time = exit_time
        
    def get_exit_time(self):
        return self.exit_time
        
    def get_next_burst(self):
        self.burst_time = self.burst_time[1:]
        self.burst_type = self.burst_type[1:]
    
    def increment_wait_time(self):
        self.wait_time += 1

    def get_wait_time(self):
        return self.wait_time

    def get_burst_time(self):
        return self.burst_time[0]
    
    def get_burst_type(self):
        return self.burst_type[0]

    def get_arrival_time(self):
        return self.arrival_time

    def get_priority(self):
        return self.priority
    
    def set_priority(self, priority):
        self.priority = priority
    
    def get_id(self):
        return self.id
    
    def get_ML_wait_time(self):
        return self.ML_wait_time
    
    def increment_ML_wait_time(self):
        self.ML_wait_time += 1
        
    def reset_ML_wait_time(self):
        self.ML_wait_time = 0