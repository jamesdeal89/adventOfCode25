# Day 9: Factory
# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1)
# [goal setting of lights] (button and which lights it flips)...
import itertools


def getMinButtons():
    # key: goal config, value: button config
    machines = []
    buttonsIN = []
    with open('input9','r') as f:
        for line in f:
            sections = line.split(' ')
            # we can ignore joltage for 1st part
            machines.append(sections[0])
            buttonsIN.append(sections[1:-1])
    
    minimums = []
    for btnidx,machine in enumerate(machines):
        buttons = buttonsIN[btnidx]

        # remove brackets
        machine = machine[1:-1]
        # [0,1,1,0]
        targetVect = [1 if val == '#' else 0 for val in machine ]
        print(f"Trying machine {machine}")
        # [0,0,0,0]
        baseVect = [0]*len(machine)
        # list of indexes which are flipped by this button.
        buttonsFixed = []
        for button in buttons:
            buttonsFixed.append(list(map(int,button[1:-1].split(','))))
        buttons = buttonsFixed
        # turn button into vectors of a matrix
        buttMatrix = []
        for button in buttons:
            buttVect = baseVect.copy()
            for val in button:
                buttVect[val] = 1
            buttMatrix.append(buttVect)
        # we multiply this with a press vector
        # it's valid if the result, modulo 2, is equal to the target vector
        # iterate how many 1's are in the press vector in every position (enabling and disabling a button's effect)
        # increase each iter
        # return number of 1's which worked.
        numButtons = len( buttMatrix)
        valid = []
        pressesMax = range(numButtons)
        oldlen = len(minimums)
        for presses in pressesMax:
            pVectsPossible = list(itertools.combinations(range(numButtons), presses))
            for pButtons in pVectsPossible:
                # add the transposed matrix with each buttVect scaled by the pVect (enabled/disabled)
                pVect = [0]*len(buttMatrix)
                for val in pButtons:
                    pVect[val] = 1
                resultVect = [0]*len(machine)
                # i = button idx
                for i,component in enumerate(pVect):
                    # j = light idx
                    for j in range(len(resultVect)):
                        resultVect[j] += buttMatrix[i][j] * component

                # modulo each as flipping on and off does nothing
                resultVect = [comp % 2 for comp in resultVect]

                if resultVect == targetVect:
                    print(f"MINIMUM PRESSES = {sum(pVect)}\n")
                    minimums.append(sum(pVect))
                    print(pVect)
                    break
            if len(minimums) > oldlen:
                break
        if len(minimums) == oldlen:
            print("FAILURE")
        
    return sum(minimums)


print(f"\nSUM OF MINIMUMS = {getMinButtons()}")
