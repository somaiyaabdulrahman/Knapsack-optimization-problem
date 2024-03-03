from mimetypes import init
import time

startTime = time.perf_counter()

# Item-ID, benefit, weight
itemList = [
    [1, 20, 15],
    [2, 40, 32],
    [3, 50, 60],
    [4, 36, 80],
    [5, 26, 43],
    [6, 64, 120],
    [7, 54, 77],
    [8, 18, 6],
    [9, 46, 93],
    [10, 28, 35],
    [11, 25, 37], 
]
class Node():
    def __init__(self,information,numberOfID, parent,depth,benefit,weight):
        self.information = information
        self.numberOfID = numberOfID
        self.parent = parent
        self.depth = depth
        self.benefit = benefit
        self.weight = weight

    information = 0
    numberOfID = 0
    parent = []
    depth = 0
    benefit = 0
    weight = 0

 #------------------------------ALL VARIABLES ------------------------------#   

#knapsack weight can not exceed 420
maximumWeight = 420

#the loop cannot run more levels than the depth 
maximumDepth = 11

#empty queue that will eventually be filled 
bfsQueue = []

#rootNode = (information, parentNode, deapth, benefit, weight)
rootNode = Node(information = 0, numberOfID = 0, parent=0, depth = 0, benefit=0, weight=0)

#highest benefit value
highestBenefitNode = Node(information = 0, numberOfID = 0, parent=0, depth = 0, benefit=0, weight=0)

#the id:s of the highestbenefitnode in the knapsack
filledKnapsack = []

######------------before starting our loop --------------######

#we insert our rootnode first in the queue  
bfsQueue.append(rootNode)


######--------------------the loop-----------------######

while len(bfsQueue) != 0:
    currentNode = bfsQueue.pop(0)
    if currentNode.benefit > highestBenefitNode.benefit:
        if currentNode.weight <= maximumWeight:
            highestBenefitNode = currentNode

    if currentNode.depth < maximumDepth:
        childNode_with = Node(1,itemList[currentNode.depth][0], currentNode,currentNode.depth+1,itemList[currentNode.depth][1] + currentNode.benefit,itemList[currentNode.depth][2] + currentNode.weight)
        childNode_without = Node(0, itemList[currentNode.depth][0], currentNode,currentNode.depth+1,currentNode.benefit, currentNode.weight)
        if currentNode.weight <= maximumWeight:
            bfsQueue.append(childNode_with)
            bfsQueue.append(childNode_without)


currentNode = highestBenefitNode
while currentNode.parent != 0:
    if currentNode.information == 1:
        filledKnapsack.append(currentNode.numberOfID)  
    currentNode = currentNode.parent

        

endTime = time.perf_counter()

searchtime = endTime - startTime

print("----------------- BREADTH-FIRST-SEARCH (BFS) -----------------\n")
print("Combination of item-ID:s in the knapsack:", filledKnapsack)
print("\nBest knapsack total weight:",highestBenefitNode.weight)
print("\nBest knapsack total benefit:", highestBenefitNode.benefit)
print("\nBFS serach time: ", searchtime, "seconds")
print('_______________________________________________________________')
