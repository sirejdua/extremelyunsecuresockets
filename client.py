#!/usr/bin/env python3

import sys
import socket
import selectors
import types
import time
import os
import psutil

from server import port


# Put your hostname here
host = socket.gethostbyname("cedar.cs.berkeley.edu")

first = True
terminate = False
while (first or (not terminate)):
	cpu_usage = psutil.cpu_percent()
	if (cpu_usage > 20.0):
		time.sleep(10)
		continue
	first = False
	rsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	rsock.connect((host, port))
	message = rsock.recv(1024).decode("utf-8")
	if len(message) >= 2 and message[-2:] == "\\n":
		message = message[:-2]
	rsock.close()
	if (message == "terminating connection\n"):
		terminate = True
	else:
		print(message)
                
		exit_coded = os.system(message)

		if (exit_code != os.EX_OK):
			break
print("Disconnected")
