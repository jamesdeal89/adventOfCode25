# day 8: largest area of a rectangle made by choosing two opposite corners.

def getAreaLargestRect():
    redTiles = []
    with open('input8', 'r') as f:
        for line in f:
            redTiles.append(list(map(int,line.strip().split(','))))
    

    # maximise up and right 
    mostTopR = None
    # maximise up and left
    mostTopL = None
    # maximise down and right
    mostBottomR = None
    # maximise down and left
    mostBottomL = None

    # whichever combo of
    # mostTopR + mostBottomL VS mostTopL + mostBottoR 
    # gives the greatest area, take as answer

    for i,j in redTiles:
            if not mostTopR or \
                (mostTopR[0]-i + \
                j - mostTopR[1]) > 0:
                mostTopR = (i,j)
            if not mostTopL or \
                (mostTopL[0]-i -( \
                j - mostTopL[1])) > 0:
                mostTopL = (i,j)
            if not mostBottomR or \
                (i - mostBottomR[0] + \
                j - mostBottomR[1]) > 0:

                mostBottomR = (i,j)
            if not mostBottomL or \
                (i - mostBottomL[0] - \
                j - mostBottomL[1]) > 0:
                mostBottomL = (i,j)
    
    area1 = ((mostBottomR[0] - mostTopL[0])+1) * ((mostBottomR[1] - mostTopL[1])+1)
    area2 = ((mostBottomL[0] - mostTopR[0])+1) * ((mostTopR[1] - mostBottomL[1])+1)
    print(mostBottomR, mostTopL)
    print(mostBottomL, mostTopR)
        
    return max(area1, area2)

print(getAreaLargestRect())




        


