# import socket library
from socket import *
import sys
NUM_TRANSMISSIONS=10
if(len(sys.argv) < 2):
  print("Usage: python3 " + sys.argv[0] + " server_port")
  sys.exit(1)
assert(len(sys.argv) == 2)
server_port = int(sys.argv[1])

# Create a socket for the server
soc_server = socket(AF_INET, SOCK_DGRAM)
# Bind it to server_port 
soc_server.bind(('127.0.0.1', server_port))
# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
  # Receive RPC request from client
  byteData, (address, port) = soc_server.recvfrom(4096)
  # Turn byte array that you received from client into a string variable called rpc_data
  rpc_data = byteData.decode()
  # Parse rpc_data to get the argument to the RPC.
  # Remember that the RPC request string is of the form prime(NUMBER)
  argument = int(rpc_data[6:-1])
  # Print out the argument for debugging
  print('argument is', argument)
  # Compute if the number is prime (return a 'yes' or a 'no' string)
  result = ''
  if argument > 1:
   # check for factors
   for i in range(2,argument):
       if (argument % i) == 0:
           result = 'no'
           break
   else:
       result = 'yes'
  else:
    result = 'no'
  # Send the result of primality check back to the client who sent the RPC request
  soc_server.sendto(result.encode(), ('127.0.0.1', port))
# Close server's socket
soc_server.close()