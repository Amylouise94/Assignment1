import socket, os, platform

print(platform.system(), end = " ")
print(platform.release())
print(os.name)
print(socket.gethostname())
