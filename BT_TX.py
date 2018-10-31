import socket
import numpy as np
import time

serverMACAddress = 'B8:27:EB:0e:a5:bb'
port = 30
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.connect((serverMACAddress,port))
while 1:
    data = str(np.random.randint(100))
    time.sleep(2)
    if data == "quit":
        break
    s.send(bytes(data, 'UTF-8'))
s.close()
