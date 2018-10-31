import socket
import paho.mqtt.publish as pub

hostMACAddress = 'B8:27:EB:BC:52:83'  # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 30 # 3 is an arbitrary choice. However, it must match the port used by the client.
backlog = 1
size = 1024
s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
s.bind((hostMACAddress,port))
s.listen(backlog)
try:
    client, address = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            data1 = str(data)
            pub.single("miladkhademinori", data1, hostname="172.21.216.242")
            print(data)
            #client.send(data)
except:	
    print("Closing socket")	
    client.close()
    s.close()
