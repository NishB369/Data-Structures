class MyArray:
    def __init__(self, cap: int) -> None:
        self.__cap = cap
        self.__size = 0
        self.__data = [None] * cap
        
    def right_rotate(self,k:int)->None:
        k=k%self.__size
        self.__data = (self.__data[-k:] + self.__data[:-k])