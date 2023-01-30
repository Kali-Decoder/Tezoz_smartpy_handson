import smartpy as sp
class Lottery(sp.Contract):
    def __init__(self):
        #storage we have to set players 
        self.init(
            players=sp.map(l={} , tkey=sp.TNat , tvalue=TAddress),
            ticket_cost= sp.tez(1),
            ticket_available=sp.nat(5),
            max_tickets=sp.nat(5)
        )


    @sp.entry_point
    def buy_ticket(self):
        #assertions
        sp.verify(self.data.ticket_available>0,"No tickets are available")
        sp.verify(sp.amount>=self.data.ticket_cost,"Insufficient ampount")
        #storage changes 
        #records the address of the users or tracking users 
        self.data.players[sp.len(self.data.players)]=sp.sender
        self.data.ticket_available=sp.as_nat(self.data.ticket_available-1)

        #return extra tez to sender again 
        extra_amount= (sp.amount-self.data.ticket_cost)
        sp.if extra_amount>sp.tez(0):
            sp.send(sp.sender,extra_amount)


    @sp.entry_point
    def end_game(self):
        #assertions
        sp.verify(self.data.ticket_available==0,"All tickets are not sold")

        #generates the random number 
        winner_index= (sp.as_nat(sp.now - sp.timestamp(0)) % self.data.ticket_available)
        winner_address = self.data.players[winner_index]
        sp.send(winner_address,sp.balance)

        #reset the contract again for playing 

        self.data.players={}
        self.data.ticket_available=self.data.max_tickets
        


#lets write some test for our lottery contract 

@sp.add_test(name="Lottery")
def test():
    scenerio = sp.test_scenario()

    #test accounts import 
    alice= sp.test_account("alice")
    bob= sp.test_account("bob")
    cat= sp.test_account("cat")
    dog= sp.test_account("dog")
    elephant= sp.test_account("elephant")
    

    #lets make contract instance 

    lottery = Lottery()
    scenerio+=lottery
    

    #let buy some tickets 
    scenerio+= lottery.buy_ticket().run(amount=sp.tez(1),sender=alice)
    scenerio+= lottery.buy_ticket().run(amount=sp.tez(5),sender=bob)
    scenerio+= lottery.buy_ticket().run(amount=sp.tez(8),sender=cat)
    scenerio+= lottery.buy_ticket().run(amount=sp.tez(9),sender=dog)
    scenerio+= lottery.buy_ticket().run(amount=sp.tez(1),sender=elephant)
    
    #execute end game function 

    scenerio+=lottery.end_game().run(now=sp.timestamp(5))









