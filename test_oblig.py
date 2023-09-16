import pytest
import os
import re

RIPES_PATH = r"C:/Users/smk1/Documents/NTNU/TDT4160/Ripes-v2.2.6-win-x86_64/Ripes.exe"
RIPES_ARGUMENTS = "--mode cli -t asm --proc RV32_5S --isaexts M --regs"  


def test_oving2():
    extra_arguments = "--src Øving2/2.s"

    default_registers = ["--reginit 2=0x7ffffff0,3=10000000,10=2,11=2,12=4,13=5,14=8,15=9", "--reginit 2=0x7ffffff0,3=10000000,10=-5,11=0,12=1,13=41,14=100,15=-64", "--reginit 2=0x7ffffff0,3=10000000,10=10,11=-110,12=-2,13=-2,14=-7,15=5"]
    output = []
    for i, register in enumerate(default_registers):
        stream = os.popen(f"{RIPES_PATH} {RIPES_ARGUMENTS} {extra_arguments} {register}")
        o = stream.read()

        print(o)

        a0_register = int(re.findall(r"x10:\t([-|\d]*)\t", o)[0])
        output.append(a0_register)

    assert output[0] == 17
    assert output[1] == 42
    assert output[2] == -2
