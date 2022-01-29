class Worker:
    def __init__(self, name, pay):                  # intialize when created
        self.name = name                            # self is the new object
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]                # split string on blanks
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)                 # update pay in place

bob = Worker('bob Smith',50000)                     # make 2 instances
sue = Worker('sue Jones', 60000)                    # each has name and pay
print(bob.lastName())                               # call method: bob is self
print(sue.lastName())                               # sue is self
sue.giveRaise(.10)                                  # update sues pay
print(sue.pay)
