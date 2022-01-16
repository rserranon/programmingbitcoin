from helper import merkle_parent
hex_hashes = [
    'c117ea8ec828342f4dfb0ad6bd140e03a50720ece40169ee38bdc15d9eb64cf5',
    'c131474164b412e3406696da1ee20ab0fc9bf41c8f05fa8ceea7a08d672d7cc5',
    'f391da6ecfeed1814efae39e7fcb3838ae0b02c02ae7d0a5848a66947c0727b0',
    '3d238a92a94532b946c90e19c49351c763696cff3db400485b813aecb8a13181',
    '10092f2633be5f3ce349bf9ddbde36caa3dd10dfa0ec8106bce23acbff637dae',
]
hashes = [bytes.fromhex(x) for x in hex_hashes]
if len(hashes) % 2 == 1:
    hashes.append(hashes[-1])
parent_level = []
for i in range(0, len(hashes), 2):
    parent = merkle_parent(hashes[i], hashes[i+1])
    parent_level.append(parent)
for item in parent_level:
    print(item.hex())

from importlib import reload
from helper import run
import merkleblock 
    
reload(merkleblock)
run(merkleblock.MerkleBlockTest("test_parse"))