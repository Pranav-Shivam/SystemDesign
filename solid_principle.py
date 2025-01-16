# SOLID Principles Demonstrated with Code Examples

"""
This code demonstrates the SOLID principles, which are fundamental to object-oriented design and software engineering.
Each principle aims to make systems easier to understand, maintain, and extend.

Principles:
1. Single Responsibility Principle (SRP): A class should only have one reason to change.
2. Open-Closed Principle (OCP): Classes should be open for extension but closed for modification.
3. Liskov Substitution Principle (LSP): Subtypes must be substitutable for their base types without altering correctness.
4. Interface Segregation Principle (ISP): No client should be forced to depend on methods it does not use.
5. Dependency Inversion Principle (DIP): High-level modules should not depend on low-level modules. Both should depend on abstractions.
"""

# 1. Single Responsibility Principle (SRP)
"""
Why:
   - Reduces complexity by separating concerns.
   - Makes classes easier to test and maintain.

Use:
   - Each class handles a single responsibility.

Pros:
   - Improves readability and maintainability.
   - Reduces coupling between functionalities.

Cons:
   - May lead to more classes and increased initial development effort.
"""

# NOT following SRP: Combines user data management and authentication in one class.
class UserWithAuth:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def authenticate(self, password):
        # Logic for authentication
        return self.password == password

# Following SRP: Separates user data management and authentication responsibilities.
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Auth:
    def authenticate(self, password, stored_password):
        # Logic for authentication
        return password == stored_password

# 2. Open-Closed Principle (OCP)
"""
Why:
   - Prevents modification of existing code when adding new features.

Use:
   - Use abstractions and polymorphism to extend functionality.

Pros:
   - Reduces risk of introducing bugs in existing functionality.
   - Encourages scalability.

Cons:
   - Requires careful planning and design.
"""

# NOT following OCP: Adding new shapes requires modifying the existing class.
class ShapeWithSwitch:
    def area(self, shape_type, dimensions):
        if shape_type == "circle":
            return 3.14 * dimensions["radius"] ** 2
        elif shape_type == "rectangle":
            return dimensions["width"] * dimensions["height"]

# Following OCP: Using polymorphism to extend functionality without modifying existing code.
class Shape:
    def area(self):
        raise NotImplementedError()

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# 3. Liskov Substitution Principle (LSP)
"""
Why:
   - Ensures that derived classes can be used interchangeably with their base class.

Use:
   - Design classes so that derived classes preserve the behavior of the base class.

Pros:
   - Enhances code reliability.
   - Makes polymorphism more predictable.

Cons:
   - Requires disciplined inheritance design.
"""

# NOT following LSP: Penguin class breaks expectations of the Bird class.
class Bird:
    def fly(self):
        return "Flying"

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")

# Following LSP: Separates flying and non-flying birds.
class BirdLSP:
    def lay_eggs(self):
        print("Laying eggs")

class FlyingBird(BirdLSP):
    def fly(self):
        print("Flying")

class Penguin(BirdLSP):
    def swim(self):
        print("Swimming")

# 4. Interface Segregation Principle (ISP)
"""
Why:
   - Avoids forcing clients to implement methods they do not need.

Use:
   - Use smaller, more specific interfaces.

Pros:
   - Reduces unused code in implementations.
   - Improves flexibility and clarity.

Cons:
   - Requires more interfaces, increasing initial effort.
"""

# NOT following ISP: Forces all clients to implement unused methods.
class MultiFunctionDevice:
    def print(self):
        raise NotImplementedError()

    def scan(self):
        raise NotImplementedError()

    def fax(self):
        raise NotImplementedError()

class Printer(MultiFunctionDevice):
    def print(self):
        print("Printing")
    # Forced to implement methods like scan or fax, even if not needed.

# Following ISP: Smaller, more specific interfaces.
class Printable:
    def print(self):
        raise NotImplementedError()

class Scannable:
    def scan(self):
        raise NotImplementedError()

class Printer(Printable):
    def print(self):
        print("Printing")

class Scanner(Scannable):
    def scan(self):
        print("Scanning")

# 5. Dependency Inversion Principle (DIP)
"""
Why:
   - Decouples high-level modules from low-level modules.

Use:
   - Use abstractions to make dependencies flexible.

Pros:
   - Improves scalability and testability.
   - Reduces coupling between modules.

Cons:
   - May require additional abstraction layers.
"""

# NOT following DIP: Manager is tightly coupled to Developer.
class Developer:
    def work(self):
        return "Writing code"

class ManagerWithoutDIP:
    def manage(self):
        dev = Developer()
        print(f"Managing: {dev.work()}")

# Following DIP: Both Manager and Developer depend on the abstraction `Employee`.
class Employee:
    def work(self):
        raise NotImplementedError()

class Developer(Employee):
    def work(self):
        return "Writing code"

class Designer(Employee):
    def work(self):
        return "Designing graphics"

class Manager:
    def manage(self, employee: Employee):
        print(f"Managing: {employee.work()}")

# Final Example Incorporating All Principles
if __name__ == "__main__":
    # SRP Example
    user = User(name="Alice", email="alice@example.com")
    auth = Auth()
    print(auth.authenticate("password123", "password123"))  # Output: True

    # OCP Example
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=6)
    print(f"Circle area: {circle.area()}")  # Output: 78.5
    print(f"Rectangle area: {rectangle.area()}")  # Output: 24

    # LSP Example
    sparrow = FlyingBird()
    penguin = Penguin()
    sparrow.fly()         # Output: Flying
    penguin.swim()        # Output: Swimming

    # ISP Example
    printer = Printer()
    scanner = Scanner()
    printer.print()       # Output: Printing
    scanner.scan()        # Output: Scanning

    # DIP Example
    dev = Developer()
    designer = Designer()
    manager = Manager()
    manager.manage(dev)       # Output: Managing: Writing code
    manager.manage(designer)  # Output: Managing: Designing graphics
