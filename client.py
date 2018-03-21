# -*- coding: utf-8 -*-
# @Author: Pop Alexandru
# @Date:   2018-03-19 11:37:22
# @Last Modified by:   Pop Alexandru
# @Last Modified time: 2018-03-20 16:46:51

import socket
import threading
import sys

class Client:
	#AF_INET = IPv4 and IPv6
	#SOCK_STREAM = TCP connections for UPD connections use SOCK_DGRAM
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	def __init__(self):
		self.sock.connect(('localhost', 10000))

		input_thread = threading.Thread(target=self.sendMsg)
		input_thread.daemon = True
		input_thread.start()

		while True:
			data = self.sock.recv(1024)
			if not data:
				break
			print(str(data, 'utf-8'))

	def sendMsg(self):
		while True:
			self.sock.send(bytes(input(""), 'utf-8'))



class Connection:


	connections = []
	def addClient(self,client_connection, client_address):
		print('test')
		self.connections.append(client_connection)
		clientThread = threading.Thread(self.handler(client_connection, client_address))
		clientThread.deamon = True
		clientThread.start()
		print(srt(client_address[0]) + ":" + str(client_address[1]), "connected")

	def handler(self, client_connection, client_address):

		while True:
			data = client_connection.recv(1024)
			print(data)
			print(self.connections)
			for connection in self.connections:
				if client_connection != connection:
					connection.send(data)
					print(data)
			if not data:
				print(srt(client_address[0]) + ":" + str(client_address[1]), "disconected")
				self.connections.remove(client_connection)
				client_connection.close()
				break




if __name__ == "__main__":
	client = Client()
	client.sendMsg()
