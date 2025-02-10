def round_robin(processes, burst_time, time_quantum):
    n = len(processes)  # Number of processes

    # Create a list to store remaining time for each process
    remaining_time = []
    for i in range(n):
        remaining_time.append(burst_time[i])

    waiting_time = [0] * n  # List to store waiting time for each process
    turnaround_time = [0] * n  # List to store turnaround time for each process
    time = 0  # Current time in the system

    # Loop until all processes are completed
    while True:
        done = True  # Assume all processes are done
        for i in range(n):
            if remaining_time[i] > 0:
                done = False  # At least one process is not done
                if remaining_time[i] > time_quantum:
                    # Process executes for the time quantum
                    time += time_quantum
                    remaining_time[i] -= time_quantum
                else:
                    # Process completes execution
                    time += remaining_time[i]
                    waiting_time[i] = time - burst_time[i]
                    remaining_time[i] = 0
                    turnaround_time[i] = time

        # If all processes are done, exit the loop
        if done:
            break

    # Calculate average waiting time and average turnaround time
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n

    # Print the results
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")

# Example usage
processes = ['P1', 'P2', 'P3', 'P4']
burst_time = [10, 5, 8, 12]
time_quantum = 2

round_robin(processes, burst_time, time_quantum)