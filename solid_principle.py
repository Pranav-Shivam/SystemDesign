# SOLID Principles Demonstrated with Code Examples

# 1. Single Responsibility Principle (SRP)
#    A class should have only one reason to change, focusing on a single responsibility.

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
#    A class should be open for extension but closed for modification.

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
#    Subtypes must be substitutable for their base types without altering correctness.

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
#    No client should be forced to depend on methods it does not use.

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
#    High-level modules should not depend on low-level modules. Both should depend on abstractions.

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
