#!/usr/bin/env python3

"""Mohammed Abu Mustafa, 04/02/2023"""


import platform   
import subprocess
import netifaces
from os import system, name
from time import sleep


"""
param host is used to represnt the IP address or domain name.
A function that tests if the parameter host is pinged successfully is so; it prints to inform the sys admin that the ping was successful and failed if otherwise
for both windows and linux.
"""
def ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', param, '1', host]
    if subprocess.call(command) == 0:
    	clear()
    	print("please inform your system administator that the ping was SUCCESFUL!")
    else:
    	print("please inform your system administator that the ping has FAILED!")

"""
A function that clears the terminal for both windows and linux.
"""
def clear():
	#windows
    if name == 'nt':
        _ = system('cls')
	#linux
    else:
        _ = system('clear')

"""
Main function that works as an end user interface, it will set a title and add a list of options as an an input to pick from,
depending on the input it will either test the connectivity to the gateway, a remote IP address, a URL to validate that DNS resolution, or display your gateway IP address, and if there is an invlaid input it will print a error message, and tell you to select a number from 1-4 again.
This will run infinitly until "Q/q" is entered, quiting the program.
"""
def main():
	run=True
	while run==True:
		clear()
		title="Ping Test Troubleshooter"
		print("\n",title.center(100))
		val=input("Enter selection:\n\n\t1 - Test connectivity to your gateway.\n\t2 - Test for remote connectivity.\n\t3 - Test for DNS resolution.\n\t4 - Display gateway IP Address.\n\nPlease enter a number(1-4) or \"Q/q\" to quit to program.")

		if val=="1":
			clear()
			print("Testing Connectivity to your gateway...")
			sleep(2)
			gateways = netifaces.gateways()
			default_gateway = gateways['default'][netifaces.AF_INET][0]
			ping(default_gateway)
			sleep(2)
			clear()
		elif val=="2":
			clear()
			print("Testing for remote connectivity... trying IP address 8.8.8.8.")
			sleep(2)
			ping("8.8.8.8")
			sleep(2)
			clear()
		elif val=="3":
			clear()
			print("Resolving DNS: trying URL... www.google.com.")
			sleep(2)
			ping("google.com")
			sleep(2)
			clear()
		elif val=="4":
			clear()
			print("your gateway IP address is", default_gateway)
			sleep(2)
			clear()
		elif val=="q" or val=="Q":
			clear()
			print("Quiting program: returning to shell.\n\nHave a wonderfull day!")
			sleep(2)
			run=False
			clear()
		else:
			print("\n\nyou entered an invalid option\n\nPlease select a number between1 through 4.")
			sleep(2)
			clear()




main()
