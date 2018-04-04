import telnetlib
import time

ip = "192.168.1.101"
n = 50

for router in range(1,n):
    print(router, ip)
    quad = ip[len(ip)-3:len(ip)]
    quad_int = int(quad)
    quad_int += 1
    quads = str(quad_int)
    temp_ip = ip[:len(ip)-3]
    ip = temp_ip + quads
