from sockets.python3.client import Client

client = Client()
response, addr = client.poll_server('Hi', server=('172.29.41.128', 6000))
print(response, addr) 