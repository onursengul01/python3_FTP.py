import socket 
s = socket.socket()
host = input(str("Please enter the host address of the sneder: "))
port = 8080

s.connect((host,port))
print("Coonected")

filename = input(str("PLease enter a filename for the incoming file: " ))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
print("File has neem recived succesfully.")

