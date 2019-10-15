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

    #print(np.matrix(preference_matrix))
    #for z in range(len(table)):
    #for z in table:
    a = range(matrix_length/2)
    for z in a:
        #x,y = column(table, z)
        #x,y = [row[column] for row in table]
        x,y = table[:,z]
        #print(x,y)
        total = total + preference_matrix[x][y] + preference_matrix[y][x]
    
    #print('total is:', total) 
    return total
    
#grab data from file. 
def main():
     
    with open(sys.argv[1], 'r') as f:
        #grab first line of how many people.
        first_line = f.readline().rstrip('\n')  
        matrix_length = int(first_line)
        #skip first line.
        #next(f) 
        #read in preference_table into matrix. 
        preference_matrix = [[int(num) for num in line.split(" ")] for line in f]   
        #print(np.matrix(preference_matrix))
        
        high_score = 0
        t_end = time.time() + 60 * 1
        while time.time() < t_end:
            #generate a matrix of random integers from 0:9
            table = np.random.choice(matrix_length,(2,matrix_length/2), replace=False)
            
            #prints a matrix of random integers. 
            #print(table)
            sum = score(preference_matrix, table, matrix_length)
            if sum > high_score:
                high_score = sum

        print('The highest score was: ', high_score)
    
    #for testing purposes.
    #print('matrix length: ', matrix_length)
    #print(preference_matrix)
    

main()
