class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time

def sjf_scheduler(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))  # Sort processes based on arrival time and burst time
    completion_time = [0] * len(processes)
    turnaround_time = [0] * len(processes)
    waiting_time = [0] * len(processes)

    completion_time[0] = processes[0].burst_time
    turnaround_time[0] = completion_time[0] - processes[0].arrival_time
    waiting_time[0] = turnaround_time[0] - processes[0].burst_time

    for i in range(1, len(processes)):
        completion_time[i] = completion_time[i - 1] + processes[i].burst_time
        turnaround_time[i] = completion_time[i] - processes[i].arrival_time
        waiting_time[i] = turnaround_time[i] - processes[i].burst_time

    print("Process\t Arrival Time\t Burst Time\t Completion Time\t Turnaround Time\t Waiting Time")
    for i in range(len(processes)):
        print(f"{processes[i].process_id}\t\t{processes[i].arrival_time}\t\t{processes[i].burst_time}\t\t"
              f"{completion_time[i]}\t\t\t{turnaround_time[i]}\t\t\t{waiting_time[i]}")

if __name__ == "__main__":
    # Example processes
    processes = [
        Process(1, 0, 6),
        Process(2, 2, 8),
        Process(3, 3, 4),
        Process(4, 5, 3),
    ]

    sjf_scheduler(processes)
