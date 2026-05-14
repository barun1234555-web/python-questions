class Employee:
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def annual_salary(self):
        return self.monthly_salary * 12

emp = Employee("John", 5000)
print(f"Employee: {emp.name}, Annual Salary: {emp.annual_salary()}")