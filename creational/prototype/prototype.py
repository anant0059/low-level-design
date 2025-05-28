import copy

class Address:
    def __init__(self, street: str, city: str,country: str):
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f"Address(street={self.street}, city={self.city}, country={self.country})"

class Person:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Person(name={self.name}, address={self.address})"

address = Address("123 Elm St", "Springfield", "USA")
john = Person("John Doe", address)
print(john)
# jane = john
# jane.name = "Jane Doe"
# print(john)  # This will show that john's name has changed to "Jane Doe"
# print(jane)  # This will show that john's name has changed to "Jane Doe"

jane  = Person("Jane Doe", address)
print("----")
print(john)
print(jane)

jane.address.street = "456 Oak St"
print("----")
print(john)  # This will show that john's address has changed to "456 Oak St"
print(jane)  # This will show that jane's address has changed to "456 Oak St"


john1 = Person("John Doe", Address("123 Elm St", "Springfield", "USA"))
jane1 = copy.deepcopy(john1)
jane1.name = "Jane Doe"
jane1.address.street = "456 Oak St"
print("----")
print(john1)  # This will show that john's name and address remain unchanged
print(jane1)  # This will show that jane's name is "Jane Doe" and address is unchanged
