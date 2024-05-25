class MyArray:
    def __init__(self, cap: int) -> None:
        self.__cap = cap
        self.__size = 0
        self.__data = [None] * cap

    def cust_resize(self, factor:int) -> None:
        arr2 = [None] * (factor * self.__cap)
        for i in range(self.__size):
            arr2[i] = self.__data[i]
        self.__data = arr2
        self.__cap *= factor

 
