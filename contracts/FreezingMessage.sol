pragma solidity ^0.8.0;

contract FreezingMessage {
    struct Message {
        address from;
        string message;
        uint256 createdBlockNumber;
        uint256 freezingGracePeriod;
    }
    
    event Write(Message message);
    event Edit(Message message);

    uint256 public messageCount = 0;
    Message[] public messages;
    
    modifier onlyUnfrozen(uint256 index, uint256 blockNumber) {
        require(
                messages[index].createdBlockNumber + messages[index].freezingGracePeriod >= blockNumber,
                "frozen"
        );
        _;
    }

    constructor(){}

    function write(string memory _message, uint256 _freezingGracePeriod) public returns (uint256) {
        messages.push(Message(msg.sender, _message, block.number, _freezingGracePeriod));
        return messages.length-1;
        emit Write(messages[messageCount]);
        messageCount+=1;
    }
    
    function edit(uint256 index, string memory _message) public onlyUnfrozen(index, block.number){
        messages[index].message = _message;
        emit Edit(messages[index]);
    }

}
