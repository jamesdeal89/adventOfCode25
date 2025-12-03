# Day 2: find the maximum voltage possible 
# each line input is the possible values.
# can take 2 digits from each line, together they form the volage
# sum for all lines to get max.
# e.g 8181819111211 would be 9 and 2 forming 92

def maxVolt():
    maxVolt = 0
    with open('input2', 'r') as f:
        for line in f:
            possib = []
            print(line)
            for char in line:
                if char and char != '\n':
                    possib.append(int(char))
            dig1 = max(possib[:-1])
            dig2 = max(possib[possib.index(dig1)+1:])
            print(dig1,dig2)
            maxVolt += dig1*10 + dig2
    return maxVolt

#print(maxVolt())

# Part 2: choose exactly 12 batteries in each bank.

def maxVolt2():
    maxVolt = 0
    with open('input2', 'r') as f:
        for line in f:
            possib = []
            print("Bank :" + line)
            for char in line:
                if char and char != '\n':
                    possib.append(int(char))

            digs = []

            # sliding window max
            lptr = 0
            rptr = len(possib)-11
            while len(digs) < 12:
                best = max(possib[lptr:rptr])
                digs.append(best)
                lptr = (possib[lptr:rptr].index(best)+lptr)+1
                rptr += 1

            print("result:")
            print(digs)

            maxVolt += int(''.join(map(str,digs)))
    return maxVolt

print(maxVolt2())

