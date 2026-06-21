''' class : class is a blueprint or atemplate eg. for an exam that
 contains name,age,electives,father's name etc
#object: specific instance created from the template (class.). eg form
 which contains the data from john doe'''
class Employee:
    company="HP"

    def get_salary(self):
        return 34000
    

e=Employee()
print(e.get_salary())

e2=Employee()
print(e2.get_salary())
print(e2.company())