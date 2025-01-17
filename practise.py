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



try:
    n = int(input("Enter an integer: "))
    print("Number entered", n)

except ValueError:
    print("Invalid input")


try:
    a = float(input("enter 1st number "))
    b = float(input("Enter 2nd number"))

    result = a/b
    print(result)

except ZeroDivisionError:
    print("Division by zero is not allowed")
except ValueError:
    print(" enter numeric values")




n = int(input().strip())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 1 < n < 6 :
    print("Not Weird")
elif n % 2 == 0 and 5 < n < 21 :
    print("Weird")
elif n % 2 == 0 and n > 21:
    print("Not Weird")



import socket

s = socket.socket()
print("Socket created")

s.bind(('localhost', 9999))

s.listen(3)
print("Waiting")

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Client connected", addr)
    
    c.send(bytes("Welcome here", 'utf-8'))

    c.close()



import socket

c = socket.socket()

c.connect(('localhost', 9999))

name = input("Enter Name ")
c.send(bytes(name, 'utf-8'))


print(c.recv(1024).decode())
