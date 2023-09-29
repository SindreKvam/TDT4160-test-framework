import pytest
import os
import re

RIPES_PATH = r"C:/Users/smk1/Documents/NTNU/TDT4160/Ripes-v2.2.6-win-x86_64/Ripes.exe"
ØVING_2_PATH = "Øving2/2.s"
ØVING_3_PATH = "Øving3/3.s"
RIPES_ARGUMENTS = "--mode cli -t asm --proc RV32_5S --isaexts M --regs"


def test_ripes_setup_correctly():
    stream = os.popen(f"{RIPES_PATH} {RIPES_ARGUMENTS} --runinfo --src test.s")
    o = stream.read()

    x0_register = int(re.findall(r"x0:\t([-|\d]*)\t", o)[0])
    assert x0_register == 0


def test_oving2():
    extra_arguments = f"--src {ØVING_2_PATH}"

    default_registers = ["--reginit 2=0x7ffffff0,3=10000000,10=2,11=2,12=4,13=5,14=8,15=9", "--reginit 2=0x7ffffff0,3=10000000,10=-5,11=0,12=1,13=41,14=100,15=-64", "--reginit 2=0x7ffffff0,3=10000000,10=10,11=-110,12=-2,13=-2,14=-7,15=5"]
    output = []
    for i, register in enumerate(default_registers):
        stream = os.popen(f"{RIPES_PATH} {RIPES_ARGUMENTS} {extra_arguments} {register}")
        o = stream.read()

        print(o)

        # Regex to fetch a0 register value
        a0_register = int(re.findall(r"x10:\t([-|\d]*)\t", o)[0])
        output.append(a0_register)

    assert output[0] == 17
    assert output[1] == 42
    assert output[2] == -2


def test_oving3():
    extra_arguments = f"--src {ØVING_3_PATH}"
    init_registers_cmd  = "--reginit"

    # Sender inn default register; a0=9, a0=39, a0=2401 og a0=2
    default_registers = ["10=9", "10=39", "10=2401", "10=2"]
    output = []
    for i, register in enumerate(default_registers):
        stream = os.popen(f"{RIPES_PATH} {RIPES_ARGUMENTS} {extra_arguments} {init_registers_cmd} {register}")
        o = stream.read()

        print(o)

        # Regex to fetch a0 and a1 register value
        a0_register = int(re.findall(r"x10:\t([-|\d]*)\t", o)[0])
        a1_register = int(re.findall(r"x11:\t([-|\d]*)\t", o)[0])
        output.append([a0_register, a1_register])

    assert (output[0][0] == 3) and (output[0][1] == 1)
    assert (output[1][0] == 13) and (output[1][1] == 0)
    assert (output[2][0] == 343) and (output[2][1] == 1)
    assert (output[3][0] == 1) and (output[3][1] == 0)
    
