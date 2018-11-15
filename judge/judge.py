#coding=utf-8

import os
import json
import time

class Complier(object):

    cmd = "g++"
    file = "a.exe"

    def __init__(self, binary):
        self.args = data['args']
        
        self.file = binary
        self.cmd += " -std=" + self.args['std']
        for key in self.args['macro']:
            self.cmd += " -D" + key
        for key in self.args['args']:
            self.cmd += " " + key
        # print(self.cmd)

    def complie(self, path):
        cmd = self.cmd + " " + path + " -o " + self.file
        # print(cmd)
        os.system(cmd)

    def run(self):
        start = time.time()
        
        run = os.popen(self.file)
        out = run.read()
        
        end = time.time()
        last = 1000 * (end - start)
        print("Exe Time: %d ms" % last)

        return last
       
data = {}
with open("settings.json", "r") as f:
    data = json.loads(f.read())

jd = Complier("std.exe")
jd.complie("a.cpp")
jd.run()
