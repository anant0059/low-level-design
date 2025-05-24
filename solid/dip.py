#DIP - Dependency Inversion Principle
#
# The Dependency Inversion Principle (DIP) states that high-level modules should not depend on low-level modules, but both should depend on abstractions. This means that the details should depend on the abstractions, not the other way around.
from enum import Enum
from abc import ABC, abstractmethod

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name: str):
        self.name = name
#Bad Practice
class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent: Person, child: Person):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

class Research:
    def __init__(self, relationships: Relationships):
        self.relations = relationships.relations
        for r in self.relations:
            if r[0].name == 'John' and r[1] == Relationship.PARENT:
                print(f'John has a child named {r[2].name}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)
research = Research(relationships)

# Good Practice
class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name: str):
        pass

class RelationshipsBetter(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent: Person, child: Person):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name: str):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

class ResearchBetter:
    def __init__(self, browser: RelationshipBrowser):
        for child_name in browser.find_all_children_of('John'):
            print(f'John has a child named {child_name}')


parent_better = Person('John')
child1_better = Person('Chris')
child2_better = Person('Matt')
relationships_better = RelationshipsBetter()
relationships_better.add_parent_and_child(parent_better, child1_better)
relationships_better.add_parent_and_child(parent_better, child2_better)
research_better = ResearchBetter(relationships_better)