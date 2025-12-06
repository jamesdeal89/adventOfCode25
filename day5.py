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

print(mathSolution())


