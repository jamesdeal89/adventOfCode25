# Advent of code day 1
# Find the invalid IDs, what do you get when you sum the invalid IDs.
# Ivalid IDs - made of some sequence of digits *repeated twice*.
# e.g 55 6464 123123
# input is one long comma seperated line.
# input is seperated into *ranges*
# 11-22 would be 11,12,13...22 IDs.

def getSumInvalid():
    invalid = 0
    with open('input1', 'r') as f:
        ranges = f.readline().strip().split(',')
        for r in ranges:
            se = r.split('-')
            print(se)
            s = int(se[0])
            e = int(se[1])
            while s <= e:
                if str(s)[0:len(str(s))//2] == str(s)[len(str(s))//2:]:
                    invalid += s
                s+=1 
    return invalid

print(getSumInvalid())

# Part 2: invalid is a sequence repeated *at least* twice.

def getSumInvalid2():
    invalid = 0
    with open('input1', 'r') as f:
        ranges = f.readline().strip().split(',')
        for r in ranges:
            se = r.split('-')
            print(se)
            s = int(se[0])
            e = int(se[1])
            while s <= e:
                l = 1
                while l <= len(str(s))//2:
                    if str(s)[:l] * (len(str(s))//l) == str(s):
                        invalid += s
                        break
                    l+=1 
                s+=1 
    return invalid

print(getSumInvalid2())
