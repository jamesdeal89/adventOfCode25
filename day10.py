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

    def getNumPaths(self):
        return self.paths

graph = graph()
graph.traverseGraph()
print(graph.getNumPaths())


