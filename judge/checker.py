#coding=utf-8

import sys
import os
import json
import judge

def checker(name, options, generator = "init.exe", dataPath = "..\\input\\", inputFile = "", outputFile = ""):
    outToFile = False
    inToScreen = True
    noprint = False
    if inputFile == "":
        inputFile = dataPath + name + ".in"

    for val in options:
        if val == "-noprint":
            noprint = True
        if val == "-out":
            outToFile = True
        if val == "-nin":
            inToScreen = False

    chk = judge.Judger(data, "", name + ".exe", 1000, True)

    if inToScreen:
        inp = os.popen(generator).read()
        with open(dataPath + name + ".in", 'w') as f:
            f.write(inp)

    output, usedTime = chk.running(inputFile)

    if noprint:
        return True

    if inToScreen:
        print("Input:\n" + inp.rstrip())
    if outToFile:
        with open(outputFile, 'w') as f:
            f.write(output)
    else:
        print("\nOutput:\n" + output.rstrip())

    return output

data = {}
with open(r"D:\5-Project\problemAutomata\settings.json", "r") as f:
    data = json.loads(f.read())


if len(sys.argv) == 1:
    print("checker *\n  use init.exe to generate testcase and get the result.\n")
    print("Options")
    print("  -out: out to file 'out.txt'.")
    print("  -nin: use 'in.txt' instead of init.exe.")
    exit()

checker(sys.argv[1], sys.argv[2:])
