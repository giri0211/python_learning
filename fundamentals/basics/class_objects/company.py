from employee import Employee

class Company:
    def __init__(self):
        self.employees = []
    
    def Add_employees(self, employee):
        self.employees.append(employee)
        
    def Calc_paycheck(self):
        print('Paycheck for employees')
        for employee in self.employees:
            salary = employee.Calculate_paycheck()
            print(employee.fname, employee.lname, 'salary is:', f'${salary:,.2f}')
        print('------------------------')
        
    def List_employees(self):
        print('Current employees')
        for emp in self.employees:
            print(emp.fname, emp.lname)
        print('--------------')
        
def main():
    company = Company()
    employee1 = Employee('girish', 'tirumalasetti', '1000')
    employee2 = Employee('ramesh', 'ratnala', '2000')
    company.Add_employees(employee1)
    company.Add_employees(employee2)
    
    # company.List_employees()
    company.Calc_paycheck()

main()