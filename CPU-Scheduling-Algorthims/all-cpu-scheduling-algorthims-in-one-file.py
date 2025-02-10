import queue

def fcfs(processes):
    # processes.sort(key=lambda x: x[1])  # Sort by arrival time
    for i in range(len(processes)):
        for j in range(i + 1, len(processes)):
            if processes[i][1] > processes[j][1]:  # Compare arrival times
                processes[i], processes[j] = processes[j], processes[i]  # Swap
    time = 0
    for process in processes:
        pid, arrival, burst = process
        if time < arrival:
            time = arrival
        print(f'Process {pid} starts at {time} and finishes at {time + burst}')
        time += burst

def sjf_non_preemptive(processes):
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival, then burst time
    time = 0
    completed = []
    while processes:
        available = [p for p in processes if p[1] <= time]
        if available:
            shortest = min(available, key=lambda x: x[2])
            processes.remove(shortest)
            pid, arrival, burst = shortest
            print(f'Process {pid} starts at {time} and finishes at {time + burst}')
            time += burst
            completed.append(pid)
        else:
            time += 1

def sjf_preemptive(processes):
    time = 0
    remaining = {p[0]: p[2] for p in processes}
    while remaining:
        available = [p for p in processes if p[1] <= time and p[0] in remaining]
        if available:
            shortest = min(available, key=lambda x: remaining[x[0]])
            pid = shortest[0]
            print(f'Process {pid} runs at time {time}')
            remaining[pid] -= 1
            if remaining[pid] == 0:
                del remaining[pid]
        time += 1

def round_robin(processes, quantum):
    q = queue.Queue()
    time = 0
    for p in processes:
        q.put(p)
    while not q.empty():
        pid, arrival, burst = q.get()
        if time < arrival:
            time = arrival
        execute = min(quantum, burst)
        print(f'Process {pid} runs from {time} to {time + execute}')
        time += execute
        if burst > quantum:
            q.put((pid, time, burst - quantum))

def priority_scheduling(processes):
    processes.sort(key=lambda x: (x[1], x[3]))  # Sort by arrival, then priority
    time = 0
    for process in processes:
        pid, arrival, burst, priority = process
        if time < arrival:
            time = arrival
        print(f'Process {pid} starts at {time} and finishes at {time + burst}')
        time += burst

# Example Usage

ask = input("Enter 1 for FCFS,\n 2 for SJF Non-Preemptive,\n 3 for SJF Preemptive,\n 4 for Round Robin,\n 5 for Priority Scheduling: ")
processes = [(1, 0, 8), (2, 1, 4), (3, 2, 9), (4, 3, 5)]
processes_priority = [(1, 0, 8, 2), (2, 1, 4, 1), (3, 2, 9, 3), (4, 3, 5, 2)]
if ask == "1":
    print("FCFS:")
    fcfs(processes)

elif ask == "2":
    print("\nSJF Non-Preemptive:")
    sjf_non_preemptive(processes)

elif ask == "3":
    print("\nSJF Preemptive:")
    sjf_preemptive(processes)

elif ask == "4":
    print("\nRound Robin:")
    round_robin(processes, quantum=2)

elif ask == "5":
    print("\nPriority Scheduling:")
    priority_scheduling(processes_priority)

