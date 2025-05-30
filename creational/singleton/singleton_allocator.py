import random

class Database:
    _instance = None

    def __init__(self):
        id = random.randint(1, 1000)
        print("id = ", id)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

if __name__ == "__main__":
    db1 = Database()
    db2 = Database()

    print(db1 is db2)  # Output: True, both variables point to the same instance
    print(id(db1), id(db2))  # Output: Same memory address for both instances
    