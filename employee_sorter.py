class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def print_employees(self):
        for employee in self.employees:
            print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

    def sort_employees(self, key):
        if key == 1:
            self.employees.sort(key=lambda x: x.age)
        elif key == 2:
            self.employees.sort(key=lambda x: x.name)
        elif key == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting key")

if __name__ == "__main__":
    company = Company()

    
    company.add_employee(Employee("161E90", "Ramu", 35, 59000))
    company.add_employee(Employee("171E22", "Tejas", 30, 82100))
    company.add_employee(Employee("171G55", "Abhi", 25, 100000))
    company.add_employee(Employee("152K46", "Jaya", 32, 85000))

    
    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    sorting_key = int(input("Enter your choice: "))

    
    company.sort_employees(sorting_key)
    print("\nSorted Employee Data:")
    company.print_employees()
