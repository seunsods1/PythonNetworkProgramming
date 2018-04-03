
import telnetlib
import time

def telnet_gns3(ip):
    wait = 2   
    # -----------Sign in--------------------------
    connection = telnetlib.Telnet(ip, 23, 5)        
    connection.read_until("Password:", 5)
    connection.write('cisco' + "\n")
    connection.write('enable' + "\n")
    connection.read_until("Password:", 5)
    connection.write('cisco' + "\n")
    # -----------Sign in--------------------------


    # -----------Command loop--------------------------
    cmd_file = raw_input('Enter command file name and extension: ') 
    selected_cmd_file = open(cmd_file, 'r')
    selected_cmd_file.seek(0)
    for each_line in selected_cmd_file.readlines():
        time.sleep(wait)
        connection.write(each_line)
        connection.write("\n")
    # -----------Command loop--------------------------

    connection.write('show run' + "\n")
    time.sleep(15)

    # -------Write output to a file-------------------
    time.sleep(wait)
    output = connection.read_very_eager()
    R2 = open("R2", "w")
    R2.write(output)
    R2.close
    # -------Write output to a file-------------------
    print output
    
        
    

    connection.close()
        

#Call gns3
telnet_gns3('192.168.1.101')