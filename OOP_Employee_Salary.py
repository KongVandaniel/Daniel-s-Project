class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []  # Each company has its own employee list

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_company_info(self, number):
        print(f"\nCompany {number}")
        print(f"===== Company: {self.name} =====")

        count = 1
        for employee in self.employees:
            employee.display_info(count)
            count += 1


class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def display_info(self, number):
        print(f"\nEmployee {number}")
        print(f"Employee Name     : {self.name}")
        print(f"Employee Age      : {self.age} Years Old")
        print(f"Employee Position : {self.position}")
        print(f"Employee Salary   : ${self.salary}\n")

    def increase_salary(self, amount):
        self.salary += amount                       # Increase the salary by the specified amount


companies = []


# Company Loop
while True:
    company_name = input("\nEnter Company Name (or type 'stop' to finish): ")

    if company_name.lower() == "stop":
        break

    company = Company(company_name)

    # Employee Loop
    while True:
        name = input("\nEnter Employee Name (or type 'stop' to finish): ")

        if name.lower() == "stop":
            break

        age = int(input("Enter Employee Age: "))
        position = input("Enter Employee Position: ")
        salary = float(input("Enter Employee Salary: "))

        employee = Employee(name, age, position, salary)

        employee.increase_salary(100)                       # Increase salary by $100 for each employee

        company.add_employee(employee)

    companies.append(company)


# Display Everything
print("\n========== ALL COMPANIES ==========")

for i, company in enumerate(companies, start=1):
    company.display_company_info(i)
