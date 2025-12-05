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

print(freshCount())

# Part 2: how many ingredient IDs are considered fresh according to the ID ranges?

def freshCount2():
    safe = set()
    count = 0
    with open('input4', 'r') as f:
        for line in f:
            if line == '\n':
                break
            start, end = line.split('-')
            start, end = int(start),int(end)
            chunkSize = 1000
            for chunkStart in range(start, end+1, chunkSize):
                chunkEnd = min(chunkStart + chunkSize -1, end)
                safe.update(range(chunkStart, chunkEnd+1))
    return len(safe)

print(freshCount2())

