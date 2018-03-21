# -*- coding: utf-8 -*-
# @Author: Pop Alexandru
# @Date:   2018-03-20 16:50:10
# @Last Modified by:   Pop Alexandru
# @Last Modified time: 2018-03-20 17:02:22

import socket
import threading
import sys
# from server import connections

class Connection:
	connections = [];
	def setConnections(self, client_connection):
		self.connections.append(client_connection)
	def handler(self, client_connection, client_address):
		print('in connection handler')
		while True:
			data = client_connection.recv(1024)
			for connection in self.connections:
				if client_connection != connection:
					connection.send(data)
					print(data)
			if not data:						
				print(srt(client_address[0]) + ":" + str(client_address[1]), "disconected")
				self.connections.remove(client_connection)
				client_connection.close()
				break