from enum import Enum, IntEnum, StrEnum, auto


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Grade(IntEnum):
    A = 90
    B = 80
    C = 70


class Role(StrEnum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"
    OTHER = auto()  #


class C:
    count = 0

    def __init__(self):
        self.add()

    @classmethod
    def add(cls):
        cls.count += 1

    @classmethod
    def get_count(cls):
        print(f"该类一共实例化了{cls.count}个对象。")

    @staticmethod
    def get_c(cls):
        print(f"该类一共实lihua了{cls.count}个对象。")


class D(C):
    count = 0


class E(C):
    count = 0

    def __init__(self):
        super().__init__()
        self._x = 250

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x
