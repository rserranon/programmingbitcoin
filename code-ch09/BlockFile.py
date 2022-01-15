from io import BytesIO
from unittest import TestCase

from block import Block

from helper import (
    little_endian_to_int,
    read_varint
)
class BlockFile:

    def __init__(self, magic_bytes, block_size, block_header, tx_count):  
        self.magic_bytes    = magic_bytes
        self.block_size     = block_size
        self.block_header   = block_header
        self.tx_count       = tx_count
       
    @classmethod
    def parse(cls, s):
        magic_bytes = s.read(4)
        block_size = little_endian_to_int(s.read(4))
        block_header = Block.parse(s)
        tx_count = read_varint(s)

        return cls(magic_bytes, block_size, block_header, tx_count)