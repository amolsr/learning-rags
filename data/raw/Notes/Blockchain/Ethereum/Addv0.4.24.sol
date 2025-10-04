pragma solidity ^0.4.24;
contract Add {
    uint public result;

    constructor() public {
    result = 0;
    }

    function setResult(uint num1, uint num2) public {
        result=num1+num2;
    }

    function getAdd() public view returns (uint) {
        return result;
    }
}