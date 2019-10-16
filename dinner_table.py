#solve dinner table problem HW#1 for Artificial Intelligence. 

import argparse
import functools
import heapq 
import random
import numpy as np
import sys
import math
import time

def column(matrix, i):
        return [row[i] for row in matrix]

#generate random matrix of matrix_length/2.
def score(preference_matrix, table, matrix_length):
    total = 0
    hosts = (matrix_length//2) - 1
    guests = (matrix_length//2)

    #print(np.matrix(preference_matrix))
    for z in range(matrix_length//2):
        x,y = table[:,z]
        #FOR TESTING PURPOSES
        #print(table)
        #print(x,y)
        total = total + preference_matrix[x][y] + preference_matrix[y][x]
        #Checks if person across is host to guest if so add 2 points. 
        if (x <= hosts and y >= guests) or (y <= hosts and x >= guests):
            total = total + 2
        #go until we reach last column
        a, t1 = np.shape(table)
        if z <= t1-2:
            #print('z is: ', z)
            w,v = table[:,z+1]
            total = total + preference_matrix[x][w] + preference_matrix[w][x]
            if (x <= hosts and w >=guests) or (w <= hosts and x >= guests):
                total = total + 1
            total = total + preference_matrix[y][v] + preference_matrix[v][y]
            if (y <= hosts and v >=guests) or (v <= hosts and y >= guests):
                total = total + 1
    #print('total is:', total) 
    return total
    
#grab data from file. 
def main():
    
    parser = argparse.ArgumentParser(description='Generate best dinner table.')
    parser.add_argument('--file', '-f', type=str, default=None, help='input file') 

    solvers = {
    "random",
    #"walk",
    #"bfs",
    #"dfs",
    #"dfid",
    "astar"
    }
    parser.add_argument('--solver', '-s',
                    type=str, choices=solvers,
                    default="random", help='solver algorithm')
    matrix = {
    "random",
    "manual"
    }
    parser.add_argument('--matrix', '-m',
                    type=str, choices=matrix,
                    default="random", help='test random or manual matrix')
    args = parser.parse_args()
    #n = args.n
    solver = args.solver
    matrix = args.matrix
    file = args.file
    if args.file == None:
        # Build a random puzzle.
        print("no input file detected")
        return -1;

    #with open(sys.argv[1], 'r') as f:
    with open(args.file, 'r') as f:
        #grab first line of how many people.
        first_line = f.readline().rstrip('\n')  
        #get the size of the table. 
        matrix_length = int(first_line)
        #read in preference_table into matrix. 
        preference_matrix = [[int(num) for num in line.split(" ")] for line in f]   
        #print(np.matrix(preference_matrix))
        
        high_score = 0
        highest_table = np.zeros((2,matrix_length//2))
        t_end = time.time() + 60 * 0.25
        while time.time() < t_end:

            #generate a matrix of random integers from 0:9
            if matrix == "random":
                table = np.random.choice(matrix_length,(2,matrix_length//2), replace=False)
            #MANUAL ARRAY INPUT EXAMPLE
            elif matrix == "manual": 
                if file != "hw1-inst1.txt":
                    table = np.array([[29,27,22,11,10,0,18,5,28,26,8,3,6,21,20],[19,2,16,23,13,24,14,12,15,1,25,17,4,7,9]])
                else:
                    table = np.array([[4,8,5,9,2],[0,3,7,6,1]])
                    #print('manual table is:',table)

            #prints a matrix of random integers. 
            #print(table)
            sum = score(preference_matrix, table, matrix_length)
            if sum > high_score:
                high_score = sum
                print('current_high_score', high_score)
                highest_table = np.copy(table)

        print(np.matrix(preference_matrix))
        print('The highest score was: ', high_score)
        print('The highest table is:')
        print(highest_table)
    
    #for testing purposes.
    #print('matrix length: ', matrix_length)
    #print(preference_matrix)
    

main()
