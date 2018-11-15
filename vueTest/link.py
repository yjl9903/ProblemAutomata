#coding=utf-8

import tornado.ioloop
from tornado import websocket

class myWebsocket(websocket.WebSocketHandler):
    def open(self):
        print("WebSocket Opened")
    
    def on_message(self, message):
        self.write_message("I have received your msg " + message)
        print(message)

    def on_close(self):
        print("WebSocket Closed")

    def check_origin(self, origin):
        return True
        

app = tornado.web.Application([(r"/", myWebsocket),])

app.listen(3001)
tornado.ioloop.IOLoop.instance().start()