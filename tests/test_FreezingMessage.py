from brownie import accounts, reverts

class TestDeploy:
    def test(self, FreezingMessage, users):
        issuer = users['issuer']
        freezingMessage = issuer.deploy(FreezingMessage)
        message1Index = freezingMessage.write("hogehoge", 2).return_value
        assert FreezingMessage[0].messages(message1Index)[1] == "hogehoge"
        assert FreezingMessage[0].messages(message1Index)[3] == 2
        
        message2Index = freezingMessage.write("fugafuga", 4).return_value
        assert FreezingMessage[0].messages(message2Index)[1] == "fugafuga"
        assert FreezingMessage[0].messages(message2Index)[3] == 4

        assert FreezingMessage[0].messages(message1Index)[1] == "hogehoge"
        assert FreezingMessage[0].messages(message1Index)[3] == 2

        freezingMessage.edit(message1Index, "hogehoge edited")
        assert FreezingMessage[0].messages(message1Index)[1] == "hogehoge edited"
        assert FreezingMessage[0].messages(message1Index)[3] == 2

        with reverts(revert_msg="frozen"):
            freezingMessage.edit(message1Index, "hogehoge edited twice")
        
        
