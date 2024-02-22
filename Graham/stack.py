class Stack:
    def __init__(self):
        #initialised as empty stack, infinite size
        self.__values = []
        self.__top = 0

    def isEmpty(self):
        return 0==self.__top
    
    def push(self,value):
        self.__values[self.__top] = value
        self.__top +=1

    def pop(self):
        val = self.peek()
        if val is not None:
            self.__top -= 1
        return val
    
    def peek(self):
        if not self.isEmpty():
            return self.__values[self.__top]
        return None