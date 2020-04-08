from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json
clients = []


class SimpleEcho(WebSocket):

    def handleMessage(self):
        message = json.loads(self.data)
        if message["type"] == "login":
            text_to_send = f"conn {message['text']}"
        else:
            text_to_send = f"{message['nickName']}:{message['text']}"

        for client in clients:
            if client != self:
                client.sendMessage(text_to_send)
                print("msg Recived :", self.address)

    def handleConnected(self):
        print(self.address, 'connected')
        clients.append(self)

    def handleClose(self):
        print(self.address, 'closed')
        clients.remove()


server = SimpleWebSocketServer('', 8000, SimpleEcho)
print("Server is running on 8000")
server.serveforever()
