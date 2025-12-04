# Day 3: given a matrix, return the number of '@' that are adjacent to < 4 other '@'.

def getNumAccessible():
    mat = []
    with open('input3', 'r') as f:
        for line in f:
            mat.append(list(line)[:-1])
        # store all the offsets to get all adjacent positions to check
        adjacent = [[1,1],[0,1],[1,0],[-1,-1],[1,-1],[-1,1],[-1,0],[0,-1]]
        accessible = 0
        print(mat)
        for i,row in enumerate(mat):
            print('\n')
            for k,col in enumerate(row):
                count = 0
                for offset in adjacent:
                    rowOff, colOff = offset[0], offset[1]
                    newI = i + rowOff 
                    newK = k + colOff
                    if newI < 0 or newI > len(mat)-1 or newK < 0 or newK > len(mat[0])-1:
                        continue
                    if mat[newI][newK] == '@':
                        count += 1
                if count < 4 and mat[i][k] == '@':
                    accessible += 1
                    print('x', end='')
                else:
                    print(mat[i][k], end='')
        return accessible

#print(getNumAccessible())

# Part 2: once it can be accessed, it is removed. 

def getNumAccessible2():
    mat = []
    with open('input3', 'r') as f:
        for line in f:
            mat.append(list(line)[:-1])
        # store all the offsets to get all adjacent positions to check
        adjacent = [[1,1],[0,1],[1,0],[-1,-1],[1,-1],[-1,1],[-1,0],[0,-1]]
        accessible = 0
        print(mat)
        prev = -1
        while accessible != prev:
            prev = accessible
            for i,row in enumerate(mat):
                print('\n')
                for k,col in enumerate(row):
                    count = 0
                    for offset in adjacent:
                        rowOff, colOff = offset[0], offset[1]
                        newI = i + rowOff 
                        newK = k + colOff
                        if newI < 0 or newI > len(mat)-1 or newK < 0 or newK > len(mat[0])-1:
                            continue
                        if mat[newI][newK] == '@':
                            count += 1
                    if count < 4 and mat[i][k] == '@':
                        accessible += 1
                        mat[i][k] = '.'
                        print('x', end='')
                    else:
                        print(mat[i][k], end='')
    return accessible

print(getNumAccessible2())
