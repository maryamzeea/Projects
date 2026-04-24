#employee details, salaries, manager and regular employee

class Employee:
    def __init__(self, name, salary,id):
        self.name = name
        self.salary = salary
        self.id = id

    def display_info(self):
        print("\n====Employee Information====")
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("ID:",self.id)

    def bonus(self):
        print(f"Bonus:{self.salary * 0.1}")

class manager(Employee):
    def __init__(self, name, salary, id,department):
        Employee.__init__(self, name, salary, id)
        self.department = department

    def display_info(self):
        Employee.display_info(self)
        print("Department:",self.department)

    def bonus(self):
        print(f"Bonus:{self.salary * 0.2}")



class Developer(Employee):
    def __init__(self, name, salary, id,programminglanguage):
        Employee.__init__(self, name, salary, id)
        self.programminglanguage = programminglanguage

    def display_info(self):
        Employee.display_info(self)
        print("Programming Language:",self.programminglanguage)

    def bonus(self):
        print(f"Bonus:{self.salary * 0.05}")


employees = []
def add_employee():
    print("\n===Adding employee===")
    print("1. Regular Employee\n2. Manager\n3. Developer")
    choice = int(input("Enter your choice: "))

    name = input("Enter employee name: ")
    salary = int(input("Enter employee salary: "))
    id = input("Enter employee id: ")
    if choice == 1:
        employees.append(Employee(name,salary,id))
    elif choice == 2:
        department = input("Enter employee department: ")
        employees.append(manager(name,salary,id,department))
    elif choice == 3:
        programminglanguage = input("Enter programming language: ")
        employees.append(Developer(name,salary,id,programminglanguage))

    else:
        print("Invalid choice!")

def display_employee():
    for employee in employees:
        employee.display_info()
        employee.bonus()

while True:

    print("\n===Employee Management System===")
    print("1. Add Employee")
    print("2. Display Employee")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_employee()
    elif choice == 2:
        display_employee()
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")


