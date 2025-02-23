# assingments

    # -- best-fit
    # -- worst-fit

# firts-fit algorithm
def first_fit(blocksize, m, process_size, n):
    allocation = [-1] * n  # initi value to all process -1

    for i in range(n):
        for j in range(m):
            if blocksize[j] >= process_size[i]:
                allocation[i] = j
                blocksize[j] -= process_size[i]
                break

    # print
    print(f"    process No\tblock No")
    
    for i in range(n):
        print('P',i + 1,"   ", process_size[i],'    ', end='    ')
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not allocated")

# Data
Block_size = [100, 500, 200, 300, 600]
process_size = [212, 417, 112, 426]

# sizes
m = len(Block_size)
n = len(process_size)

first_fit(Block_size, m, process_size, n)

