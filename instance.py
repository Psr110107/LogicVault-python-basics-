class Employee:
 company="asus"

 def __init__(self,salary,name,bond,company):
    self.salary=salary
    self.name=name
    self.bond=bond
    self.company=company

 def get_salary (self):
     return self.salary



 def get_info(self):
      print("the name of employee is {self.name}. salary is {self.salary}.the bond is for {self.bond}years")

e1=Employee(34000,"john doe",4,"asus")

print(e1.company)
print(Employee.company)

print(dir(e1))