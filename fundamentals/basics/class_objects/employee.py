class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname =  lname
        self.salary = salary
        
    def Calculate_paycheck(self):
        return float(self.salary)/52