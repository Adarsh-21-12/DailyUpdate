class Student: 
    def __init__ (self, Name, marks):
        self.name = Name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print (self.name, sum/3)



student1 = Student("Adarsh", [33, 45, 50])
print(student1.name)
student1.get_avg()


class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no 
    
    def debit(self, amount):
        self.balance -= amount
        print(amount, "Money debited")

    def credit(self, amount):
        self.balance += amount
        print(amount, "Money Credited")

    def show_balance (self):
        print(self.balance)


c1 = Account(200, 1)
c1.debit(20)
c1.show_balance()
c1.credit(304)
c1.show_balance()

