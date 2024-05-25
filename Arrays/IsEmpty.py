class MyArray:
    def __init__(self, cap: int) -> None:
        self.__cap = cap
        self.__size = 0
        self.__data = [None] * cap

    def IsEmpty(self) -> int:
        if self.__size==0:
            return True
        return False

# l=MyArray(3)
# print(l.IsEmpty())
# l.append(1)
# print(l.IsEmpty())