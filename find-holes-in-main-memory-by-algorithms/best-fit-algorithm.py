# Assignments

# -- Best-Fit

# Find the index of the smallest available block that can fit the process
def smallest_position(block_size, process_size):
    smallest_index = -1
    min_size = max(block_size) + 1 
    for i in range(len(block_size)):
        if block_size[i] >= process_size and block_size[i] < min_size:
            min_size = block_size[i]
            smallest_index = i
    return smallest_index


# Best-Fit Algorithm
def best_fit(block_size, m, process_size, n):
    allocation = [-1] * n  # Initialize allocation array with -1 (not allocated)

    for i in range(n):  # Loop over each process
        # Find the smallest block that can accommodate the process
        smallest_pos = smallest_position(block_size, process_size[i])
        if smallest_pos != -1:  # If a suitable block is found
            allocation[i] = smallest_pos
            block_size[smallest_pos] -= process_size[i]  # Reduce block size


    # Print allocation results with better formatting
    print("\nMemory Allocation Results:")
    print("| Process No | Process Size | Block No |")
    for k in range(n):
        block_num = allocation[k] + 1 if allocation[k] != -1 else "Not Allocated"
        print(f"|  P{k+1}        |  {process_size[k]}\t    |    {block_num}     |")


    # Print remaining blocks
    print("\nRemaining Blocks:")
    for i in range(m):
        if block_size[i] != 0:
            print(f"Block {i+1}: {block_size[i]}")

# Data
block_size = [300, 450, 500, 310, 400]
process_size = [212, 417, 200, 260, 460]

# Sizes
m = len(block_size)
n = len(process_size)

best_fit(block_size, m, process_size, n)
