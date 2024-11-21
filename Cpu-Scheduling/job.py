class job:
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
    
    def decrement_burst_time(self):
        
        self.burst_time -= 1
        if self.burst_time == 0:
            return True
        return False    
    
    def increment_wait_time(self):
        self.wait_time += 1

    def get_wait_time(self):
        return self.wait_time

    def get_burst_time(self):
        return self.burst_time

    def get_arrival_time(self):
        return self.arrival_time

    def get_priority(self):
        return self.priority
    