# import everything and define a test runner function
from importlib import reload
from helper import run
import ecc
import helper
import tx
import script

reload(tx)
run(tx.TxTest("test_sig_hash"))