from io import BytesIO
from ecc import S256Point, Signature
from helper import hash256, int_to_little_endian, encode_varint
from script import Script
from tx import Tx, TxIn, SIGHASH_ALL
hex_tx = '0100000001868278ed6ddfb6c1ed3ad5f8181eb0c7a385aa0836f01d5e4789e6\
bd304d87221a000000db00483045022100dc92655fe37036f47756db8102e0d7d5e28b3beb83a8\
fef4f5dc0559bddfb94e02205a36d4e4e6c7fcd16658c50783e00c341609977aed3ad00937bf4e\
e942a8993701483045022100da6bee3c93766232079a01639d07fa869598749729ae323eab8eef\
53577d611b02207bef15429dcadce2121ea07f233115c6f09034c0be68db99980b9a6c5e754022\
01475221022626e955ea6ea6d98850c994f9107b036b1334f18ca8830bfff1295d21cfdb702103\
b287eaf122eea69030a0e9feed096bed8045c8b98bec453e1ffac7fbdbd4bb7152aeffffffff04\
d3b11400000000001976a914904a49878c0adfc3aa05de7afad2cc15f483a56a88ac7f40090000\
0000001976a914418327e3f3dda4cf5b9089325a4b95abdfa0334088ac722c0c00000000001976\
a914ba35042cfe9fc66fd35ac2224eebdafd1028ad2788acdc4ace020000000017a91474d691da\
1574e6b3c192ecfb52cc8984ee7b6c568700000000'
hex_sec = '03b287eaf122eea69030a0e9feed096bed8045c8b98bec453e1ffac7fbdbd4b\
b71'
hex_der = '3045022100da6bee3c93766232079a01639d07fa869598749729ae323eab8ee\
f53577d611b02207bef15429dcadce2121ea07f233115c6f09034c0be68db99980b9a6c5e75402\
2'
hex_redeem_script = '475221022626e955ea6ea6d98850c994f9107b036b1334f18ca88\
30bfff1295d21cfdb702103b287eaf122eea69030a0e9feed096bed8045c8b98bec453e1ffac7f\
bdbd4bb7152ae'
sec = bytes.fromhex(hex_sec)
der = bytes.fromhex(hex_der)
redeem_script = Script.parse(BytesIO(bytes.fromhex(hex_redeem_script)))
stream = BytesIO(bytes.fromhex(hex_tx))
tx_obj = Tx.parse(stream)
s = int_to_little_endian(tx_obj.version, 4)
s += encode_varint(len(tx_obj.tx_ins))
i = tx_obj.tx_ins[0]
s += TxIn(i.prev_tx, i.prev_index, redeem_script, i.sequence).serialize()
s += encode_varint(len(tx_obj.tx_outs))
for tx_out in tx_obj.tx_outs:
    s += tx_out.serialize()
s += int_to_little_endian(tx_obj.locktime, 4)
s += int_to_little_endian(SIGHASH_ALL, 4)
z = int.from_bytes(hash256(s), 'big')
point = S256Point.parse(sec)
sig = Signature.parse(der)
print(point.verify(z, sig))
True