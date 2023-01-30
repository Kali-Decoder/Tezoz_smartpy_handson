import smartpy as sp 
class Calculator(sp.Contract):
    def __init__(self):
        self.init(value=sp.nat(0))

    @sp.entry_point
    def add(self,x,y):
        self.data.value=x+y


    @sp.entry_point
    def sub(self,x,y):
        self.data.value=sp.as_nat(x-y)


    @sp.entry_point
    def multiply(self,x,y):
        self.data.value=x*y


    @sp.entry_point
    def square(self,x):
        self.data.value=x*x


    @sp.entry_point
    def div(self,x,y):
        self.data.value=x/y



    @sp.add_test(name = "Calculator")
    def test():
        ob = Calculator()
        scenario = sp.test_scenario()
        scenario += ob
        admin  = sp.test_account("admin")
        
        scenario +=ob.multiply(x = 4, y = 2)
        scenario +=ob.add(x = 4, y = 2)
        scenario +=ob.sub(x = 11, y = 5)
        scenario +=ob.div(x = 15, y = 3)

       

