class MyArray:
    def __init__(self, cap: int) -> None:
        self.__cap = cap
        self.__size = 0
        self.__data = [None] * cap

    def __len__(self) -> int:
        return self.__size

# l=MyArray(4)
# l.append(1)
# l.append(2)
# l.append(1)
# l.append(2)
# print(len(l))
# l.append(1)
# print(len(l))