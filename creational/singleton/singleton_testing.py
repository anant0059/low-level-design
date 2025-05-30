import unittest

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self):
        self.population = {}
        f = open("population.txt", "r")
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            country = lines[i].strip()
            population = int(lines[i + 1].strip())
            self.population[country] = population
        f.close()

class SinletonRecordFinder:
    def total_population(self, cities):
        result = 0
        for city in cities:
            result += Database().population.get(city, 0)
        return result
    
class ConfigurableRecordFinder:
    def __init__(self, database):
        self.database = database

    def total_population(self, cities):
        result = 0
        for city in cities:
            result += self.database.population.get(city, 0)
        return result

class DummyDatabase:
    def __init__(self):
        self.population = {
            'Seoul': 17500000,
            'Sao Pulao': 17700000,
            'New York': 8000000
        }
    
    def get_population(self, city):
        return self.population.get(city, 0)

class SingletonTests(unittest.TestCase):
    def test_singleton(self):
        db1 = Database()
        db2 = Database()
        self.assertEqual(db1, db2)

    def test_population(self):
        finder = SinletonRecordFinder()
        self.assertEqual(finder.total_population(['Seoul']), 17500000)
        self.assertEqual(finder.total_population(['Sao Pulao']), 17700000)
    
    ddb = DummyDatabase()

    def test_dependent_total_population(self):
        finder = ConfigurableRecordFinder(self.ddb)
        self.assertEqual(finder.total_population(['Seoul']), 17500000)
        self.assertEqual(finder.total_population(['Sao Pulao']), 17700000)
        self.assertEqual(finder.total_population(['New York']), 8000000)
        self.assertEqual(finder.total_population(['Unknown City']), 0)

if __name__ == "__main__":
    unittest.main()