Bar Movshovich <br \>
CS541 AI <br \>
https://github.com/movshov/AI-Dinner-Party <br \>

# Dinner Party
Solve a dinner party dilemma where we need to generate a table based on a preference matrix of how much person "a" likes or despises person "b". 

For example the hw1-inst1.txt file looks like this: 
```
10
0 -4 6 5 8 1 1 -6 2 -9
-6 0 3 -7 -5 -2 0 -1 -8 -7
-8 1 0 5 2 -6 3 -1 -7 10
2 -4 0 0 0 -4 2 6 5 -7
-7 1 -4 -1 0 3 -8 -8 -1 -5
-9 -5 -4 -7 0 0 -9 9 8 -2
1 9 10 -4 -1 -3 0 0 0 -1
1 -8 -9 1 -4 -10 9 0 1 9
2 2 -1 2 7 2 -8 -9 0 2
-6 -1 9 3 -6 10 9 -3 10 0
```
The number on the first row is the number of people attending this party referred to hereafter as "N". Then every column to row is how much person "a" wants to be seated next to person "b". Note that the number in the preference_matrix can be negative and if the row and column are both equal to the same number, aka the same person, then the value is 0 because a person cannot be seated next to themselves. 

# Build
This program has several flags available for testing. 
```
python3 dinner_table.py --help
usage: dinner_table.py [-h] [--file FILE] [--solver {local,random}]
                       [--matrix {manual,random}]

Generate best dinner table based off of preference_matrix.

optional arguments:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  input file
  --solver {local,random}, -s {local,random}
                        solver algorithm, local search by default
  --matrix {manual,random}, -m {manual,random}
                        test random or manually inputed starting matrix(hard
                        codded), random starting matrix used by default
```

To run the program run the following command: 
```
python3 dinner_table.py -f <YOUR.TXT FILE HERE>
```
You will need to replace <YOUR.TXT FILE HERE> with whatever .txt file you want to use.
For example if you wanted to test the **hw1-inst1.txt** file you would type: 
```
python3 dinner_table.py -f hw1-inst1.txt
```
This will run the program using the local search approach on hw1-inst1.txt file and will output the final result into a txt file called **hw1-inst1-RESULT.txt** in the same directory. The same thing will happen if you run the above command using hw1-inst2 and hw1-inst3 txt files but each will have their own unique RESULT txt file. In total there will be 3 RESULT files for each txt file ran.
```
RESULT FILES:
    hw1-inst1-RESULT.txt
    hw1-inst2-RESULT.txt
    hw1-inst3-RESULT.txt
```

If you wish to see the difference between my local search approach vs random search you can set the **-s flag** to be random a shown below: 
```
python3 dinner_table.py -f hw1-inst1.txt -s random
```
If you wish to test a seating arrangement that you think might be optimal, you can manually input a 2d array to test using the **-m flag**. You will however need to modify the tables manually in the _dinner_table.py_ file. An example is shown below using a manual table with the prefernce matrix from hw1-inst1.txt file: 
```
python3 dinner_table.py -f hw1-inst1.txt -m manual
```
# Algorithm
I ended up using a local search approach with a heuristic to solving this problem. What I did was I set an anchor at row zero and column zero [0][0]. Then I calculated the total score of the table. Next I swapped the person at [0][0] with the person to the right [0][1] and once again calculated the score of the table. If the new score is higher then the previous score save the table as the new best table else if the new score is lower then the previous score revert the table back to what it was before swapping. I then do this again but with the next right index from the one I just used. Once i've hit the last column and checked the scores, I then increment the row by 1 and start again using the same anchor until i've hit the last column again. Once that happens I then increment the anchor once to the right and repeat the process all over again at index [0][0]. I then repeat this same process for every index of the table. I've calcualted that this approach will give me between O(n^2) and O(nLOG(n)) time complexity. This is about what I expected this approach to give me. Since i'm not using a complete state search like branch and bound i'm not always guaranteed to get the best solution. This local search approach with a heuristic will always give me a good estimate but will not always give me the best solution.   
