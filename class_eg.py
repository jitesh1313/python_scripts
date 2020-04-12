#!/usr/bin/python
class server(object):
    def _init_(self,ip,hostname):
        self.ip = ip
        self.hostname = hostname
    def set_ip(self,ip):
        self.ip = ip
    def set_hostname(self,hostname):
        self.hostname = hostname
    def ping(self,ip_addr):
        print "pinging %s from %s (%s)" % (ip_addr, self.ip, self.hostname)
if _name_ == '_main_':
    server = server('192.168.1.0', 'bumbly')
    server.ping('192.168.1.15')
