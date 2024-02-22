from math import sqrt, pi, atan2

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def calcAngle(self,point2):
        #cos x = (a . b) / |a| |b|
        return (atan2(point2.y-self.y, point2.x-self.x) + 2*pi) % (2 * pi)
    
    def calcDistance(self,point2):
        return sqrt((point2.y-self.y)**2 + (point2.x-self.x)**2)
    
class PointSymbolTableTree:
    def __init__(self, key, value):
        self.__value = value
        self.__left = None
        self.__right = None
        self.__key = key
    
    def getLeft(self):
        return self.__left
    
    def getRight(self):
        return self.__right
    
    def getKey(self):
        return self.__key
    
    def getValue(self):
        return self.__value
    
    def setLeft(self, left):
        self.__left = left
    
    def setRight(self, right):
        self.__right = right
    
    def setValue(self, value):
        self.__value = value
    
    def get(self, key):
        if self.__key == key:
            return self.__value
        elif self.__key < key:
            if self.__right is not None:
                return self.__right.get(key)
            else:
                return None
        else:
            if self.__left is not None:
                return self.__left.get(key)
            else:
                return None
    
    def put(self, key, value, ref):
        if self.__key == key:
            if value.calcDistance(ref) > self.__value.calcDistance(ref):
                self.setValue(value)
        elif self.__key < key:
            if self.__right is not None:
                self.__right.put(key, value)
            else:
                self.__right = PointSymbolTableTree(key, value)
        else:
            if self.__left is not None:
                self.__left.put(key, value)
            else:
                self.__left = PointSymbolTableTree(key, value)
     