**README - Python Terminology Quick Reference**

A concise guide to common Python special methods and keywords for quick revision, with examples.

---

## `self` vs `cls`

* **`self`**

  * Refers to the **instance** of a class inside instance methods.
  * Used to access or modify **instance attributes**.

  **Example:**

  ```python
  class Dog:
      def __init__(self, name):
          self.name = name  # 'self' refers to this specific Dog instance

  dog1 = Dog("Rocky")
  print(dog1.name)  # Output: Rocky
  ```

* **`cls`**

  * Refers to the **class itself** inside class methods and special methods like `__new__`.
  * Used to access or modify **class attributes**.

  **Example:**

  ```python
  class Dog:
      total_dogs = 0

      def __new__(cls, *args, **kwargs):
          # 'cls' refers to the Dog class, not an instance
          cls.total_dogs += 1
          return super().__new__(cls)

  d1 = Dog()
  d2 = Dog()
  print(Dog.total_dogs)  # Output: 2
  ```

---

## Variable Argument Lists: `*args` & `**kwargs`

* **`*args`** captures extra **positional** arguments as a tuple.
* **`**kwargs`** captures extra **keyword** arguments as a dict.
* They allow functions/methods to accept a flexible number of inputs.

**Example with both:**

```python
def show_data(*args, **kwargs):
    print('Positional args:', args)
    print('Keyword args:', kwargs)

show_data(10, 20, a=1, b=2)
# Output:
# Positional args: (10, 20)
# Keyword args: {'a': 1, 'b': 2}
```

Another example:

```python
def greet(*names, **options):
    sep = options.get('sep', ' ')
    message = options.get('msg', 'Hello')
    print(message + sep + sep.join(names))

# Using it:
greet('Anant', 'Sonam', msg='Hi', sep=' & ')
# Output: Hi & Anant & Sonam
```

---

## `super()`

* Returns a **proxy** object to call methods of a parent class in the MRO (Method Resolution Order).
* **Zero-arg** form (`super()`) is available in Python 3+ and infers class and instance automatically.
* **Explicit** form (`super(ClassName, self)`) names the class and instance for compatibility or clarity.

**Zero-arg example:**

```python
class Base:
    def greet(self):
        print('Hello from Base')

class Child(Base):
    def greet(self):
        super().greet()  # calls Base.greet()
        print('Hello from Child')

Child().greet()
# Output:
# Hello from Base
# Hello from Child
```

**Explicit form example:**

```python
class Child(Base):
    def greet(self):
        super(Child, self).greet()
        print('Hello again from Child')
```

---

## Common Special (Dunder) Methods

Special methods (aka “magic methods”) are identified by the double underscores (`__`) before and after their names. They let you customize core behaviors.

| Method                     | Purpose                                                         | Example                               |
| -------------------------- | --------------------------------------------------------------- | ------------------------------------- |
| `__init__(self, ...)`      | Initialization: sets up instance after creation.                | See `Point` example below.            |
| `__new__(cls, ...)`        | Creation: allocates and returns new instance before `__init__`. | Used in singleton or immutable types. |
| `__str__(self)`            | Human-readable str with `str(obj)` or `print(obj)`.             | `"Point(1, 2)"`                       |
| `__repr__(self)`           | Unambiguous repr for devs and REPL.                             | `"Point(1, 2)"`                       |
| `__eq__(self, other)`      | Equality `==`. Returns `True/False`.                            | `Point(1,2) == Point(1,2)`            |
| `__add__`, `__sub__`, etc. | Arithmetic operations.                                          | `p1 + p2`                             |
| `__len__(self)`            | Length of container with `len(obj)`.                            | `len([1,2,3]) # 3`                    |
| `__getitem__(self, k)`     | Indexing/slicing: `obj[k]`.                                     | `mylist[0]`                           |
| `__iter__(self)`           | Returns iterator (for loops).                                   | `for x in obj: ...`                   |
| `__call__(self, ...)`      | Make instance callable like function: `obj()`.                  | `f = Foo(); f()`                      |
| `__enter__/__exit__`       | Context manager (`with` statement).                             | See `Resource` example below.         |

### Examples of Dunder Methods

**Point class:**

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Output: Point(4, 6)
```

**Resource context manager:**

```python
class Resource:
    def __enter__(self):
        print("Acquiring resource")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing resource")

with Resource() as r:
    print("Using resource")
# Output:
# Acquiring resource
# Using resource
# Releasing resource
```
