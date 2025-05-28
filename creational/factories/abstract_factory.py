from abc import ABC, abstractmethod
from enum import Enum, auto

class HotDrink(ABC):
    @abstractmethod
    def consume(self) -> None:
        pass

class Tea(HotDrink):
    def consume(self) -> None:
        print("This tea is nice")

class Coffee(HotDrink):
    def consume(self) -> None:
        print("This coffee is delicious")

class HotDrinkFactory(ABC):
    def prepare(self, amount: int):
        pass

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount: int) -> HotDrink:
        print(f"Steeping tea for {amount} seconds")
        return Tea()

class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount: int) -> HotDrink:
        print(f"Dripping coffee for {amount} seconds")
        return Coffee()

class HotDrinkFactory(ABC):
    class AvailableDrinks(Enum):
        TEA = auto()
        COFFEE = auto()
    
    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrinks:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()

                self.factories.append((name, factory_instance))
    
    def make_drink(self):
        print("Available drinks:")
        for name, _ in self.factories:
            print(f"- {name}")

        choice = input(f"Choose a drink (0-{len(self.factories)-1}): ")
        idx = int(choice)

        s = input(f"Specify the amount: ")
        amount = int(s)

        return self.factories[idx][1].prepare(amount)


def make_drink(type: str) -> HotDrink:  
    factories = {
        "tea": TeaFactory(),
        "coffee": CoffeeFactory()
    }
    
    if type not in factories:
        raise ValueError(f"Unknown drink type: {type}")
    
    amount = int(input(f"How many seconds to prepare {type}? "))
    return factories[type].prepare(amount)

if __name__ == "__main__":
    # entry = input("What kind of hot drink would you like? (tea/coffee): ")
    # drink = make_drink(entry)
    # drink.consume()

    hdm = HotDrinkFactory()
    drink = hdm.make_drink()
    drink.consume()