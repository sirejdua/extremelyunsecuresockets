#!/usr/bin/env python3

import sys
import socket
import selectors
import types

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Choose a port here
port = 42525

lsock.bind(('',port))
lsock.listen(10)
print("listening on", port)

command_list = []

## Populate your command list with a list of strings (each string is 1 command)

i = 0
done = False
try:
	while not done:
		rsock, address = lsock.accept()
		print("connected to {}".format(address))
		if (i < len(command_list)):
			msg = command_list[i]
			i += 1
		else:
			msg = "terminating connection\n"
			print("Done")
			done = True
		rsock.sendall(msg.encode("utf-8"))
		rsock.close()
except KeyboardInterrupt:
	print("Exitting")
	lsock.close()
