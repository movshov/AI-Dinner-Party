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
The number on the first row is the number of people attending this party referred to hereafter as "N". Then every column to row is how much person "a" wants to be seated next to person "b". Note that the number in the preference_matrix can be negative and if the row and column are both equal to "N" then the value is 0 because a person cannot be seated next to themselves. 

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

