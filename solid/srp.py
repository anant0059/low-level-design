#SRP - Single Responsibility Principle
#SOC - Separation of Concerns

# The Single Responsibility Principle (SRP) states that a class should have only one reason to change, meaning that a class should have only one job or responsibility.

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)
    
    # def save(self, filename):
    #     pass

    # def load(self, filename):
    #     pass

    # def low_from_web(self, url):
    #     pass

class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w') as f:
            f.write(str(journal)) 
        file = open(filename, 'w')
        file.write(str(journal))
        file.close()



j = Journal()
j.add_entry('I cried today')
j.add_entry('I ate a bug')
print(f'Journal entries:\n{j}')
# print(j)


file = r'/Users/anantkumar/Desktop/LLD/solid/journal.txt'
PersistenceManager.save_to_file(j, file)

with open(file, 'r') as f:
    print(f.read())