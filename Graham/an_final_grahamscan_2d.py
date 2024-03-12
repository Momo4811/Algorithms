class PointSymbolTable: #technically a binary tree
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
    
    def valuesToList(self):#in order traversal to list
        return (self.left.valuesToList() if self.left else []) + [self.value] + (self.right.valuesToList() if self.right else [])
    
    def get(self, key):#normal binary tree get 
        return self.value if self.key == key else (self.right.get(key) if self.key < key else self.left.get(key))
    
    def put(self, key, value:int, ref, arr):#normal binary tree put - value in this context is the array index
        if self.key == key:
            #always keep furthest point from ref
            self.value = value if calcDistance(arr[value],ref) > calcDistance(arr[self.value],ref) else self.value
        elif self.key < key:
            if self.right is not None:
                self.right.put(key, value, ref, arr)
            else:
                self.right = PointSymbolTable(key, value)
        else:
            if self.left is not None:
                self.left.put(key, value, ref, arr)
            else:
                self.left = PointSymbolTable(key, value)

def cross_product(p1,p2,p3):#point repr as [x,y]
    return (p2[0] - p1[0])*(p3[1] - p1[1]) - (p3[0] - p1[0])*(p2[1] - p1[1])

def calcDistance(point1,point2):#manhattan distance
    return abs(point2[0]-point1[0]) + abs(point2[1]-point1[1])    

def sort_key(start,p1): #sort by -1/tan (angle)
    if p1[1] == start[1]:
        return float('inf') if p1[0] - start[0] < 0 else float('-inf')
    return - (p1[0] - start[0]) / (p1[1] - start[1])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

def akn_graham_scan(listOfPoints):
    stack=[]
    #find point with lowest y co-ordinate - if y is the same take lowest x
    point0 = listOfPoints[0]
    for current in listOfPoints[1:]:
        if (current[1] < point0[1]) or ((current[1] == point0[1]) and (current[0] < point0[0])):
            point0 = current

    #initialise symbol table with angle key and point value
    symTable = PointSymbolTable(sort_key(point0, listOfPoints[0]), 0)

    #calculate angles then sort by angle using symbol table
    for i in range (1,len(listOfPoints)):
        if listOfPoints[i] != point0:
            symTable.put(sort_key(point0,listOfPoints[i]), i, point0, listOfPoints)
        
    sortedPoints = [point0] + [listOfPoints[index] for index in symTable.valuesToList()]
    #push first two points onto stack
    stack.append(sortedPoints[0])
    stack.append(sortedPoints[1])
    for i in range(2,len(sortedPoints)):
        while len(stack) > 1 and cross_product(stack[-2],stack[-1],sortedPoints[i]) <= 0:
            #if < 0 then we are turning right so pop the last point from the stack - anticlockwise search
            stack.pop()
        stack.append(sortedPoints[i])
    return stack