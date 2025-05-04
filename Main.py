class Student:
    Uni = "KBTU"
    
    def __init__(self, name="Unknown", group="Unknown", studID=0, gpa=1.0, money=0):
        self.name = name
        self.group = group
        self.studentID = studID
        self.gpa = gpa
        self.money = money

    def __bool__(self):
        return self.gpa >= 2.0

    def __str__(self):
        return f"Student {self.name} has GPA {self.gpa} and ${self.money} money"

    def sayHello(self):
        print(f"Hello, my name is {self.name}. I study in {self.group} group.")

    def Info(self):
        print("Name:", self.name)
        print("Group:", self.group)
        print("ID:", self.studentID)
        print("University:", self.Uni)
        print("Money:", self.money)

    def work(self, amount):
        if amount > 0:
            self.money += amount
            print(f"{self.name} worked and earned ${amount}. Total money: ${self.money}")
        else:
            print("Amount to earn must be positive.")

    def rest(self, cost):
        if cost <= self.money:
            self.money -= cost
            print(f"{self.name} rested and spent ${cost}. Remaining money: ${self.money}")
        else:
            print(f"{self.name} doesn't have enough money to rest. Needs ${cost}, has ${self.money}")
      
s1 = Student("Egor", "GE2542", 4131, 2.5, 10)
print(s1)

s1.work(20)
s1.rest(5)
s1.rest(30)

s1.Info()
