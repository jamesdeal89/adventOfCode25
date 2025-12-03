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

print(maxVolt())
