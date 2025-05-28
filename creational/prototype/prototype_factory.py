import copy

class Address:
    def __init__(self, street: str, city: str, suite: str):
        self.street = street
        self.city = city
        self.suite = suite
    
    def __str__(self):
        return f"Address(street={self.street}, city={self.city}, suite={self.suite})"

class Employee:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address
    
    def __str__(self):
        return f"Employee(name={self.name}, address={self.address})"

class EmployeeFactory:
    main_office_address = Employee("", Address("123 Main St", "Metropolis", "Suite"))
    aux_office_address = Employee("", Address("456 Side St", "Gotham", "Suite"))

    @staticmethod
    def _new_employee(proto: str, name: str, suite: str) -> Employee:
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name: str, suite: str) -> Employee:
        return EmployeeFactory._new_employee(
            EmployeeFactory.main_office_address, 
            name, 
            suite
        )
    
    @staticmethod
    def new_aux_office_employee(name: str, suite: str) -> Employee:
        return EmployeeFactory._new_employee(
            EmployeeFactory.aux_office_address, 
            name, 
            suite
        )

if __name__ == "__main__":
    john = EmployeeFactory.new_main_office_employee("John Doe", "A1")
    jane = EmployeeFactory.new_aux_office_employee("Jane Smith", "B2")
    
    print(john)  # Output: Employee(name=John Doe, address=Address(street=123 Main St, city=Metropolis, suite=A1))
    print(jane)  # Output: Employee(name=Jane Smith, address=Address(street=456 Side St, city=Gotham, suite=B2))
    
    # Changing the suite of Jane's address
    jane.address.suite = "C3"
    print(john)  # Output: Employee(name=Jane Smith, address=Address(street=456 Side St, city=Gotham, suite=C3))
    print(jane)  # Output: Employee(name=John Doe, address=Address(street=123 Main St, city=Metropolis, suite=A1))