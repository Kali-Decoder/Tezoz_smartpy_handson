// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

contract CRUD {
    address public admin;

    constructor() {
        admin = msg.sender;
    }

    string[] public techs;

    function addTech(string memory _data) public {
        techs.push(_data);
    }

    function getTechData(uint256 id) public view returns (string memory) {
        return techs[id];
    }

    function updateData(uint256 id, string memory newTechTerm)
        public
        crossCheck(id)
    {
        techs[id] = newTechTerm;
    }

    function deleteData(uint256 id) public crossCheck(id) {
        techs[id] = techs[techs.length - 1];
        techs.pop();
    }

    modifier crossCheck(uint256 id) {
        require(id < techs.length);
        _;
    }
}
