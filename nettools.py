#!/usr/bin/python3
import os
#############
# Simple Functions for Network Administration
#############


# 1.) get hostname by ip:
#requires sshpass on remote hosts
def gethost(ip,user,passwd):
    '''gethost - returns hostname for a given ip address'''
    resolved_hostname = os.popen(f'sshpass -p {passwd} ssh -q {user}@{ip} hostname')
    hostname = resolved_hostname.read()
    return hostname
