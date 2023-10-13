import pytest
import os
import re
import platform

pwd = os.getcwd()
if platform.system() == "Windows" or platform.system() == "Darwin":
    RIPES_PATH = f"{pwd}/Ripes/Ripes.exe"
if platform.system() == "Linux":
    RIPES_PATH = f"{pwd}.AppImage"


ØVING_2_PATH = "Øvinger/2.s"
ØVING_3_PATH = "Øvinger/3.s"
ØVING_4_PATH = "Øvinger/4.s"
RIPES_ARGUMENTS = "--mode cli -t asm --proc RV32_5S --isaexts M --regs"


def test_ripes_setup_correctly():
    stream = os.popen(f"{RIPES_PATH} {RIPES_ARGUMENTS} --runinfo --src test.s")
    o = stream.read()

    x0_register = int(re.findall(r"x0:\t([-|\d]*)\t", o)[0])
    assert x0_register == 0


def test_oving2():
    extra_arguments = f"--src {ØVING_2_PATH}"

    default_registers = [
        "--reginit 2=0x7ffffff0,3=10000000,10=2,11=2,12=4,13=5,14=8,15=9",
        "--reginit 2=0x7ffffff0,3=10000000,10=-5,11=0,12=1,13=41,14=100,15=-64",
        "--reginit 2=0x7ffffff0,3=10000000,10=10,11=-110,12=-2,13=-2,14=-7,15=5",
    ]
    output = []
    for i, register in enumerate(default_registers):
        stream = os.popen(
            f"{RIPES_PATH} {RIPES_ARGUMENTS} {extra_arguments} {register}"
        )
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
    init_registers_cmd = "--reginit"

    # Sender inn default register; a0=9, a0=39, a0=2401 og a0=2
    default_registers = ["10=9", "10=39", "10=2401", "10=2"]
    output = []
    for i, register in enumerate(default_registers):
        stream = os.popen(
            f"{RIPES_PATH} {RIPES_ARGUMENTS} {extra_arguments} {init_registers_cmd} {register}"
        )
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


def test_oving4():
    extra_arguments = f"--src {ØVING_4_PATH}"
    init_registers_cmd = "--reginit"

    # Sender inn default register for alle øvinger;
    default_registers = [
        "10=6,11=5,12=4,13=3,14=2,15=1",
        "10=1,11=2,12=3,13=4,14=5,15=6",
        "10=50,11=390,12=14,13=21,14=-20,15=2000",
        "10=0,11=2,12=16,13=64,14=16,15=2",
        "10=0,11=0,12=0,13=0,14=0,15=0",
    ]
    output = []
    for i, register in enumerate(default_registers):
        stream = os.popen(
            f"{RIPES_PATH} {RIPES_ARGUMENTS} {extra_arguments} {init_registers_cmd} {register}"
        )
        o = stream.read()

        # Regex to fetch a0, a1, a2, a3, a4, a5 register value
        a0_register = int(re.findall(r"x10:\t([-|\d]*)\t", o)[0])
        a1_register = int(re.findall(r"x11:\t([-|\d]*)\t", o)[0])
        a2_register = int(re.findall(r"x12:\t([-|\d]*)\t", o)[0])
        a3_register = int(re.findall(r"x13:\t([-|\d]*)\t", o)[0])
        a4_register = int(re.findall(r"x14:\t([-|\d]*)\t", o)[0])
        a5_register = int(re.findall(r"x15:\t([-|\d]*)\t", o)[0])
        output.append(
            [
                a0_register,
                a1_register,
                a2_register,
                a3_register,
                a4_register,
                a5_register,
            ]
        )

    expected_results = [
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [-20, 14, 21, 50, 390, 2000],
        [0, 2, 2, 16, 16, 64],
        [0, 0, 0, 0, 0, 0],
    ]
    for i in range(len(expected_results)):
        for j in range(len(expected_results[i])):
            assert output[i][j] == expected_results[i][j]
