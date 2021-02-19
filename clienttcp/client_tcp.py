import socket
import sys

def main():
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as error:
        print("Connection failed: {} ".format(error))
        sys.exit()

    
    host = input("Enter IP host to connect: ")
    port = int(input("Enter port: "))

    try:
        connection.connect((host, port))
        print("connected!")
        connection.shutdown(2)
    except socket.error as error:
        print("Failed connected: {}".format(error))
        sys.exit()
    
        
main()