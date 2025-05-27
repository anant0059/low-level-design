class Person:
    def __init__(self):
        #address
        self.street_address = None
        self.postcode = None
        self.city = None
        #employment
        self.company_name = None
        self.position = None
        self.annual_income = None
    
    def __str__(self):
        return f'Person: {self.street_address}, {self.postcode}, {self.city}, {self.company_name}, {self.position}, {self.annual_income}'
    
class PersonBuilder:
    def __init__(self, person: Person = None):
        if person is None:
            self.person = Person()
        else:
            self.person = person
    
    @property
    def works(self) -> 'PersonJobBuilder':
        return PersonJobBuilder(self.person)

    @property
    def lives(self) -> 'PersonAddressBuilder':
        return PersonAddressBuilder(self.person)
    
    def build(self) -> Person:
        return self.person

class PersonJobBuilder(PersonBuilder):
    def __init__(self, person: Person = None):
        super().__init__(person)
    
    def at(self, company_name: str) -> 'PersonJobBuilder':
        self.person.company_name = company_name
        return self
    
    def as_a(self, position: str) -> 'PersonJobBuilder':
        self.person.position = position
        return self
    
    def earning(self, annual_income: float) -> 'PersonJobBuilder':
        self.person.annual_income = annual_income
        return self

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person: Person = None):
        super().__init__(person)
    
    def at(self, street_address: str) -> 'PersonJobBuilder':
        self.person.street_address = street_address
        return self
    
    def with_postcode(self, postcode: str) -> 'PersonJobBuilder':
        self.person.postcode = postcode
        return self
    
    def in_city(self, city: float) -> 'PersonJobBuilder':
        self.person.city = city
        return self

pb = PersonBuilder()

person = pb\
    .lives.at('123 London Road') \
    .with_postcode('SW1 1AA') \
    .in_city('London') \
    .works.at('Fabrikam') \
    .as_a('Engineer') \
    .earning(123000) \
    .build()
print(person)
# Output: Person: 123 London Road, SW1 1AA, London, Fabrikam, Engineer, 123000
# This code demonstrates the Builder pattern, allowing for a fluent interface to build complex objects step by step.
# The PersonBuilder class serves as the main builder, while PersonJobBuilder and PersonAddressBuilder handle specific aspects of the Person object.
# This pattern is useful for creating objects with many optional parameters or complex initialization logic.
# The Builder pattern is a creational design pattern that allows for the step-by-step construction of complex objects.