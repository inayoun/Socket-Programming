# Socket-Programming
TCP and UDP Socket Programming

- TCP networked application using sockets. TCP_client sends a random String to TCP_server, TCP_server concatenates String and returns to TCP_client. Output should look like:\
Client:
~~~
sent: GaQGJAB1xY
received: CuE190z1pzGaQGJAB1xY

sent: yzyX9cU3UK
received: iwdkV0stp1yzyX9cU3UK
~~~
\
Server:
~~~
received data GaQGJAB1xY; appended CuE190z1pz
received data yzyX9cU3UK; appended iwdkV0stp1
~~~

\- UDP remote procedure call (RPC) system that allows a client to invoke methods remotely on a server machine. Client sends prime(N) and server returns yes/no. utput should look like:\
Client:
~~~
sent: prime(82)
prime: no

sent: prime(74)
prime: no

sent: yzyX9cU3UK
received: iwdkV0stp1yzyX9cU3UK
~~~
\
Server:
~~~
 argument is 82
 argument is 74
~~~
