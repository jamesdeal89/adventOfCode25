# Day 5: math problems vertically

# 123 328  51 64 
# 45 64  387 23 
#  6 98  215 314
#  *   +   *   + 

# return the sum of all the answers to each column.

import operator
from functools import reduce

def mathSolution():
    with open('input5', 'r') as f:
        transpose = [[] for line in range(len(f.readline().split(' '))-1)]
        f.seek(0)
        for line in f:
            tokens = line.split(' ')
            tokens = filter(lambda x: x != ' ' and x != '' and x != '\n', tokens)
            for i,token in enumerate(tokens):
                transpose[i].append(token.strip())

    sumSol = 0
    print(transpose)
    for problem in transpose:
        if len(problem) > 2:
            # last token hold operator
            print(problem)
            opTok = problem[-1].strip()
            if opTok == '+':
                op = operator.add
            elif opTok == '/':
                op = operator.truediv
            elif opTok == '-':
                op = operator.sub
            elif opTok == '*':
                op = operator.mul
        
            sumSol += reduce(op,list(map(int,problem[:-1])))


    return sumSol

#print(mathSolution())

# Part 2: again vertical, but even *more* vertically.
'''
Below's first equation is now considered to be:
1*24*356 

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + 
'''

def mathSolution2():
    grid = []
    with open('input5', 'r') as f:
        # tokenise into a 2D array
        for line in f:
            grid.append([token for token in line if token != '\n'])

    # last row will be the operators
    # can use the operator positions to determine indexes of 1st column of equation
    # iterate down rows first, then across columns
    totals = []
    total = 0
    currOp = None
    for c in range(len(grid[0])):
        value = []
        for r in range(len(grid)):
            token = grid[r][c]
            if token not in ['+','*'] and token != ' ':
                value.append(int(token))
            if token in ['+','*']:
                # countering an operator means starting a new calc
                # add previous complete calculation result to results
                totals.append(total)
                total = 0
                currOp = token 
        if value:
            colVal = 1
            checkVal = value.copy()[::-1]
            value = 0
            for digit in checkVal:
                value += digit * colVal
                colVal *= 10
            if currOp == '*':
                if total == 0:
                    total = value
                else:
                    total *= value
            else:
                if total == 0:
                    total = value
                else:
                    total += value
    totals.append(total)

    return sum(totals) 

print(mathSolution2())
