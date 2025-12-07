# Day 6: Beam splitting.
# Given a grid, how many times will a beam which does down from 'S' 
# be split.
# It is split when it encounters a '^'.
# Causes it to create 2 beams which continue down from either side of it.

'''
Example with the beam reaching a splitter and begining to split.

.......S.......
.......|.......
......|^|......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............

'''

def numSplits():
    grid = []
    with open('input6', 'r') as f:
        for line in f:
            grid.append(list(line.strip()))
    count = 0
    i=1
    while i < len(grid):
        y=0
        while y < len(grid[0]):
            if grid[i][y] == '^' and grid[i-1][y] in ['S','1']:
                if y < len(grid)-1:
                    grid[i][y+1] = '1'
                if y > 0:
                    grid[i][y-1] = '1'
                count += 1
            elif grid[i-1][y] in ['S','1']:
                grid[i][y] = '1'
            y+=1
        i+=1

    return count 


print(numSplits())
























