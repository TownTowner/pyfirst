class Singleton:
    _instance = None

    @staticmethod
    def get_instance():
        if not Singleton._instance:
            Singleton._instance = Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance:
            raise Exception("This class is a singleton!")
        else:
            Singleton._instance = self
            self.value = 0

    def increment(self):
        self.value += 1


# 使用单例实例
singleton1 = Singleton.get_instance()
singleton2 = Singleton.get_instance()
singleton1.increment()
print(singleton2.value)
print(f"2:", singleton2.value)

singleton3 = Singleton()  # raise Exception("This class is a singleton!")
singleton3._instance.value = 100
print(singleton3.value)
