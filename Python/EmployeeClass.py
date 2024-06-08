class Employee:
    employee_count = 0
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        Employee.increment_employee_count()
        
    @classmethod
    def increment_employee_count(cls):
        cls.employee_count += 1

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    @staticmethod
    def is_valid_employee_id(employee_id):
        return isinstance(employee_id, str) and employee_id.isdigit()

employee1 = Employee("John Doe", "12345")
employee2 = Employee("Jane Smith", "67890")

print(Employee.get_employee_count())  
print(Employee.is_valid_employee_id("12345"))  
print(Employee.is_valid_employee_id("1234A"))