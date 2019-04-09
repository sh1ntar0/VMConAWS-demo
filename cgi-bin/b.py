#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
host = socket.gethostname()
ip = socket.gethostbyname(host)

print ("Content-type: text/html")
print ("<html>")
print (ip)
print ("</html>")
