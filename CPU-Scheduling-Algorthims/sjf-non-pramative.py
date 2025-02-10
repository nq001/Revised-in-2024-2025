def sjf_non_preemptive(processes, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Combine processes and burst time into a list of lists
    process_burst = []
    for i in range(n):
        process_burst.append([processes[i], burst_time[i]])
        

    # Sort the list based on burst time (using Bubble Sort for simplicity)
    for i in range(n):
        for j in range(0, n-i-1):
            if process_burst[j][1] > process_burst[j+1][1]:
                # Swap the processes
                process_burst[j], process_burst[j+1] = process_burst[j+1], process_burst[j]

    # Calculate waiting time and turnaround time
    for i in range(n):
        if i == 0:
            waiting_time[i] = 0
        else:
            waiting_time[i] = waiting_time[i-1] + process_burst[i-1][1]
        turnaround_time[i] = waiting_time[i] + process_burst[i][1]

    # Calculate average waiting time and average turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    # Print the results
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{process_burst[i][0]}\t{process_burst[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

# Example usage
processes = ['P1', 'P2', 'P3', 'P4']
burst_time = [6, 8, 7, 3]

sjf_non_preemptive(processes, burst_time)