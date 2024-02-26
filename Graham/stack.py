class Stack:
    def __init__(self):
        #initialised as empty stack, infinite size
        self.__values = []
        self.__top = -1

    def isEmpty(self):
        return 0==self.__top
    
    def push(self,value):
        self.__values.append(value)
        self.__top += 1

    def pop(self):
        if self.isEmpty():
            return None
        self.__top -= 1
        return self.__values.pop()
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.__values[self.__top]
    
    def peekNext(self):
        if self.__top > 0:
            return self.__values[self.__top-1]
        return None
    
    def size(self):
        return self.__top+1

    def toList(self):
        return self.__values