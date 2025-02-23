# Assignments

# -- Worst-Fit

# Find the index of the largest available block
def large_position(block_size):
    large_index = 0
    max_size = 0
    for i in range(len(block_size)):
        if block_size[i] > max_size:
            max_size = block_size[i]
            large_index = i
    return large_index  # Return index of the largest available block

# Worst-Fit Algorithm
def worst_fit(block_size, m, process_size, n):
    allocation = [-1] * n  # Initialize allocation array with -1 (not allocated)

    for i in range(n):  # Loop over each process
        larg_pos = large_position(block_size)  # Find the largest available block
        if larg_pos != 0 and block_size[larg_pos] >= process_size[i]:  # Check if it fits
            allocation[i] = larg_pos
            block_size[larg_pos] -= process_size[i]  # Reduce block size

    # Print allocation results
    print(f"Process No\tProcess Size\tBlock No")
    for k in range(n):
        print(f"P{k+1}\t\t{process_size[k]}\t\t", end='')
        if allocation[k] != -1:
            print(allocation[k])
        else:
            print("Not Allocated")

# Data
block_size = [100, 200, 700, 600]
process_size = [212, 417, 112, 426]

# Sizes
m = len(block_size)
n = len(process_size)

worst_fit(block_size, m, process_size, n)
