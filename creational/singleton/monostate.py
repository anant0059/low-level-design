class CEO:
    _shared_state = {
        "name": "John Doe",
        "age": 50
    }

    def __init__(self):
        self.__dict__ = self._shared_state

    def __str__(self):
        return f"CEO(name={self.name}, age={self.age})"

class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls)
        obj.__dict__ = cls._shared_state
        return obj

class CFO(Monostate):
    def __init__(self):
        self.name = "Jane Doe"
        self.money_managed = 45

    def __str__(self):
        return f"CFO(name={self.name}, age={self.money_managed})"

if __name__ == "__main__":
    ceo1 = CEO()
    ceo2 = CEO()

    print(ceo1)  # Output: CEO(name=John Doe, age=50)
    print(ceo2)  # Output: CEO(name=John Doe, age=50)

    ceo1.name = "Jane Smith"
    ceo1.age = 45

    print(ceo1)  # Output: CEO(name=Jane Smith, age=45)
    print(ceo2)  # Output: CEO(name=Jane Smith, age=45)

    cfo1 = CFO()
    cfo2 = CFO()
    print(cfo1)  # Output: CFO(name=Jane Doe, age=45)
    print(cfo2)  # Output: CFO(name=Jane Doe, age=45)
    cfo1.name = "Alice Johnson"
    cfo1.money_managed = 60
    print(cfo1)  # Output: CFO(name=Alice Johnson, age=60)
    print(cfo2)  # Output: CFO(name=Alice Johnson, age=60)
    print(ceo1 is ceo2)  # Output: False, both variables not point to the same instance
    print(cfo1.name is cfo2.name)  # Output: True, both name variables point to the same instance