# Day 11: final day!
# Fitting presents under trees.
# 2D knapsack problem.

'''
EXAMPLE FILE INPUT:
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
'''

# Output how many of the regions can fit all of the presents listed.

# Backtracking approach:
# Before even attempting a region, do an area check, if the area of a all shapes is > area of region,
#   immediate False.
# As soon as it becomes impossible (all variations of curr present attempted, yet cannot fit), failed branch, prune and return False.

# if multiple presents are required of a given type, simply add it to the present queue twice.

# load all presents and store in a 2D-array which resolves to all it's variations.
#  [[var1, var2, var3, ...],...]
presents = []

# also keep a list of areas for quick checks
# [7,7,...]

# queue of grids to test alongside specification as a tuple
grids = []

# grid generator
def genGrid(x,y):
    return [['.'] * x for _ in range(y)]
    
def readInput():
    with open('input11', 'r') as f:
        present = []
        x = 0
        for line in f:
            if 'x' in line:
                # it's a grid definition
                l,r = line.split('x')
                spec = list(map(int,r[r.index(':')+1:].strip().split(' ')))
                grids.append((genGrid(int(l),int(r[:r.index(':')])),(spec)))
            else: 
                # it's a present definition
                if line.strip() == "":
                    presents.append(present)
                    present = []
                    x=0
                elif not ':' in line:
                    y=0
                    for char in line.strip():
                        if char == '#':
                            present.append((x,y)) 
                        y+=1
                    x+=1
                
readInput()

presentVariations = []
                        
def genVariations():
    for present in presents:
        presentVariations.append([])
        # for (x,y)
        variation = []
        # 90 deg rotate (y,-x)
        for coordinate in present:
            x, y = coordinate[0], coordinate[1]
            variation.append((y,-x))
        # transform to reset to origin.
        # find minimums of x and y
        minX = min([coord[0] for coord in variation])
        minY = min([coord[1] for coord in variation])
        # apply transformation: component - minimum of that component
        variation = [(coord[0]-minX, coord[1]-minY) for coord in variation]
        presentVariations[-1].append(variation)
        variation = []
        # 180 deg rotate (-x,-y)
        for coordinate in present:
            x, y = coordinate[0], coordinate[1]
            variation.append((-x,-y))
        # transform to reset to origin.
        # find minimums of x and y
        minX = min([coord[0] for coord in variation])
        minY = min([coord[1] for coord in variation])
        # apply transformation: component - minimum of that component
        variation = [(coord[0]-minX, coord[1]-minY) for coord in variation]
        presentVariations[-1].append(variation)
        variation = []
        # 270 deg rotate (-y,x)
        for coordinate in present:
            x, y = coordinate[0], coordinate[1]
            variation.append((-y,-x))
        # transform to reset to origin.
        # find minimums of x and y
        minX = min([coord[0] for coord in variation])
        minY = min([coord[1] for coord in variation])
        # apply transformation: component - minimum of that component
        variation = [(coord[0]-minX, coord[1]-minY) for coord in variation]
        presentVariations[-1].append(variation)
        variation = []
        # horizontal flip (x,-y)
        for coordinate in present:
            x, y = coordinate[0], coordinate[1]
            variation.append((x,-y))
        # transform to reset to origin.
        # find minimums of x and y
        minX = min([coord[0] for coord in variation])
        minY = min([coord[1] for coord in variation])
        # apply transformation: component - minimum of that component
        variation = [(coord[0]-minX, coord[1]-minY) for coord in variation]
        presentVariations[-1].append(variation)
        variation = []
        # vertical flip (-x,y)
        for coordinate in present:
            x, y = coordinate[0], coordinate[1]
            variation.append((-x,y))
        # transform to reset to origin.
        # find minimums of x and y
        minX = min([coord[0] for coord in variation])
        minY = min([coord[1] for coord in variation])
        # apply transformation: component - minimum of that component
        variation = [(coord[0]-minX, coord[1]-minY) for coord in variation]
        presentVariations[-1].append(variation)
        
        # basic un-rotated or flipped co-ords
        presentVariations[-1].append(present)

genVariations()

for presentVar in presentVariations:
    print(presentVar)

# Generate queue based on a spec from the available presents
def genQueue(spec):
    queue = []
    for idx, quantity in enumerate(spec):
        for _ in range(quantity):
            queue.append(presentVariations[idx])
    return queue

def printGrid(grid):
    for row in grid:
        print(''.join(row))

def backTrack(grid, queue):
    # all presents placed, success 
    if len(queue) == 0:
        return True
    # for each present and it's variations
    presentVariations = queue.pop(0)
    # do quick area check
    area = 0
    for row in grid: 
        area += row.count('.')
    if len(presentVariations[0]) > area:
        # area of present is > available area, impossible
        return False
    # for each specifc variation of a present
    for present in presentVariations:
        # iterate through all possible origins to place the present
        for xg in range(len(grid)):
            for yg in range(len(grid[0])):
                # try to place each present co-ord,
                placementValid = True
                for coord in present: 
                    x,y = coord[0],coord[1]
                    if xg+x >= len(grid):
                        # this origin fails by going off the end of the row
                        placementValid = False
                        continue
                    if yg+y >= len(grid[0]):
                        # this origin fails by going off the bottom
                        placementValid = False
                        continue
                    if grid[xg+x][yg+y] == '#':
                        placementValid = False
                        continue
                if placementValid:
                    # all points placed successfully
                    # place points
                    # deep copy grid
                    newGrid = [row[:] for row in grid]
                    for coord in present:
                        x,y=coord[0],coord[1]
                        newGrid[xg+x][yg+y] = '#'
                    # can move onto the next present
                    if backTrack(newGrid,queue.copy()):
                        return True
    # tried all variatoions and all placements.
    # no placement worked for this present:
    # restore present to the queue to try again with different present order.
    queue.insert(0,presentVariations)
    return False

def checkAreaOfAll(queue, grid):
    allPresentsArea = 0
    for variation in queue:
        allPresentsArea += len(variation[0])
    area = 0
    for row in grid: 
        area += row.count('.')
    if allPresentsArea > area:
        return False
    return True
        

def testAllGrids():
    count = 0

    for gridspec in grids:
        grid, spec = gridspec[0], gridspec[1]
        queue = genQueue(spec)
        # do a cumulative area check
        if not checkAreaOfAll(queue, grid):
            print("impossible due to area...")
            continue
        print("testing grid:")
        printGrid(grid)
        if backTrack(grid, queue):
            print("ADDED TO COUNT")
            count += 1

    return count

print(testAllGrids())




