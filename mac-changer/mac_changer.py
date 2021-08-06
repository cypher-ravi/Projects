#!/usr/bin/env python

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify a interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please enter a new_mac,use --help for more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):

    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(b"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC =" + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)

if options.new_mac == options.new_mac:
    print("mac changed successfully and your new mac is:" ,current_mac)
else:
    print("mac address did not changed successfully")



