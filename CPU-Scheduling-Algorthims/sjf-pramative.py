# Function to calculate waiting time
def calculate_waiting_time(processes, n, burst_time, waiting_time):
    remaining_time = burst_time.copy()
    time = 0
    completed = 0
    while completed < n:
        # Find the process with the shortest remaining time
        idx = -1
        min_time = float('inf')
        for i in range(n):
            if remaining_time[i] > 0 and remaining_time[i] < min_time:
                min_time = remaining_time[i]
                idx = i
        # Process execution
        if idx != -1:
            remaining_time[idx] -= 1
            time += 1
            if remaining_time[idx] == 0:
                completed += 1
                waiting_time[idx] = time - burst_time[idx]
                
# Function to calculate turnaround time
def calculate_turnaround_time(processes, n, burst_time, waiting_time, turnaround_time):
    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

# Function to find the average waiting time and turnaround time
def find_average_times(processes, n, burst_time):
    waiting_time = [0] * n
    turnaround_time = [0] * n

    calculate_waiting_time(processes, n, burst_time, waiting_time)
    calculate_turnaround_time(processes, n, burst_time, waiting_time, turnaround_time)

    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    return average_waiting_time, average_turnaround_time

# Driver code
if __name__ == "__main__":
    processes = [1, 2, 3]  # Process IDs
    burst_time = [6, 8, 7]  # Burst time for each process
    n = len(processes)

    average_waiting_time, average_turnaround_time = find_average_times(processes, n, burst_time)

    print(f"Average Waiting Time: {average_waiting_time:.2f}")
    print(f"Average Turnaround Time: {average_turnaround_time:.2f}")
