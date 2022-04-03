import pytest
from brownie import web3
from web3.middleware import geth_poa_middleware

web3.middleware_onion.inject(geth_poa_middleware, layer=0)


@pytest.fixture()
def users(web3, accounts):
    admin = accounts[0]
    trader = accounts[1]
    issuer = accounts[2]
    agent = accounts[3]
    user1 = accounts[4]
    user2 = accounts[5]
    users = {
        "admin": admin,
        "trader": trader,
        "issuer": issuer,
        "agent": agent,
        "user1": user1,
        "user2": user2
    }

    yield users
