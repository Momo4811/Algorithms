from stack import Stack
from point import Point, PointSymbolTable
from math import atan2

def cross_product(p1,p2,p3):
    return (p2.x - p1.x)*(p3.y - p1.y) - (p3.x - p1.x)*(p2.y - p1.y)

def getAngle(p1,p2):
    return atan2(p2.y - p1.y, p2.x - p1.x)

def akn_graham_scan(listOfPoints):
    stack=Stack()

    #find point with lowest y co-ordinate - if y is the same take lowest x
    point0 = listOfPoints[0]
    for current in listOfPoints[1:]:
        if (current.y < point0.y) or ((current.y == point0.y) and (current.x < point0.x)):
            point0 = current
    
    #initialise symbol table with angle key and point value
    symTable = PointSymbolTable(getAngle(point0,listOfPoints[0]),listOfPoints[0])

    #calculate angles then sort by angle using symbol table
    for current in listOfPoints:
        if current != point0:
            symTable.put(getAngle(point0,current),current,point0)
    
    sortedPoints = [point0] + symTable.valuesToList()
    #push first two points onto stack
    stack.push(sortedPoints[0])
    stack.push(sortedPoints[1])
    for i in range(2,len(sortedPoints)):
        while stack.size() > 1 and cross_product(stack.peekNext(),stack.peek(),sortedPoints[i]) <= 0:
                #if < 0 then we are turning right so pop the last point from the stack
                stack.pop()
        stack.push(sortedPoints[i])
    return stack.toList()