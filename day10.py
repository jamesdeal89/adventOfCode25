# Day 10: Finding number of paths


class node:
    def __init__(self, name='', connections=[]):
        self.name = name
        self.connections = connections

    def getConnections(self):
        return self.connections

    def getName(self):
        return self.name

class graph():
    def __init__(self):
        self.nodes = {}
        with open('input10', 'r') as f:
            for line in f:
                # format of line: aaa: bbb ccc
                # machine aaa has connection to bbb and ccc
                machine, outputs = line.split(':')
                outputs = outputs.strip().split(' ')
                newNode = node(machine.strip(), outputs)
                self.nodes[newNode.getName()] = newNode 

    def traverseGraph(self):
        # number of paths from 'you' to 'out'
        self.paths = 0
        def recursiveSearch(connections):
            for connection in connections:
                if connection == 'out':
                    self.paths += 1
                    break
                recursiveSearch(self.nodes[connection].getConnections())

        recursiveSearch(self.nodes['you'].getConnections())

    def traverseGraph2(self):
        memo = {}
        # must go from 'svr' to 'out' but passing through both 'dac' and 'fft'.

        def recursiveSearch(connection,dac,fft):
            if connection == 'dac':
                dac = True
            if connection == 'fft':
                fft = True
            # check memo
            state = (connection, dac, fft)
            if state in memo:
                return memo[state]
            if connection == 'out' and dac and fft:
                return 1 
            if connection not in self.nodes:
                return 0
            paths = 0
            for connectionNext in self.nodes[connection].getConnections():
                paths += recursiveSearch(connectionNext, dac, fft)
            # memoise
            memo[state] = paths
            return paths


        self.paths2 = recursiveSearch('svr', False, False)


    def getNumPaths(self):
        return self.paths

    def getNumPaths2(self):
        return self.paths2

graph = graph()
#graph.traverseGraph()
#print(graph.getNumPaths())
graph.traverseGraph2()
print(graph.getNumPaths2())

