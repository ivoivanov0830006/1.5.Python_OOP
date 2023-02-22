class Employee:
    def __init__(self, id, first_name, last_name, salary):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def raise_salary(self, current_raise):
        self.salary += current_raise
        return self.salary

    def get_annual_salary(self):
        result = 12 * self.salary
        return result


employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())


"""
------------------------------------ Problem to resolve --------------------------------

Create class Employee. Upon initialization, it should receive id (number), first_name (string), 
last_name (string) and salary (number). Create 3 additional instance methods:
⦁	get_full_name() - returns "{first_name} {last_name}"
⦁	get_annual_salary() - returns the total salary for 12 months
⦁	raise_salary(amount) - increases the salary by the given amount and returns the new salary
-------------------------------------- Example inputs ----------------------------------
Test Code	
employee = Employee(744423129, "John", "Smith", 1000)
print(employee.get_full_name())
print(employee.raise_salary(500))
print(employee.get_annual_salary())	
Output
John Smith
1500
18000

"""
