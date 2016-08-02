#!/usr/bin/env python
# Akshay Singh
# Program to calculate the broadcast address, network address and number of hosts.


import ipaddress

def subnet_calc():
    
    try:
        while True:
        
            print("Welcome to the Subnet Calculator \n")
            ip_input = raw_input("Enter an ip address: " )
            ip_u = unicode(ip_input, "utf-8")
            ip_split = ip_input.split('.')
            check_ip = ipaddress.ip_address(ip_u)
        
            if(1 <= int(ip_split[0]) < 233) and (int(ip_split[0]) != (169 or 127)):
                break
            else:
                print "Ip is Invalid \n"
                continue
                
        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]
        while True:
            
            subnet_input = raw_input("Enter a subnet mask: ")
            subnet_split = subnet_input.split('.')
            #print "debug 1"
            if ((len(subnet_split) == 4)
            and (int(subnet_split[0]) == 255)
            and (int(subnet_split[1]) in masks) and (int(subnet_split[2]) in masks)
            and (int(subnet_split[3]) in masks)
            and (int(subnet_split[0]) >= int(subnet_split[1]) >= int(subnet_split[2]) >= int(subnet_split[3]))):
                #print "debug 2"
                break
            else:
                
                #print "debug 3"
                print "\nThe subnet mask is Invalid!\n"
                continue
            
            #print "debug 4"

        subnet_list = []
        for i in range(0, len(subnet_split)):
            subnet_bin = bin(int(subnet_split[i])).split("b")[1]
            
            if(len(subnet_bin) == 8):
                subnet_list.append(subnet_bin)
                
            elif(len(subnet_bin) < 8):
                temp = subnet_bin.zfill(8)
                subnet_list.append(temp)
                
        #print subnet_list
        subnet_new_list = "".join(subnet_list)
        #print subnet_new_list
                
        no_of_zeros = subnet_new_list.count("0")
        #print no_of_zeros
        no_of_ones = subnet_new_list.count("1")
        #print no_of_ones
        no_of_subnets = abs(2 ** no_of_ones - 2) # Number of Subnets
        #print no_of_subnets
        no_of_hosts = abs(2 ** no_of_zeros - 2) # Number of hosts
        #print no_of_hosts
    
        ip_list = []
        
        ip_new_split = ip_input.split('.')
        #print ip_new_split
        
        for j in range(0, len(ip_new_split)):
            ip_bin = bin(int(ip_new_split[j])).split("b")[1]
            #print ip_bin
            if(len(ip_bin) < 8):
                new_temp = ip_bin.zfill(8)
                ip_list.append(new_temp)
            else:
                ip_list.append(ip_bin)
                
        #print ip_list
        ip_join_list = "".join(ip_list)
        #print ip_join_list
        #print subnet_new_list
        """ Network Address"""
    
        network_address_bin = bin(int(str(ip_join_list),2) & int(str(subnet_new_list),2)).split('0b')[1]
        #print network_address_bin
        network_list_bin = []
        
        for z in range(0,len(network_address_bin), 8):
            temp = network_address_bin[z:z+8]
            network_list_bin.append(temp)
        #print network_list
        #print network_list[0]
        network_list_dec = []
        
        for k in range(0,len(network_list_bin)):
            network_list_dec.append(str(int(network_list_bin[k],2)))
        #print network_list_dec
        network_address = ".".join(network_list_dec)
        #print network_address
        """ Network Address End"""
        
        """ Broadcast Address """
        subnet_str = str(subnet_new_list)
        invert_subnet = subnet_str.replace('1','2').replace('0','1').replace('2','0')
        broadcast_address_bin = bin(int(str(ip_join_list),2) | int(invert_subnet,2)).split('0b')[1]
        #print broadcast_address_bin
        broadcast_list_bin = []
        
        for o in range(0,len(broadcast_address_bin), 8):
            temp = broadcast_address_bin[o:o+8]
            broadcast_list_bin.append(temp)
        #print broadcast_list_bin
        
        broadcast_list_dec = []
        for k in range(0,len(broadcast_list_bin)):
            broadcast_list_dec.append(str(int(broadcast_list_bin[k],2)))
        
        broadcast_address = ".".join(broadcast_list_dec)
        #print broadcast_address
        """ Broadcast Address End"""
        
        """ Printing the results """
        print "\n"
        print "Broadcast address is: ",broadcast_address
        print "Network address is: ",network_address
        print "Number of possible hosts per subnet: ",no_of_hosts
        print "\n"
        """ Printing End """
        
    except KeyboardInterrupt:
        print'\n'
        print "Program aborted! \n"
    except:
        print"\n"
        print "Please check your value \n"
    
subnet_calc()
    

