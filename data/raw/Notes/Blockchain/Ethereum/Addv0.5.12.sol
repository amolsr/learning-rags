pragma solidity ^0.5.12;
contract Add {
    uint public result;

    constructor() public {
    result = 0;
    }

    function setResult(uint a, uint b) public {
        result=a+b;
    }
}