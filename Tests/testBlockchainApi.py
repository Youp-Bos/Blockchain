import unittest
import time
from Blockchain import Blockchain

class MyTestCase(unittest.TestCase):
    def testBlocks(client, app):
        assert client.get('/get_chain').status.code == 200


if __name__ == '__main__':
    unittest.main()

def test_block():
    block = Blockchain(1, [], 0, 1662843237.224394, 0)
    assert block.index == 1
    assert len(block.txs) == 0
    assert block.timestamp == 1662843237.224394
    assert block.previous_hash == 0
    assert block.nonce == 0

def test_create_hash():
    block = Blockchain(1, [], 0, 1662843237.224394, 0)
    assert block.create_hash() == '05f9ab9b43182f6f42a4c6898c5c76feaf221cafcc67c03eda01fecef33dd4c2'


def test_mine_async():
    block = Blockchain(1, [], 0, 1662843237.000001, 0)
    blockchain = Blockchain()
    nonce, hash = blockchain.mine(block)

    assert nonce > 0
    assert hash.startswith('0' * Blockchain.difficulty)


def test_add_block():
    blockchain = Blockchain()
    first_block = blockchain.create_first_block()

    assert len(first_block.hash) > 0
    assert first_block.index == 0
    assert len(blockchain.chain) == 1

    block = Blockchain(len(blockchain.chain) + 1, [], blockchain.last_block.hash, 1662843238.000002, 0)
    block.nonce, proof = blockchain.mine(block)

    blockchain.add_block(block, proof)

    assert len(blockchain.chain) == 2


def test_validate_chain():
    blockchain = Blockchain()
    blockchain.create_first_block()

    block = Blockchain(len(blockchain.chain) + 1, [], blockchain.last_block.hash, 1662843238.000002, 0)
    block.nonce, proof = blockchain.mine(block)
    blockchain.add_block(block, proof)

    block = Blockchain(len(blockchain.chain) + 1, [], blockchain.last_block.hash, 1662843238.000003, 0)
    block.nonce, proof = blockchain.mine(block)
    blockchain.add_block(block, proof)

    assert blockchain.validate_chain()

    block = Blockchain(len(blockchain.chain) + 1, [], blockchain.chain[1].hash, 1662843239.000004, 0)
    block.nonce, proof = blockchain.mine(block)
    blockchain.add_block(block, proof)

    assert blockchain.validate_chain()