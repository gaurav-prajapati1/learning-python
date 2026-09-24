#  Encapsulation :
# Wrapping data and functions into single unite (object)

class A:
    _a = 10 # protected
    __b = 20 # private 
    def show(self):
        print(self._a)
        print(self.__b)
obj = A()
obj.show()


# Private Attribute and method 
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pasa = acc_pass
acc1 = Account("688086562","IRLPPHSNA")
print(acc1.acc_no)
print(acc1.acc_pass)
