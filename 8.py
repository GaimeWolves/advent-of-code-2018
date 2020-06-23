class node:
    parent = None
    index = 0
    nOfChilds = 0
    nOfMetadata = 0
    lenOfChilds = 0
    metadata = []
    childs = []
    def toString(self):
        print("#{} {}, {}".format(self.index, self.nOfChilds, self.metadata))
        for child in self.childs:
            print("     {}, {}".format(child.nOfChilds, child.metadata))

input = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\8.txt", "r") #Normal case
#input = open("D:\\Programmieren\\Projekte\\AdventOfCode18\\8-test.txt", "r") #Test case

sumOfMetadata = 0
original = [int(s) for s in input.readlines()[0].split(' ')]

## Creates a node at the index and gets the children nodes recursively
def createNode(parent, index):
    if index == len(original):
        return None
    if parent != None:  
        print('New node at index {} with parent at index {}'.format(index, parent.index))
    else:
        print('New node at index {} with parent at index {}'.format(index, 'ROOT'))
    current = node()
    current.metadata = []
    current.childs = []
    current.parent = parent
    current.nOfChilds = original[index]
    current.index = index
    index += 1
    current.nOfMetadata = original[index]
    index += 1
    index = getChilds(current, current.nOfChilds, index)
    index = getMetadata(current, current.nOfMetadata, index)
    return [index, current]

## Creates all children and adds them to the childs array of the parent node
def getChilds(parent, amount, index):
    for x in range(amount):
        new = createNode(parent, index)
        print('Added child with index {} to {}'.format(index, parent.index))
        index = new[0]
        parent.childs.append(new[1])
    return index

## Gets all metadata of the current node and adds them to the current nodes metadata array
def getMetadata(current, amount, index):
    for x in range(amount):
        print('Metadata at index {} of node at index {}'.format(index, current.index))
        current.metadata.append(original[index])
        index += 1
    return index

## Creates the tree structure
tree = createNode(None, 0)[1]

## Adds all metadatas togheter
def addMetadatas(root, amount):
    for i in range(root.nOfChilds):
        amount = addMetadatas(root.childs[i], amount)
    for metadata in root.metadata:
        amount += metadata
    return amount

print(addMetadatas(tree, 0))
print('\nAufgabe 2')

## AUFGABE 2

## Sums up all values of the nodes recursively
def getValue(root, currentVal=0):
    if len(root.childs) > 0:
        for data in root.metadata:
            if data - 1 < len(root.childs):
                currentVal = getValue(root.childs[data - 1], currentVal)
    else:
        for data in root.metadata:
            currentVal += data
    return currentVal

print(getValue(tree))