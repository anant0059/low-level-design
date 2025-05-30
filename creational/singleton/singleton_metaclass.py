class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self):
        print("Database initialized")

if __name__ == "__main__":
    db1 = Database()
    db2 = Database()

    print(db1 is db2)  # Output: True, both variables point to the same instance
    print(id(db1), id(db2))  # Output: Same memory address for both instances