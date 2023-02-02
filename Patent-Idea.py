import smartpy as sp
class PatentIndia(sp.Contract):
    def __init__(self):
        self.init(
            base_fees= sp.mutez(200),
            ideaID=sp.TNat,
            admin= sp.address("tz1"),
            Idea= sp.record(
            index=sp.TNat, 
            owner=sp.TAddress,
            projectName=sp.TString,
            description=sp.TString,
            imageUrl=sp.TString,
            stage=sp.TNat,                
            validity=sp.TTimestamp
            ),
            ideas= sp.big_map(l={},tkey=sp.TNat,tvalue=sp.TRecord),
            owner_to_ideas=sp.big_map(l={},tkey=sp.TAddress,tvalue=sp.TList),
        )


    @sp.entry_point
    def patentYourIdea(self,params):
        sp.verify(sp.amount>=self.data.base_fees,"Inssufficient Balance to patent your idea")
        self.data.ideaID=self.data.ideaID+1
        # Validity for one year
        valid= sp.now + 365*24*60*60
        # record entries in big maps 
        rec = self.data.Idea(self.data.ideaID,sp.sender,params.name,prams.desc,params.imgurl,0,valid)
        ideas[ideaID]=rec;
        owner_to_ideas[sp.sender].push(rec)
        
    @sp.entry_point
    def updatePatentStage(self,params):
        sp.verify(params.id<=self.data.ideaID,"Record is not exist")
        idea= ideas[params.id]
        sp.verify(sp.sender==idea.owner,"You are not the owner of this proposal or idea")
        with sp.modify_record(idea,"data") as data:
            
            sp.if params._stage>=0:
                sp.if params._stage==1:
                    data.stage= sp.as_nat(1);

                sp.if params._stage==2:
                    data.stage= sp.as_nat(2);

                sp.if params._stage==3:
                    data.stage= sp.as_nat(3);

                sp.else :
                    data.stage= sp.as_nat(0); 


            sp.if params.name:
                data.projectName=params.name

            sp.if params.desc:
                data.description=params.desc

            sp.if params.imgurl:
                data.imageUrl=params.imgurl
               

    @sp.entry_point
    def deleteYourPatentIdea(self,params):
        sp.verify(params.id<=self.data.ideaID,"Record is not exist")
        idea= ideas[params.id]
        sp.verify(sp.sender==idea.owner,"You are not the owner of this proposal or idea")
        sp.verify(idea.validity>sp.now,"Validity still valid you can not remove patent from records")
        del ideas[params.id]
        
        






        
        
        
