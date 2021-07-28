from Receipt import Receipt


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls]  = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class STORE(metaclass=SingletonMeta):
    def __init__(self):
        self.receipts = []

    def add_receipt(self, r: Receipt):
        self.receipts.append(r)

if __name__ == '__main__':
    s1 = STORE()
    s2 = STORE()
    print(id(s1), id(s2))



