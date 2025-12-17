class Employee:
    def __init__(self, name, id):
        self._name = name
        self._id = id

    def get_salary(self):
        return 0

    def get_info(self):
        return f"Сотрудник: {self._name}, ID: {self._id}"

class HourlyEmployee(Employee):
    def __init__(self, name, id, hourly_rate):
        super().__init__(name, id)
        self.hourly_rate = hourly_rate
        self._hours_worked = 0

    def add_hours(self, hours):
        self._hours_worked += hours

    def get_salary(self):
        salary = self.hourly_rate * self._hours_worked
        self._hours_worked = 0
        return salary

class SalariedEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def get_salary(self):
        return self.monthly_salary

def print_payroll(employees):
    for employee in employees:
        print(employee.get_info())
        print(f"Зарплата: {employee.get_salary()} руб.")
        print("-" * 30)


# пример
emp1 = HourlyEmployee("Иван", 101, 500)
emp1.add_hours(160)

emp2 = SalariedEmployee("Анна", 102, 80000)

employees = [emp1, emp2]

print_payroll(employees)
