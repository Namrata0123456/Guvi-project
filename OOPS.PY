class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.__balance = balance   # Encapsulation (private attribute)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance


# Subclass: Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0.0, interest_rate=0.03):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f"Interest earned: {interest}")
        return interest


# Subclass: Current Account
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance=0.0, min_balance=500):
        super().__init__(account_number, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if amount > 0:
            if self.get_balance() - amount >= self.min_balance:
                # Use parent withdraw method
                super().withdraw(amount)
            else:
                print("Withdrawal denied! Minimum balance requirement not met.")
        else:
            print("Invalid withdrawal amount.")


# ----------- Example Usage -----------
if __name__ == "__main__":
    # Savings account demo
    savings = SavingsAccount("SA123", 1000, 0.05)
    savings.deposit(500)
    savings.calculate_interest()
    savings.withdraw(200)

    print("\n")

    # Current account demo
    current = CurrentAccount("CA456", 2000, 1000)
    current.withdraw(500)   # Allowed
    current.withdraw(700)   # Denied (would drop below min balance)
#######
# Base class
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        # To be overridden by subclasses
        return self.base_salary

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.calculate_salary()}"


# Subclass: Regular Employee
class RegularEmployee(Employee):
    def __init__(self, name, base_salary, bonus=0):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


# Subclass: Contract Employee
class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, base_salary=0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


# Subclass: Manager
class Manager(Employee):
    def __init__(self, name, base_salary, incentive=0, allowance=0):
        super().__init__(name, base_salary)
        self.incentive = incentive
        self.allowance = allowance

    def calculate_salary(self):
        return self.base_salary + self.incentive + self.allowance


# -------- Example Usage --------
if __name__ == "__main__":
    employees = [
        RegularEmployee("lakshmi", 50000, bonus=5000),
        ContractEmployee("Ram", hourly_rate=1000, hours_worked=20),
        Manager("Shyam", 80000, incentive=10000, allowance=5000)
    ]

    for emp in employees:
        print(emp)
######

# Base class
class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate  # base rate per day or per hour

    def calculate_rental(self, duration):
        """To be overridden by subclasses"""
        return self.rental_rate * duration

    def __str__(self):
        return f"Vehicle: {self.model}, Rental Rate: {self.rental_rate}"


# Subclass: Car
class Car(Vehicle):
    def __init__(self, model, rental_rate, seats=4):
        super().__init__(model, rental_rate)
        self.seats = seats

    def calculate_rental(self, duration):
        # Cars have an additional fixed service fee
        service_fee = 500
        return (self.rental_rate * duration) + service_fee


# Subclass: Bike
class Bike(Vehicle):
    def __init__(self, model, rental_rate, helmet_included=True):
        super().__init__(model, rental_rate)
        self.helmet_included = helmet_included

    def calculate_rental(self, duration):
        # Bikes charge purely per hour/day, no extra fees
        return self.rental_rate * duration


# Subclass: Truck
class Truck(Vehicle):
    def __init__(self, model, rental_rate, load_capacity):
        super().__init__(model, rental_rate)
        self.load_capacity = load_capacity  # in tons

    def calculate_rental(self, duration):
        # Trucks have a surcharge depending on load capacity
        surcharge = 200 * self.load_capacity
        return (self.rental_rate * duration) + surcharge


# -------- Example Usage --------
if __name__ == "__main__":
    vehicles = [
        Car("Honda City", rental_rate=2000, seats=5),
        Bike("Yamaha FZ", rental_rate=500, helmet_included=True),
        Truck("Tata 407", rental_rate=3000, load_capacity=5)
    ]

    rental_duration = 3  # days
    for v in vehicles:
        print(f"{v.model} rental for {rental_duration} days: {v.calculate_rental(rental_duration)}")
