// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

contract PatentIndia{
    address public admin ;
    uint constant public base_fees= 100 wei;
    enum Stage{
        PROPOSAL_ACCEPTED,
        STARTING_STAGE,
        ONGOING_STAGE,
        COMPLETED_STAGE
    }
    struct Idea{
        uint index;
        address owner;
        Stage stage;
        string projectName;
        string description;
        string imageUrl;
        uint validity;
    }
    mapping(uint=>Idea) public ideas;
    mapping(address=>Idea[]) public owner_to_ideas;
    uint public ideaId;

    //Create Operation 
    function patentYourIdea(string calldata _name,string calldata _desc,string calldata _url,Stage _stage) public payable returns(bool){
        require(msg.value>=base_fees,"Inssufficient Balance to patent your idea");
        uint valid= block.timestamp + 365*24*60*60;// Validity for one year
        ideaId++;
        Idea memory _idea= Idea(ideaId,msg.sender,_stage,_name,_desc,_url,valid);
        
        ideas[ideaId]=_idea;
        owner_to_ideas[msg.sender].push(_idea);
        return true;
    }

    // Read Operation on Patent Ideas List

    function readPatentIdea(uint _id) public view returns(string memory , string memory,uint){
        require(_id<=ideaId,"Not Proposal is exist");
        Idea storage _idea = ideas[_id];
        require(msg.sender==_idea.owner,"You are not the owner of this proposal or idea");
        return (_idea.projectName,_idea.description,_idea.validity);

    }

    //Update Your Patent Idea Details 
    function updatePatentStage(uint _id,uint _stage) public returns(bool){
        require(_id<=ideaId,"Not Proposal is exist");
        Idea storage _idea = ideas[_id];
        require(msg.sender==_idea.owner,"You are not the owner of this proposal or idea");
        if(_stage==1){
            _idea.stage= Stage.STARTING_STAGE;
        }else if(_stage==2){
            _idea.stage= Stage.ONGOING_STAGE;
        }else if(_stage==3){
            _idea.stage= Stage.COMPLETED_STAGE;
        }else{
           _idea.stage= Stage.PROPOSAL_ACCEPTED; 
        }
        return true;
    }
    // Delete Operation on Patent Idea list 
    function deletePatentIdea(uint _id) public returns(bool){
        require(_id<=ideaId,"Not Proposal is exist");
        Idea storage _idea = ideas[_id];
        require(msg.sender==_idea.owner,"You are not the owner of this proposal or idea");
        require(_idea.validity<block.timestamp,"Time vilidity is not over");
        delete ideas[_id];

        for(uint i=0;i<owner_to_ideas[msg.sender].length;i++){
            Idea storage _idea1 = owner_to_ideas[msg.sender][i];
            if(_idea1.index==_id){
                Idea storage temp = _idea1;
                owner_to_ideas[msg.sender][i]= owner_to_ideas[msg.sender][owner_to_ideas[msg.sender].length-1];
                owner_to_ideas[msg.sender][owner_to_ideas[msg.sender].length-1]= temp;
                owner_to_ideas[msg.sender].pop();
                return true;
            }
        }

        return true;

    }







}
