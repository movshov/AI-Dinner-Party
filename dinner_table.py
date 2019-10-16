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
    for z in range(matrix_length/2):
        x,y = table[:,z]
        #FOR TESTING PURPOSES
        #print(table)
        #print(x,y)
        total = total + preference_matrix[x][y] + preference_matrix[y][x]
        #Checks if person across is host to guest if so add 2 points. 
        if (x <= 5 and y >= 6) or (y <= 5 and x >= 6):
            total = total + 2
        #go until we reach last column
        a, t1 = np.shape(table)
        if z <= t1-2:
            #print('z is: ', z)
            w,v = table[:,z+1]
            total = total + preference_matrix[x][w] + preference_matrix[w][x]
            if (x <= 5 and w >=6) or (w <= 5 and x >= 6):
                total = total + 1
            total = total + preference_matrix[y][v] + preference_matrix[v][y]
            if (y <= 5 and v >=6) or (v <= 5 and y >= 6):
                total = total + 1
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
