import smartpy as sp;
class MyContract(sp.Contract):
    def __init__(self,value):
        self.init(storedValue=value)

    def store(self,value):
        self.data.storedValue=value
def test():
        scenario= sp.test_scenario()
        contract=MyContract(1);
        scenario+=contract
        contract.store(3)


sp.add_compilation_target("my_contract_compiled",MyContract(2))    
            
