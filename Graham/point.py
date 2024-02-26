from math import sqrt, pi, atan2

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def calcDistance(self,point2):
        return abs(point2.x-self.x) + abs(point2.y-self.y)
    
    def __repr__(self):
        return "("+str(self.x)+","+str(self.y)+")"

class HashTable:
    pass

class PointSymbolTable: #technically a binary tree
    def __init__(self, key, value):
        self.__value = value
        self.__left = None
        self.__right = None
        self.__key = key
    
    def valuesToList(self):#in order traversal to list
        list = []
        if self.__left is not None:
            list.extend(self.__left.valuesToList())
        list.append(self.__value)
        if self.__right is not None:
            list.extend(self.__right.valuesToList())
        return list
    
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
            #always keep furthest point from ref
            if value.calcDistance(ref) > self.__value.calcDistance(ref):
                self.setValue(value)
        elif self.__key < key:
            if self.__right is not None:
                self.__right.put(key, value, ref)
            else:
                self.__right = PointSymbolTable(key, value)
        else:
            if self.__left is not None:
                self.__left.put(key, value, ref)
            else:
                self.__left = PointSymbolTable(key, value)
     