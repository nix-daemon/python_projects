class Soldier():
    raise_amount = 1.05
    num_of_Soldiers = 0
    def __init__(self, name, age, rank, pay = 0):
        self.name = name
        self.age = age
        self.rank = rank
        self.pay = pay
        Soldier.num_of_Soldiers += 1

    def SoldierPrint(self):
        return "{} {}".format(self.rank, self.name)

    def SetRaise(self):
        self.pay = self.pay * self.raise_amount

    def PrintPay(self):
        return "{} {} makes {} a year".format(self.rank, self.name, self.pay)

john = Soldier("Rutherford", 31, "WO1", 60000)
print(john.SoldierPrint())
john.SetRaise()
print(john.PrintPay())


#class Bank_Account():
#    def __init__(self, balance=0):
#        self.balance = balance
#
#    def Deposit(self, amount):
#        self.balance = self.balance + amount
#
#    def Withdrawal(self, amount):
#        if self.balance < amount:
#            print("Insufficiant Funds!")
#        else:
#            self.balance = self.balance - amount
#
#    def PrintBalance(self):
#        return "Your account balance is ${}".format(self.balance)
#myAccount = Bank_Account(100)
#myAccount.Withdrawal(100)
#myAccount.Deposit(1000)
#print(myAccount.PrintBalance())