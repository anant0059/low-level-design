class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f"Person(name={self.name}, dof={self.date_of_birth}, position={self.position})"
    
    @staticmethod
    def new():
        return PersonBuilder()

class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person

class PersonInfoBuilder(PersonBuilder):
    def called(self, name: str) -> 'PersonInfoBuilder':
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position: str) -> 'PersonJobBuilder':
        self.person.position = position
        return self

class PersonDateOfBirthBuilder(PersonJobBuilder):
    def born(self, date_of_birth: str) -> 'PersonJobBuilder':
        self.person.date_of_birth = date_of_birth
        return self

pb = PersonDateOfBirthBuilder()
me = pb\
    .called("John Doe")\
    .works_as_a("Software Engineer")\
    .born("1990-01-01")\
    .build()
print(me)  # Output: Person(name=John Doe, dof=1990-01-01, position=Software Engineer)