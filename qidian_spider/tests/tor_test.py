import socket
import socks
import requests
import os

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket
print(requests.get('http://api.ipify.org?format=json').text)

os.system("""(echo authenticate '"mypassword"'; echo signal newnym; echo \
    quit) | nc localhost 9051""")

