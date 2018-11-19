#coding=utf-8

import os
import sys
import json
import judge
import webbrowser
import tornado.ioloop
from tornado import websocket

basePath = "D:\\5-Project\\problemAutomata\\"

if len(sys.argv) == 1:
    exit()

name = sys.argv[1]
flag = True

for val in os.listdir(os.path.abspath('.')):
    if name == val:
        flag = False

if flag:
    os.mkdir(name)
    os.mkdir(name + '\\debug')
    os.mkdir(name + '\\input')
    with open(name + "\\std.cpp", "w") as f:
        f.write('')
    with open(name + "\\init.cpp", "w") as f:
        f.write('')
    with open(name + "\\description.md", "w") as f:
        f.write('')

class myWebsocket(websocket.WebSocketHandler):
    def open(self):
        print("WebSocket Opened")
        content = ""
        with open(name + "\\std.cpp", "r") as f:
            content = f.read()
        self.write_message(json.dumps({
            'type': "cpp",
            'content': content.strip()
        }))
    
    def on_message(self, message):
        # self.write_message("I have received your msg " + message)
        # print(message)
        content = ""
        with open(name + "\\std.cpp", "r") as f:
            content = f.read()
        self.write_message(json.dumps({
            'type': "cpp",
            'content': content.strip()
        }))

    def on_close(self):
        print("WebSocket Closed")

    def check_origin(self, origin):
        return True

app = tornado.web.Application([(r"/", myWebsocket),])

app.listen(3001)

webbrowser.open_new(basePath + "index.html")
os.system("code " + name)

tornado.ioloop.IOLoop.instance().start()