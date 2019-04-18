#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket;
from datetime import datetime

ip = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]


print ("Content-type: text/html")
print
print ("<html>")
print ("<font size=\"7\">")
print (datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
print ("</br>")
print ("</br>")
print (ip)
print ("</font>")
print ("</html>")

