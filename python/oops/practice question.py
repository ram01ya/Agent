# Create a class:

# BankAccount

# Requirements:

# Attributes:

# account_holder

# balance

# Methods:

# deposit(amount)

# withdraw(amount)

# check_balance()

# Rules:

# Withdraw should not allow negative balance

# Print proper messages

class BankAccount():
    def __init__(self,account_holder,balance):
        self.name=account_holder
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
        return  f"Deposited  amount:{amount}, Balance:{self.balance}"
    
    def withdraw(self,amount):
        if amount>0 and self.balance>amount:
            self.balance-=amount
            return f"Withdrawn amount:{amount}, Balance:{self.balance}"
        elif amount>self.balance or amount<0:
            return "Negative amount"

    def chek_balance(self):
        return self.balance

b1=BankAccount("John",1000)
print(b1.deposit(500))
print(b1.withdraw(200))
print(b1.withdraw(-10000))
print(b1.chek_balance())

# Create a class called:

# Employee

# Requirements:

# Attributes:

# name

# base_salary

# bonus_percentage

# Methods:

# calculate_bonus()

# calculate_total_salary()

# display_details()

# Rules:

# Bonus = base_salary * bonus_percentage / 100

# total_salary = base_salary + bonus

# No negative salary allowed

class Employee:
    def __init__(self, name, base_salary, bonus_percentage):
        if base_salary < 0:
            raise ValueError("Salary cannot be negative")
            
        self.name = name
        self.base_salary = base_salary
        self.bonus_percentage = bonus_percentage

    def calculate_bonus(self):
        return self.base_salary * self.bonus_percentage / 100

    def calculate_total_salary(self):
        return self.base_salary + self.calculate_bonus()

    def display_details(self):
        print(f"Employee: {self.name}")
        print(f"Base Salary: {self.base_salary}")
        print(f"Bonus: {self.calculate_bonus()}")
        print(f"Total Salary: {self.calculate_total_salary()}")

    
e1=Employee("Alice",55000,10)

print(e1.display_details())

# Base Class:

# Employee

# Attributes:

# name

# base_salary

# Method:

# calculate_salary() → returns base_salary

# Child Class 1:

# FullTimeEmployee

# Extra attribute:

# bonus

# Override:

# calculate_salary() → base_salary + bonus

# Child Class 2:

# PartTimeEmployee

# Extra attribute:

# hours_worked

# hourly_rate

# Override:

# calculate_salary() → hours_worked * hourly_rate

class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary

    def calculate_salary(self):
        return self.base_salary
    
class FullTimeEmployee(Employee):
    def __init__(self,name,base_salary,bonus):
        super().__init__(name,base_salary)
        self.bonus=bonus

    def calculate_salary(self,bonus):
        return self.base_salary+self.bonus
    
class PartTimeEmployee(Employee):
    def __init__(self,name,base_salary,hours_worked,hourly_rate):
        super().__init__(name,base_salary)
        self.hours_worked=hours_worked
        self.hourly_rate=hourly_rate

    def calculate_salary(self,hours_worked,hourly_rate):
        return self.hours_worked*hourly_rate
    
f1=FullTimeEmployee("Bob",60000,5000)
p1=PartTimeEmployee("Charlie",0,20,15)
print(f"Full time employee salary: {f1.calculate_salary(50000)}")
print(f"Part time employee salary: {p1.calculate_salary(20,15)}")


class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self._balance=balance

    def deposit(self,amount):
        if amount>0:
            return f"Account Holder: {self.account_holder} | Balance:{self._balance+amount}"
            
        else:
            return "Invalid Deposit amount" 
        
    def withdraw(self,amount):
        if amount > 0:
            return  f"Account Holder: {self.account_holder} | Balance:{self._balance-amount}"

        elif amount <0:
            return "Invalid Withdrawn amount"
        elif amount >self._balance:
            return "Insufficinet balance"
        
    def get_balance(self):
        return f"Account Holder: {self.account_holder} | Balance:{self._balance}"
    

b1=BankAccount("John",1000)
print(b1.deposit(500))
print(b1.withdraw(200))
print(b1.get_balance())

             
        
    
