# Implementation of Strategy Design Pattern with Documentations

"""
This script demonstrates the use of the Strategy Design Pattern to replace hardcoded or conditional logic
with flexible and extensible strategies. Each example highlights how to make systems adaptable to changes
without modifying existing code, adhering to key design principles.

Examples:
1. Sorting logic.
2. Payment processing.
3. Character behavior.
"""

# 1. Sorting Logic with Strategy Pattern
"""
Why:
   - Hardcoded sorting logic limits flexibility and makes the code harder to extend.
   - Strategy Pattern decouples the sorting logic, enabling dynamic changes.

Use:
   - Define a strategy interface and implement concrete strategies for each sorting behavior.

Pros:
   - Improves flexibility and reusability.
   - Makes it easy to add new sorting strategies without changing existing code.

Cons:
   - Requires additional classes, increasing initial development effort.
"""

# Wrong implementation with hardcoded sorting logic
class Data:
    def __init__(self, data):
        self.data = data

    def sort_data(self):
        # Hardcoded sorting algorithm
        self.data.sort()
        print("Data sorted in ascending order:", self.data)

# Usage
# data = Data([3, 1, 4, 1, 5, 9, 2, 6, 5])
# data.sort_data()

# Strategy interface
class SortingStrategy:
    def sort(self, data):
        pass

# Concrete Strategies
class AscendingSort(SortingStrategy):
    def sort(self, data):
        data.sort()
        return data

class DescendingSort(SortingStrategy):
    def sort(self, data):
        data.sort(reverse=True)
        return data

# Context class
class Data:
    def __init__(self, data, strategy: SortingStrategy):
        self.data = data
        self.strategy = strategy

    def sort_data(self):
        sorted_data = self.strategy.sort(self.data.copy())
        print("Data sorted:", sorted_data)

# Usage
data = Data([3, 1, 4, 1, 5, 9, 2, 6, 5], AscendingSort())
data.sort_data()

data.strategy = DescendingSort()
data.sort_data()

# 2. Payment Processing with Strategy Pattern
"""
Why:
   - Conditional logic for payment methods makes the code rigid and difficult to extend.
   - Strategy Pattern decouples payment logic, allowing dynamic method selection.

Use:
   - Define a strategy interface and implement concrete strategies for each payment method.

Pros:
   - Simplifies addition of new payment methods.
   - Reduces the risk of errors when modifying existing code.

Cons:
   - Adds complexity with more classes.
"""

# Wrong implementation with conditional statements
class PaymentProcessor:
    def pay(self, amount, payment_method):
        if payment_method == 'credit':
            print(f"Processing ${amount} via Credit Card.")
        elif payment_method == 'debit':
            print(f"Processing ${amount} via Debit Card.")
        elif payment_method == 'paypal':
            print(f"Processing ${amount} via PayPal.")
        else:
            print("Unknown payment method.")

# Usage
# processor = PaymentProcessor()
# processor.pay(100, 'credit')
# processor.pay(50, 'paypal')

# Strategy interface
class PaymentStrategy:
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing ${amount} via Credit Card.")

class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing ${amount} via Debit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Processing ${amount} via PayPal.")

# Context class
class PaymentProcessor:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def pay(self, amount):
        self.payment_strategy.pay(amount)

# Usage
processor = PaymentProcessor(CreditCardPayment())
processor.pay(100)

processor.payment_strategy = PayPalPayment()
processor.pay(50)

# 3. Character Behavior with Strategy Pattern
"""
Why:
   - Hardcoded behavior logic makes the code inflexible.
   - Strategy Pattern enables dynamic behavior changes.

Use:
   - Define a behavior interface and implement concrete strategies for each behavior.

Pros:
   - Simplifies adding new behaviors.
   - Enhances code flexibility and reuse.

Cons:
   - Requires additional setup for behavior classes.
"""

# Wrong implementation with conditional statements
class Character:
    def __init__(self, name, behavior):
        self.name = name
        self.behavior = behavior

    def perform_action(self):
        if self.behavior == 'attack':
            print(f"{self.name} is attacking.")
        elif self.behavior == 'defend':
            print(f"{self.name} is defending.")
        elif self.behavior == 'heal':
            print(f"{self.name} is healing.")
        else:
            print(f"{self.name} is standing still.")

# Usage
# hero = Character("Knight", "attack")
# hero.perform_action()

# hero.behavior = "heal"
# hero.perform_action()

# Strategy interface
class CharacterBehavior:
    def perform(self, character):
        pass

# Concrete Strategies
class AttackBehavior(CharacterBehavior):
    def perform(self, character):
        print(f"{character.name} is attacking.")

class DefendBehavior(CharacterBehavior):
    def perform(self, character):
        print(f"{character.name} is defending.")

class HealBehavior(CharacterBehavior):
    def perform(self, character):
        print(f"{character.name} is healing.")

# Context class
class Character:
    def __init__(self, name, behavior: CharacterBehavior):
        self.name = name
        self.behavior = behavior

    def perform_action(self):
        self.behavior.perform(self)

# Usage
attack = AttackBehavior()
hero = Character("Knight", attack)
hero.perform_action()

hero.behavior = HealBehavior()
hero.perform_action()
