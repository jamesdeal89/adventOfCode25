# Day 7: Connecting junction-boxes that are the closest together.
# input: each line contains x,y,z comma seperated.
# using euclidean distance, connect the 2 closest boxes.
# repeat
# if one of the closest is already in another circuit, the rest are added to that circuit's size.
# if both are already in the same circuit, nothing happens.
from math import sqrt

def getEuclideanDist(node1, node2):
    return sqrt((node1[0]-node2[0])**2+(node1[1]-node2[1])**2+(node1[2]-node2[2])**2)


def getThreeLargestCircuitSize():
    nodes = []
    # key: circuit co-ords, value: circuitID
    created = {}
    distances = []
    with open('input7', 'r') as f:
        for line in f:
            nodes.append(list(map(int,line.strip().split(','))))
    print(nodes)
    # compute distances
    for node1 in nodes:
        for node2 in nodes:
            if node1 == node2:
                continue
            distances.append(((str(node1),str(node2)),getEuclideanDist(node1,node2)))


    # sorted distances
    distances.sort(key=lambda x: x[1])
    
    # main loop
    banned = []
    circId = 0
    connections = 0
    i=0
    while connections < 1000:
        pair, minDist = distances[i]
        minNode, minNode1 = pair[0],pair[1]
        banned.append((minNode1,minNode))
        if (minNode, minNode1) in banned:
            i+=1
            continue

        # connect 2 circuits into 1
        if minNode in created and minNode1 in created:
            if created[minNode] != created[minNode1]:
                oldId = created[minNode1]
                newId = created[minNode]
                for node, id in created.items():
                    if id == oldId:
                        created[node] = newId
        # if one is in a circuit already 
        # add both to that circId
        if minNode in created:
            created[minNode1] = created[minNode]
        elif minNode1 in created:
            created[minNode] = created[minNode1]
        else:
            # otherwise, new circuit
            created[minNode] = circId
            created[minNode1] = circId
            circId += 1
        print('\n\n')
        print(created)
        print(f"CONNECTED {minNode} and {minNode1}")
        print(f"Distance {minDist}")
        connections +=1 
        i+=1
    
    # key: circId, val: count
    sizes = {}
    print(created)
    for node,circId in created.items():
        if circId in sizes:
            sizes[circId] += 1
        else:
            sizes[circId] = 1

    sizes = list(sizes.values())
    sizes.sort(reverse=True)
    print(sizes)
    return sizes[0] * sizes[1] * sizes[2]
        
# print(getThreeLargestCircuitSize())

# Part 2: continue connecting until they're all in the same circuit.
# Return the result of multiplying together the X co-ords of the last 2 boxes connected.

def checkIfOneCircuit(created,numBoxes):
    uniqueIDs=set()
    for id in created.values():
        uniqueIDs.add(id)
    
    if len(uniqueIDs) == 1 and len(created.keys()) == numBoxes:
        return True
    return False


def connectIntoOne():
    nodes = []
    # key: circuit co-ords, value: circuitID
    created = {}
    distances = []
    with open('input7', 'r') as f:
        for line in f:
            nodes.append(list(map(int,line.strip().split(','))))
    print(nodes)
    # compute distances
    for node1 in nodes:
        for node2 in nodes:
            if node1 == node2:
                continue
            distances.append(((str(node1),str(node2)),getEuclideanDist(node1,node2)))


    # sorted distances
    distances.sort(key=lambda x: x[1])
    
    # main loop
    banned = []
    circId = 0
    connections = 0
    i=0
    while not checkIfOneCircuit(created, len(nodes)):
        pair, minDist = distances[i]
        minNode, minNode1 = pair[0],pair[1]
        banned.append((minNode1,minNode))
        if (minNode, minNode1) in banned:
            i+=1
            continue

        # connect 2 circuits into 1
        if minNode in created and minNode1 in created:
            if created[minNode] != created[minNode1]:
                oldId = created[minNode1]
                newId = created[minNode]
                for node, id in created.items():
                    if id == oldId:
                        created[node] = newId
        # if one is in a circuit already 
        # add both to that circId
        if minNode in created:
            created[minNode1] = created[minNode]
        elif minNode1 in created:
            created[minNode] = created[minNode1]
        else:
            # otherwise, new circuit
            created[minNode] = circId
            created[minNode1] = circId
            circId += 1
        print('\n\n')
        print(created)
        print(f"CONNECTED {minNode} and {minNode1}")
        print(f"Distance {minDist}")
        connections +=1 
        i+=1
    minNode = minNode.split(',')
    minNode = int(minNode[0][1:])
    minNode1 = minNode1.split(',')
    minNode1 = int(minNode1[0][1:])
    x, x1 = minNode, minNode1
    return x*x1
    
print(connectIntoOne())