import telnetlib
import time

def telnet_gns3(ip,router,val):
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
 ## cmd_file = raw_input('Enter command file name and extension: ')
    
    
    vals = str(val)
    inputs = "R"+vals+"cmds.txt"
    cmd_file = inputs
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
    time.sleep(70)
    #########################Write Output to each file for multiple routers###########################
    if router == 1:
        time.sleep(wait)
        output = connection.read_very_eager()
        R1 = open("R1","w")
        R1.write(output)
        R1.close
    elif router == 2:
        time.sleep(wait)
        output = connection.read_very_eager()
        R2 = open("R2","w")
        R2.write(output)
        R2.close
    elif router == 3:
        time.sleep(wait)
        output = connection.read_very_eager()
        R3 = open("R3","w")
        R3.write(output)
        R3.close
    elif router == 4:
        time.sleep(wait)
        output = connection.read_very_eager()
        R4 = open("R4","w")
        R4.write(output)
        R4.close
    elif router == 5:
        time.sleep(wait)
        output = connection.read_very_eager()
        R5 = open("R5","w")
        R5.write(output)
        R5.close
        
    connection.close()
    

#call gns3
val = 0
for router in range(1,6):
    if router == 1:
        ip = "192.168.1.101"
    elif router == 2:
        ip = "192.168.1.102"
    elif router == 3:
        ip = "192.168.1.103"
    elif router == 4:
        ip = "192.168.1.104"
    elif router == 5:
        ip = "192.168.1.105"
    val += 1
    telnet_gns3(ip,router,val)
"""
RN = []

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

##terminal length 0 ##Command to show all values in show running-config