# day 4: ingredient management system
# input is 1 file.
# first half of file is ranges of fresh ingredient IDs.
# then a blank line to separate.
# second half is IDs, each on their own line.
# return number of fresh IDs.

def freshCount():
    ranges = True
    safe = set()
    count = 0
    with open('input4', 'r') as f:
        for line in f:
            if ranges:
                # building safe set
                if line == '\n':
                    ranges = False
                else:
                    start, end = line.split('-')
                    safe.add(range(int(start),int(end)+1))
            else:
                # check IDs
                for safelist in safe:
                    if int(line) in safelist:
                        count += 1
                        break
            print('.')

    return count

#print(freshCount())

# Part 2: how many ingredient IDs are considered fresh according to the ID ranges?

def freshCount2():
    # Store ranges in a list, 
    # if a new range touches or overlaps with an existing range, update it.
    # if it doesn't touch or overlap, add a new range.
    ranges = []
    count = 0
    with open('input4', 'r') as f:
        for line in f:
            # building safe set
            if line == '\n':
                break
            else:
                startEnd = list(map(int,line.split('-')))
                start, end = startEnd[0], startEnd[1]
                # check for existing range overlap
                while True:
                    merged = False
                    for rangeR in ranges.copy():
                        startR, endR = rangeR[0], rangeR[1]
                        # we want the opposite of when they do not touch or overlap
                        # no overlap is when end < startR or start > endR
                        # the negation is:
                        if not (start > endR) and not (end < startR):
                            ranges.pop(ranges.index((startR,endR)))
                            start = min(start, startR)
                            end = max(end, endR)
                            merged = True
                            break
                    if not merged:
                        ranges.append((start,end))
                        break
    for range in ranges:
        start, end = range[0], range[1]
        count += end-start + 1
    return count

print(freshCount2())

