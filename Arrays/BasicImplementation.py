class MyArray:
    def __init__(self, cap: int) -> None:
        self.__cap = cap
        self.__size = 0
        self.__data = [None] * cap

    def __getitem__(self, ind: int) -> int:
        if 0 <= ind < self.__size:
            return self.__data[ind]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, ind: int, val: int) -> None:
        if 0 <= ind < self.__size:
            self.__data[ind] = val
        else:
            raise IndexError("Index out of range")

    def __len__(self) -> int:
        return self.__size

    def __resize(self) -> None:
        arr2 = [None] * (2 * self.__cap)
        for i in range(self.__size):
            arr2[i] = self.__data[i]
        self.__data = arr2
        self.__cap *= 2

    def append(self, val: int) -> None:
        if self.__size >= self.__cap:
            self.__resize()
        self.__data[self.__size] = val
        self.__size += 1
        
    def __str__(self) -> str:
        return str(self.__data[:self.__size])

# l=MyArray(3)
# l.append(1)
# l.append(2)
# l.append(3)
# print(l)