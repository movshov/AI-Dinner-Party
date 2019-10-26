#solve dinner table problem HW#1 for Artificial Intelligence. 

import argparse
import random
import numpy as np
import sys
import math
import time

#calculate the score for a whole table.
def score_whole_table(preference_matrix, table, matrix_length):
    total = 0 
    #calculate who are hosts. 
    #The first N/2 are considered hosts by the assignment parameters.
    hosts = (matrix_length//2) - 1
    #The second N/2 are considered guests by the assignment parameters.
    guests = (matrix_length//2)

    #print(np.matrix(preference_matrix))
    for z in range(matrix_length//2):
        x,y = table[:,z]
        #FOR TESTING PURPOSES
        #print(table)
        #print(x,y)
        total = total + preference_matrix[x][y]
        total = total + preference_matrix[y][x]
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

#calculate the best score between a node's neighbors. 
def score(preference_matrix, table, matrix_length, temp_highest_table):
    best_score = 0
    best_table = np.zeros((2,matrix_length//2))
    temp = 0
    starting = 0
    halfway = 0
    #new_score = 0
#grab score of table before swapping.  score = score_whole_table(preference_matrix, table, matrix_length)

    #we want this to happpen twice. Once for top row, once for bottom.
    for z in range(matrix_length//2): 
        if halfway < matrix_length//2: 
            halfway = halfway + 1
        else:
            #start on bottom row all the way left as starting index. 
            starting = 1
            halfway = halfway + 1
        #row will give 0 then 1 for row in range(0,2):
            for i in range(matrix_length//2):
                #grab ith column. 
                y = table[row,i]
                #print("x and y are: ", x,y)
                #old_table = np.copy(table)
                old_table = table
                #print("old table is", table)
                #print("origin is:", table[row][z])
                #print("x is: ", y)
                temp = table[starting][z]
                #print("temp is: ", temp)
                table[starting][z] = y
                table[row][i] = temp
                #print("new table is: ", table)
                #calculate score of whole table after swapping. 
                new_score = score_whole_table(preference_matrix, table, matrix_length)
                #check if new table has better score, if so keep it.
                if new_score > best_score:
                    #print("new_score: ", new_score)
                    #print("best_score: ", best_score)
                    best_score = new_score
                    #print("after best_score: ", best_score)
                    temp_highest_table = np.copy(table)
                    if best_score == 100:
                        print("highest_table in score: ", temp_highest_table)
                elif new_score < best_score:
                    #reset table back to old version.
                    table = old_table

    temp_highest_table = np.copy(best_table)
    return best_score

def highest_scores(preference_matrix, matrix_length):
    highest_scores_table = np.zeros(matrix_length)
    highest = 0
    #print("matrix lenght is: ",matrix_length)
    #traverse through entire preference_matrix
    for z in range(matrix_length):
        #print(z)
        for i in range(matrix_length):
            x = preference_matrix[z][i] + preference_matrix[i][z]
            #print("x is: ", x)
            #print("highest is: ", highest)
            if x > highest:
                highest = x
            #we are at the end, input to final result table.
            if i == matrix_length-1:
                highest_scores_table[z] = highest
                #reset highest
                highest = 0

    #print("highest_scores_table is: ", highest_scores_table)
    
#grab data from file. 
def main():
    
    parser = argparse.ArgumentParser(description='Generate best dinner table.') 
    parser.add_argument('--file', '-f', type=str, default=None, help='input file') 
    solvers = {
    "random",
    #"walk",
    #"bfs",
    #"dfid",
    "local"
    }
    parser.add_argument('--solver', '-s',
                    type=str, choices=solvers,
                    default="local", help='solver algorithm, random by default')
    matrix = {
    "random",
    "manual"
    }
    parser.add_argument('--matrix', '-m',
                    type=str, choices=matrix,
                    default="random", help='test random or manually inputed matrix hard codded, random by default')
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
        ids_high_score = 0
        ids_highest_table = np.zeros((2,matrix_length//2))
        ids_table = np.zeros((2,matrix_length//2))
        temp_highest_table = np.zeros((2,matrix_length//2))
        iterations = 0
        repeats = 0
        #generate the highest table as a 2 by (matrix_length/2) and initialize to zeros. 
        temp = np.zeros((2,matrix_length//2))

        #determine how long to run the code for. 
        t_end = time.time() + 60 * 0.1

        #while we haven't hit the time limit keep going. 
        while time.time() < t_end:

            if solver == "random":
                #generate a matrix of random integers from 0:9
                if matrix == "random":
                    #generate a random matrix.
                    table = np.random.choice(matrix_length,(2,matrix_length//2), replace=False)
                #MANUAL ARRAY INPUT EXAMPLE
                elif matrix == "manual": 
                    #if we are using hw1-inst2 or hw1-inst3 use this manually inputed matrix. 
                    if file != "hw1-inst1.txt":
                        table = np.array([[29,27,22,11,10,0,18,5,28,26,8,3,6,21,20],[19,2,16,23,13,24,14,12,15,1,25,17,4,7,9]])
                    else:
                        #if we are using hw1-inst1 use this manually inputed matrix. 
                        table = np.array([[2,9,5,8,4],[1,6,7,3,0]])
                #print('manual table is:',table)

                #grab the score of the table. 
                sum = score_whole_table(preference_matrix, table, matrix_length) 
                #if the new score is higher than the old score update high_score and higest_table.
                if sum > high_score:
                    high_score = sum
                    print('current_high_score', high_score)
                    highest_table = table
                    print(highest_table)

            elif solver == "local": 
                if matrix == "random":
                    #generate a random matrix.
                    table = np.random.choice(matrix_length,(2,matrix_length//2), replace=False)

                #MANUAL ARRAY INPUTS FOR TESTING
                elif matrix == "manual": 
                    #we are testing file #3.
                    if file == "hw1-inst3.txt":
                        table = np.array([[7,16,3,15,0,18,4,21,22,28,17,12,26,20,1],[27,14,8,25,19,10,23,2,29,11,5,24,13,9,6]])
                    #we are testing file #2
                    elif file == "hw1-inst2.txt":
                        table = np.array([[29,27,22,11,10,0,18,5,28,26,8,3,6,21,20],[19,2,16,23,13,24,14,12,15,1,25,17,4,7,9]])
                    #we are testing file #1
                    elif file == "hw1-inst1.txt":
                        #if we are using hw1-inst1 use this manually inputed matrix. 
                        table = np.array([[2,3,0,9,6],[7,5,8,4,1]])
###################################################################################################################################        
                best_score = 0
                best_table = np.zeros((2,matrix_length//2))
                temp = 0
                starting = 0
                halfway = 0
                old_score = 0
                
                #grab score of table before swapping.  
                score = score_whole_table(preference_matrix, table, matrix_length)

                #we want this to happpen twice. Once for top row, once for bottom.
                #Thats why we are checking halfway and updating starting if we are halfway.
                for z in range(matrix_length//2): 
                    if halfway < matrix_length//2: 
                        halfway = halfway + 1
                    else:
                        #start on bottom row all the way left as starting index. 
                        starting = 1
                        halfway = halfway + 1
                    #row will give 0 then 1
                    for row in range(0,2):
                        for i in range(matrix_length//2):
                            #grab ith column. 
                            y = table[row,i]
                            #hold the old table.
                            old_table = np.copy(table)
                            #calculate the old score of the table.
                            old_score = score_whole_table(preference_matrix,table,matrix_length) 
                            #hold original value of table[starting][z]
                            temp = table[starting][z]
                            #set table[starting][z] as y
                            table[starting][z] = y
                            #set what was y as temp
                            table[row][i] = temp
                            #calculate score of whole table after swapping. 
                            new_score = score_whole_table(preference_matrix, table, matrix_length)

                            #check if new table has better score, if so keep it.
                            if new_score >= best_score:
                                best_score = new_score
                                temp_highest_table = np.copy(table)
                            elif new_score < old_score:
                                #reset table back to old version.
                                table = np.copy(old_table)
##################################################################################################################
                if best_score > ids_high_score:
                    ids_high_score = best_score
                    ids_highest_table = np.copy(temp_highest_table)
                    print('current_high_score', ids_high_score)
                    print("highest table so far: ")
                    for rows in range(0,2):
                        for t in range(matrix_length//2):
                            temp_highest_table[rows][t] = temp_highest_table[rows][t] + 1
                    print(np.matrix(temp_highest_table))
                    
        #change table to be from range 1..matrix_length
        for rows in range(0,2):
            for t in range(matrix_length//2):
                ids_highest_table[rows][t] = ids_highest_table[rows][t] + 1


        #print(np.matrix(preference_matrix))
        print(preference_matrix)
        print("The highest score was: ", ids_high_score)
        print("The highest table is:")
        print(np.matrix(ids_highest_table))
        save_results(file, ids_high_score, ids_highest_table, matrix_length)

def save_results(file, high_score, final_table, matrix_length):
    #create save file if using hw1-inst3.txt
    if file == "hw1-inst3.txt":
        #first earse the file contents.
        save = open("hw1-inst3-RESULT.txt", "w")
        save.close()

        with open("hw1-inst3-RESULT.txt", "w") as f:
            f.write(str(high_score) + "\n")
            for rows in range(0,2):
                for t in range(matrix_length//2):
                    if rows == 0:
                        f.write(str(final_table[rows][t]) + ' ')
                        f.write(str(t+1) + '\n')
                    elif rows == 1: 
                        f.write(str(final_table[rows][t]) + ' ')
                        f.write(str((t+1) + matrix_length//2) + '\n')


            #f.write(np.array2string(final_table))

    #create save file if using hw1-inst2.txt
    elif file == "hw1-inst2.txt":
         save = open("hw1-inst2-RESULT.txt", "w")
    #create save file if using hw1-inst1.txt
    elif file == "hw1-inst1.txt":
        save = open("hw1-inst1-RESULT.txt", "w")
                        
    #for testing purposes.
    #print('matrix length: ', matrix_length)
    #print(preference_matrix)
    #highest_scores(preference_matrix, matrix_length)
    

main()
