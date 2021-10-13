# import socket library
from socket import *
import sys
import random
NUM_TRANSMISSIONS=10
if (len(sys.argv) > 3) or len(sys.argv) < 2:                                    
  print("Usage: python3 "  + sys.argv[0] + " server_port [random_seed]")        
  sys.exit(1)                                                                   
                                                                                
if len(sys.argv) == 3:                                                          
    random_seed = int(sys.argv[2])                                              
    random.seed(random_seed) 

server_port=int(sys.argv[1])

# Create a datagram socket for the client
client_soc = socket(AF_INET, SOCK_DGRAM)

# Repeat NUM_TRANSMISSIONS times
for i in range(NUM_TRANSMISSIONS):
  # Create an RPC request to compute if a number is prime
  rpc_data="prime(" + str(random.randint(0, 100)) + ")"

  # Send RPC request (i.e., rpc_data) to the server
  client_soc.sendto(rpc_data.encode(), ('127.0.0.1', server_port))
  # Print debugging information
  print("sent: " + rpc_data)

  # Receive result back from the server into the variable result_data
  result_data, address = client_soc.recvfrom(4096)
  # Display it in the format "prime: yes" or "prime: no"
  print("prime:", result_data.decode())

# Close any sockets that are open
client_soc.close()