Python: Everything is Object
1. Introduction
In Python, everything — from numbers and strings to lists and even functions — is treated as an object. This means every value has a unique identity, a type, and, for some, a changeable state (mutability). Understanding this concept is key to writing reliable and efficient code in Python. This post explores object identity, mutability, and how Python handles data when passed into functions.

2. id() and type()
Every Python object has two fundamental characteristics:

Its type, which can be retrieved using type(object).

Its unique identifier, which is the memory address (in CPython), accessible using id(object).

These two functions help determine what kind of data you're working with and whether two variables point to the same object in memory.

3. Mutable Objects
A mutable object is one that can be modified after it has been created. You can change its content without changing its identity — the memory address stays the same.

python
Copier
Modifier
fruits = ["apple", "lemon"]
print(id(fruits))  # Example: 1398349824567654336
fruits.append("strawberry")
print(fruits)      # ["apple", "lemon", "strawberry"]
print(id(fruits))  # Same ID
Common mutable types in Python include list, dict, and set.

4. Immutable Objects
An immutable object cannot be modified after its creation. Any operation that seems to "modify" it will actually create a new object with a new memory address.

python
Copier
Modifier
word = "Hello"
print(id(word))       # Example: 133938243567220560
word += " World"
print(word)           # "Hello World"
print(id(word))       # Different memory address
Immutable types in Python include int, float, str, tuple, and bool.

5. Why It Matters: Mutable vs Immutable in Python
Understanding the difference is important because it affects how variables behave when they are copied or passed into functions.

Mutable example:
python
Copier
Modifier
a = [1, 2]
b = a
a.append(3)
print(b)  # [1, 2, 3] — both variables point to the same object
Immutable example:
python
Copier
Modifier
x = 10
y = x
x += 1
print(y)  # 10 — x now points to a different object
With mutable objects, modifications affect all references to that object. With immutable objects, modifications result in a new object, leaving existing references unchanged.

6. How Arguments Are Passed to Functions
In Python, arguments are passed by object reference (also called assignment semantics). This has different consequences depending on whether the object is mutable or immutable.

Mutable Example:
python
Copier
Modifier
def add_element(l):
    l.append("Python")

my_list = ["hello"]
add_element(my_list)
print(my_list)  # ["hello", "Python"]
Here, the list is modified inside the function because it is mutable.

Immutable Example:
python
Copier
Modifier
def add_one(n):
    n += 1
    print("Inside the function:", n)

x = 5
add_one(x)
print("Outside the function:", x)  # 5
Since integers are immutable, the original value remains unchanged.

7. Conclusion
Understanding that everything in Python is an object — and knowing how mutability, object identity, and function argument passing work — helps avoid subtle bugs and leads to better, more predictable code. These core ideas are foundational for mastering Python’s object model and writing clean, robust programs.