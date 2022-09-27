class Person():
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    
    def display(self):
        return(self.name, self.idnumber)
    
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post =post
        super().__init__(name, idnumber)
    
    def display(self):
        print(super().display())
        print(self.salary)
        print(self.post)

if __name__ == "__main__":
    obj1 = Employee("Ajey", 101, 100000, "CEO")
    obj1.display()   