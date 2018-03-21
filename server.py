# -*- coding: utf-8 -*-
# @Author: Pop Alexandru
# @Date:   2018-03-19 12:04:29
# @Last Modified by:   Pop Alexandru
# @Last Modified time: 2018-03-20 17:02:11

import socket
import threading
from connections import Connection
class Server:
	#AF_INET = IPv4 and IPv6 
	#SOCK_STREAM = TCP connections for UPD connections use SOCK_DGRAM
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connections = []
	def __init__(self):
		self.sock.bind(('localhost', 10000))
		self.sock.listen(1)


	def run(self):

		while True:
			client_connection, client_address = self.sock.accept()
			handle_connection = Connection()
			clientThread = threading.Thread(handle_connection.handler(client_connection, client_address))
			clientThread.deamon = True
			clientThread.start()
			handle_connection.setConnection(client_connection)
			print(str(client_address[0]) + ":" + str(client_address[1]), "connected")

server = Server();
server.run()