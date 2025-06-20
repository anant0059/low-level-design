def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Database initialized")


if __name__ == "__main__":
    db1 = Database()
    db2 = Database()

    print(db1 is db2)  # Output: True, both variables point to the same instance
    print(id(db1), id(db2))  # Output: Same memory address for both instances