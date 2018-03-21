# -*- coding: utf-8 -*-
# @Author: Pop Alexandru
# @Date:   2018-03-19 12:04:29
# @Last Modified by:   Pop Alexandru
# @Last Modified time: 2018-03-20 17:02:11

import socket
import threading
from client import Client, Connection
class Server:
	#AF_INET = IPv4 and IPv6
	#SOCK_STREAM = TCP connections for UPD connections use SOCK_DGRAM
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	def __init__(self):
		self.sock.bind(('localhost', 10000))
		self.sock.listen(1)


	def run(self):
		print("Server up and Running")
		while True:
			c, a = self.sock.accept();
			print(c, a )
			print('run')
			connection = Connection()
			connection.addClient(c, a)



server = Server();
server.run()
