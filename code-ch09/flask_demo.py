from flask import Flask
from block import Block
import os

app = Flask(__name__)

cur_path = os.path.dirname(__file__)



@app.route("/Block")
def hello_world():
    with open(cur_path + '/' + 'blk00000.dat', "rb") as blockStream:
        blk_obj = Block.parse(blockStream) # parse function works with fileStreams
        print('ok')

    return {
        "version":      blk_obj.version,
        "prev_block":   blk_obj.prev_block.hex(),
        "timestamp":    blk_obj.timestamp,
        "version":      blk_obj.merkle_root.hex(),
        "bits":         blk_obj.bits.hex(),
        "nonce":        blk_obj.nonce.hex(),
        "hash":         blk_obj.hash().hex()
    }
  
  #000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
  #a0a875529800e90bd4b2145ad65f95a455152deee6456e1239696e2f9750cab8