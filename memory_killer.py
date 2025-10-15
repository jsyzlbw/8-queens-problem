import random
import time
from typing import Tuple, List
from math import comb

#the idea to solve the 8-queens problem
#1.construct a 64-element tuple, and each element represent a position if the board
#2.func1: put the 8 queens on the board randomly
# (utmost 64*63*62*61*60*59*58*57 = 178,462,987,637,760 situations)
#3.func2: for each situation, check whether it is OK
#4.print the result

all_positions = [(i, j) for i in range(1, 9) for j in range (1, 9)]

def checker(positions: List) -> bool:
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
#initialization
print("The program is running")
try_time = 0
solution = set()
all_situations = comb(64, 8)
t1 = time.time()

while True:
    positions = place_the_queens()
    try_time +=1
    pos_tuple = tuple(sorted(positions))
    
    if checker(positions) and (pos_tuple not in solution):
        print(positions)
        
    solution.add(pos_tuple)
    
    if try_time % 100000 ==0:
        print(f"Try: {try_time}, Memory used: {len(solution)} positions stored")
    
    if len(solution) == all_situations:
        break
    
    
t2 = time.time()
print(f"Time usage: {t2 - t1} s")
print(f"Python tired {try_time} to get the answer.")
print(f"Your CPU single core and memory performance: {try_time/(t2 - t1)}")