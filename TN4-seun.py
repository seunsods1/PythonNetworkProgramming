import telnetlib
import time

def telnet_gns3(ip):
    wait = 2
    #------------------Sign In----------------------------

    connection = telnetlib.Telnet(ip, 23, 5)
    connection.read_until("Password:", 5)
    connection.write('cisco' + "\n")
    connection.write('enable' + "\n")
    connection.read_until("Password:", 5)
    connection.write('cisco' + "\n")
    
    ##############Commands########################
    
    time.sleep(wait)
    connection.write("terminal length 0")
    connection.write("\n")
    
    time.sleep(wait)
    connection.write("configure terminal")
    connection.write("\n")
    
    time.sleep(wait)
    connection.write("int s0/0")
    connection.write("\n")
    
    time.sleep(wait)
    connection.write("ip address 6.5.5.5 255.0.0.0")
    connection.write("\n")
    
    time.sleep(wait)
    connection.write("end")
    connection.write("\n")

    time.sleep(wait)
    connection.write("show ip int brief")
    connection.write("\n")
    #######################################################
    
    #----------Write Output to file---------------
    time.sleep(wait)
    output = connection.read_very_eager()
    R2 = open("R2","w")
    R2.write(output)
    R2.close
    ##################################################
    print output

    connection.close()

#Call gns3
telnet_gns3('192.168.1.101')