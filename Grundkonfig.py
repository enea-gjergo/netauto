#!/usr/bin/env python

cmdEthernet=("interface GigabitEthernet0/{}")
cmdAddress=("ip address {}")
cmdMask=("  {}")

commandList=[]
interfaceList =[0,1]
addressList =["192.168.10.1" , "192.168.11.1"]
maskList = ["255.255.255.0","255.255.255.0"]

commandList.append("enable")
commandList.append("configure terminal")

for i,interface in enumerate(interfaceList):
        commandList.append(cmdEthernet.format(interface))
        address= addressList[i]
        mask= maskList[i]
        ipadd=cmdAddress.format(address)+cmdMask.format(mask)
        commandList.append((ipadd))
        commandList.append("exit")
        print(commandList)
