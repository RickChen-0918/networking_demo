import sockets
from sockets.python3.server import Server

class MyServer(Server):
    def act_on(self, data, addr):
        print(data, addr)
        return data.decode()
        


server = MyServer(listening_address=("172.29.41.128", 6000))
server.listen()
