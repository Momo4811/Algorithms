import timeit
import random
from stack import Stack
from point import Point, PointSymbolTableTree

def akn_graham_scan(listOfPoints):
    stack=Stack()
    #find point with lowest y co-ordinate - if y is the same take lowest x
    point0 = listOfPoints[0]
    for current in listOfPoints:
        if (current.y < point0.y) or ((current.y == point0.y) and (current.x < point0.x)):
            point0 = current
    
    symTable = PointSymbolTableTree(listOfPoints[0].calcAngle(point0),listOfPoints[0])
    #calculate angles
    for current in listOfPoints:
        symTable.put(current.calcAngle(point0),current)

"""
let points be the list of points
let stack = empty_stack()

find the lowest y-coordinate and leftmost point P0
sort points by polar angle with P0, 
if several points have the same polar angle 
then only keep the farthest

for point in points:
    # pop the last point from the stack if we turn clockwise to reach this point
    while count stack > 1 and ccw(next_to_top(stack), top(stack), point) <= 0:
        pop stack
    push point to stack
end
"""