# import everything and define a test runner function
from importlib import reload
from helper import run
import ecc
import helper

from ecc import FieldElement
reload(ecc)
run(ecc.FieldElementTest("test_ne"))