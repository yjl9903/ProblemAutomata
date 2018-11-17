#coding=utf-8

import os
import json
import time
import timelimit

def parseOutput(s):
    cp = []
    for x in s:
        if x != "":
            cp.append(x.rstrip())
    return cp

class Judger(object):

    cmd = "g++"
    src = ""
    file = "a.exe"
    maxTime = 0.0

    def __init__(self, cfg, src, binary = "std.exe", maxTime = 1000):
        self.config = cfg
        self.src = src
        self.file = binary
        self.maxTime = maxTime / 1000.0
        
        args = cfg['args']
        self.cmd += " -std=" + args['std']
        for key in args['macro']:
            self.cmd += " -D" + key
        for key in args['args']:
            self.cmd += " " + key
        # print(self.cmd)

    def compile(self):
        cmd = self.cmd + " " + self.src + " -o " + self.file
        out = os.popen(cmd).read()

    def getOutput(self):
        self.compile()
        testcase = self.config['testcase']
        path = testcase['path']
        insuf = '.' + testcase['input-suffix']
        outsuf = '.' + testcase['output-suffix']

        for i in range(testcase['num']):
            output, usedTime = self.running(path + str(i) + insuf)
            if isinstance(usedTime, str):
                raise Exception("Time Limit Excceed")
            output = parseOutput(output.split('\n'))
            # print output
            with open(path + str(i) + outsuf, 'w') as f:
                f.write('\n'.join(output))

    def check(self, output, res):
        if res == "":
            return True
        output = parseOutput(output.split('\n'))

        with open(res, "r") as f:
            ans = map(lambda x : x.rstrip(), f.readlines())

        if ans != output:
            return "Wrong Answer"
        return True

    def running(self, input):
        output = [""]
        @timelimit.setTimeLimit(self.maxTime)
        def f(file):
            output[0] = os.popen(self.file + ' <' + input).read()
            # print output
        usedTime = f(self.file)
        return output[0], usedTime

    def run(self, input, res):
        output, usedTime = self.running(input)
        if isinstance(usedTime, str):
            return usedTime
        return self.check(output, res)

    def test(self):
        self.compile()
        testcase = self.config['testcase']
        path = testcase['path']
        insuf = '.' + testcase['input-suffix']
        outsuf = '.' + testcase['output-suffix']
        # print num
        for i in range(testcase['num']):
            res = self.run(path + str(i) + insuf, path + str(i) + outsuf)
            if isinstance(res, str):
                return res
        return "Accepted"

data = {}
with open("settings.json", "r") as f:
    data = json.loads(f.read())

jd = Judger(data, "a.cpp", maxTime = 1000)
# print jd.run()
# jd.getOutput()
print jd.test()
