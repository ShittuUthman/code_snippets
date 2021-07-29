
class Employee:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    def individual_description(self):
        return f"individual name is {self.first} {self.last}, and individual is {self.age} years old"

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith', '19')
emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
print(emp_1.individual_description())


del emp_1.fullname
