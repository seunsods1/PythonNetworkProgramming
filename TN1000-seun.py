import telnetlib
import time

def telnet_gns3(ip,router):
    wait = 4
    #------------------Sign In----------------------------

    connection = telnetlib.Telnet(ip, 23, 5)
    connection.read_until("Password:", 5)
    connection.write('cisco' + "\n")
    connection.write('enable' + "\n")
    connection.read_until("Password:", 5)
    connection.write('cisco' + "\n")
    #####################################################
    
    ##################Command loop##########################
    cmd_file = raw_input('Enter command file name and extension: ')
    """
    vals = str(val)
    inputs = "R"+vals+"cmds.txt"
    cmd_file = inputs
    """
    selected_cmd_file = open(cmd_file, 'r')
    selected_cmd_file.seek(0)
    for each_line in selected_cmd_file.readlines():
        time.sleep(wait)
        connection.write(each_line)
        connection.write("\n")

    ############################################################
    """
    connection.write('show run' + "\n")
    time.sleep(50)
    """
   
    connection.write('show ip int brief' + "\n")
    time.sleep(50)
    #########################Write Output to each file for multiple routers###########################
    
    time.sleep(wait)
    output = connection.read_very_eager()
    Rtemp = open("RN" + str(router),"w")
    Rtemp.write(output)
    Rtemp.close
    connection.close()

#call gns3

"""
ip = "192.168.1.101"
n = 3

for router in range(1,n):
    telnet_gns3(ip,router)
    print(router, ip)
    quad = ip[len(ip)-3:len(ip)]
    quad_int = int(quad)
    quad_int += 1
    quads = str(quad_int)
    temp_ip = ip[:len(ip)-3]
    ip = temp_ip + quads
"""

ip = "192.168.1.99"
p3 = ip.rfind(".")
temp_s = ip[:p3+1]
quad = ip[p3+1:]
quad_int = int(quad)

n = 3
for router in range(1,n):
    telnet_gns3(ip, router)
    print(router,ip)
    quad_int += 1
    quads = str(quad_int)
    ip = temp_s + quads
    

##terminal length 0 ##Command to show all values in show running-config