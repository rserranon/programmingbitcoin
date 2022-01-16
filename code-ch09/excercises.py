
from io import BytesIO
from unittest import TestCase


# import everything and define a test runner function
from importlib import reload
from helper import run
import block
import ecc
import helper
import script
import tx

# Run tests that are not running on Jupyter Notebook

# Exercise 9
reload(block)
run(block.BlockTest("test_target"))

# Exercise 10
reload(block)
run(block.BlockTest("test_difficulty"))


# Exercise 11
reload(block)
run(block.BlockTest("test_check_pow"))

from block import Block
from helper import TWO_WEEKS
last_block = Block.parse(BytesIO(bytes.fromhex('00000020fdf740b0e49cf75bb3d5168fb3586f7613dcc5cd89675b0100000000000000002e37b144c0baced07eb7e7b64da916cd3121f2427005551aeb0ec6a6402ac7d7f0e4235954d801187f5da9f5')))
first_block = Block.parse(BytesIO(bytes.fromhex('000000201ecd89664fd205a37566e694269ed76e425803003628ab010000000000000000bfcade29d080d9aae8fd461254b041805ae442749f2a40100440fc0e3d5868e55019345954d80118a1721b2e')))
time_differential = last_block.timestamp - first_block.timestamp
if time_differential > TWO_WEEKS * 4:
    time_differential = TWO_WEEKS * 4
if time_differential < TWO_WEEKS // 4:
    time_differential = TWO_WEEKS // 4
new_target = last_block.target() * time_differential // TWO_WEEKS
print('{:x}'.format(new_target).zfill(64))

# Exercise 12

from io import BytesIO
from block import Block
from helper import TWO_WEEKS
from helper import target_to_bits

block1_hex = '000000203471101bbda3fe307664b3283a9ef0e97d9a38a7eacd8800000000000000000010c8aba8479bbaa5e0848152fd3c2289ca50e1c3e58c9a4faaafbdf5803c5448ddb845597e8b0118e43a81d3'
block2_hex = '02000020f1472d9db4b563c35f97c428ac903f23b7fc055d1cfc26000000000000000000b3f449fcbe1bc4cfbcb8283a0d2c037f961a3fdf2b8bedc144973735eea707e1264258597e8b0118e5f00474'

# parse both blocks
block1 = Block.parse(BytesIO(bytes.fromhex(block1_hex)))
block2 = Block.parse(BytesIO(bytes.fromhex(block2_hex)))
# get the time differential
time_differential = block2.timestamp - block1.timestamp
# if the differential > 8 weeks, set to 8 weeks
if time_differential > TWO_WEEKS * 4:
    time_differential = TWO_WEEKS * 4
# if the differential < 1/2 week, set to 1/2 week
if time_differential < TWO_WEEKS // 4:
    time_differential = TWO_WEEKS // 4
# new target is last target * differential / 2 weeks
new_target = block2.target() * time_differential // TWO_WEEKS
# convert new target to bits
new_bits = target_to_bits(new_target)
# print the new bits hex
print(new_bits.hex())

# Exercise 13

reload(helper)
run(helper.HelperTest("test_calculate_new_bits"))

from BlockFile import BlockFile
from tx import Tx
import os

cur_path = os.path.dirname(__file__)

with open(cur_path + '/' + 'blk00001.dat', "rb") as blockStream:
    blk_obj = BlockFile.parse (blockStream) # parse function works with fileStreams
    print('block_size: {}'.format(blk_obj.block_size))
    print('tx_count: {}'.format(blk_obj.tx_count))
    print(blk_obj.block_header.hash().hex())
    print('000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')

    for tx in range (1, blk_obj.tx_count + 1):
        tx_obj = Tx.parse(blockStream)
        if not tx_obj.is_coinbase():
             if tx_obj.verify():  # verify transaction if it's not a coinbase Tx
                 print('Transaction: {} verified!'.format(tx_obj.hash().hex()))
        print(repr(tx_obj))

# Create parser for coinbase transaction
# Create a test to validate number of transactions = 1 on genesis block
# Create a test to validate hash() equal to the genesis block hash
# 000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
