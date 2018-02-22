#!/bin/python3

import sys
import math
    
def task_one(arg_1,arg_2):
    # increase between l (arg_1) and r (arg_2) minus one
    # index for this starts at 1 so use (r-1), etc.
    for place, item in enumerate(A[arg_1-1:arg_2]):
        A[place] = item + 1
    return A
    
def task_two(arg_1,arg_2):
    # make a new list so I don't screw up A
    B = A[:]
    # factorialize each item between l (arg_1) and r (arg_2)
    for place, item in enumerate(B[arg_1-1:arg_2]):
        if item > 39:
            B = []
            print(0)
            return
        else:
            B[place] = item * math.factorial(item - 1)
    # then add up list
    # print mod 10^9
    print(sum(B[arg_1-1:arg_2])%1000000000)
    

def task_three(arg_1,arg_2):
    # change value of index i (arg_1) to v (arg_2)
    A[arg_1-1] = arg_2
    return A
    
if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    A = list(map(int, input().strip().split(' ')))
    for a0 in range(m):
        # Write Your Code Here
        task, arg_1, arg_2 = input().strip().split(' ')
        task, arg_1, arg_2 = [int(task), int(arg_1), int(arg_2)]
        if task   == 1:
            task_one(arg_1,arg_2)
        elif task == 2:
            task_two(arg_1,arg_2)
        elif task == 3:
            task_three(arg_1,arg_2)
        

############

#!/bin/python3

import sys
import math

def task_two(arg_1,arg_2):
    if 40 in A[arg_1-1:arg_2]:
        print(0)
    else:
    # make a new list so I don't screw up A
    # factorialize each item between l (arg_1) and r (arg_2)
        B = list([(x * math.factorial(x - 1))%1000000000 for x in A[arg_1-1:arg_2]])
        print(sum(B))

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    A = list(map(int, input().strip().split(' ')))
    for a0 in range(m):
        # Write Your Code Here
        task, arg_1, arg_2 = input().strip().split(' ')
        task, arg_1, arg_2 = [int(task), int(arg_1), int(arg_2)]
        if task   == 1:
            A[arg_1-1:arg_2] = [x + 1 for x in A[arg_1-1:arg_2]]
        elif task == 2:
            task_two(arg_1,arg_2)
        elif task == 3:
            A[arg_1-1] = arg_2
