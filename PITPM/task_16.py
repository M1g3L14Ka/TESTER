class User:
    __name = None
    __surname = None

    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname


user = User('john', 'smit')
print(user.getName())
print(user.getSurname())


class Employee:
    __name = None
    __salary = None
    __age = None

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def Getname(self):
        return self.__name

    def Getsalary(self):
        return self.__salary

    def Getage(self):
        return self.__age


worker = Employee('misha', 21312, 18)

print("Имя:", worker.Getname(), "зарплата:", worker.Getsalary(), "возраст:", worker.Getage())
