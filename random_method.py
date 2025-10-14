import random
import time
from typing import Tuple, List

#the idea to solve the 8-queens problem
#1.construct a 64-element tuple, and each element represent a position if the board
#2.func1: put the 8 queens on the board randomly
# (utmost 64*63*62*61*60*59*58*57 = 178,462,987,637,760 situations)
#3.func2: for each situation, check whether it is OK
#4.print the result

all_positions = [(i, j) for i in range(1, 9) for j in range (1, 9)]

def checker(positions: Tuple) -> bool:
    #check the columns and rows
    for i in range(8):
        for j in range(i+1, 8):
            if (
                positions[i][0] == positions[j][0]
                or positions[i][1] == positions[j][1]
                or abs(positions[i][1] - positions[j][1]) == abs(positions[i][0] - positions[j][0])
                ):
                return False
    
    return True

def place_the_queens() ->List:
    return random.sample(all_positions, 8)

#the main function
print("The program is running")
try_time = 0
t1 = time.time()
while True:
    positions = place_the_queens()
    try_time +=1
    if checker(positions):
        print(positions)
        break
t2 = time.time()
print(f"Time usage: {t2 - t1} s")
print(f"Python tired {try_time} to get the answer.")
print(f"Your CPU single core performance: {try_time/(t2 - t1)}")