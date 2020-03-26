# Firewall_Python

How to use:
1) Git clone the repository and navigate to the directory
2) Run Python3 in interactive mode with 
### `python3 -i`
3) Import Firewall class with
### `from firewall import Firewall`
4) Create a Firewall object with a CSV file
### `fw = Firewall( [your-csv-file-path-here] )`
5) Check if network packet is valid with
### `fw.accept_packet( [direction] , [protocol] , [port] , [ip address] )`
an example can be found below
### `fw.accept_packet("inbound", "tcp", 80, "192.168.1.2")`
6) To exit python interactive mode, use
### `exit()`


# TESTING

I tested my code to be able to handle the entire range of ports and ip addresses. In my first design and implementation, my constructor was frozen as it tried to process 65536 x 256 x 256 x 256 x 256 inputs for every direction/protocol combination. I queried the edge cases with port number 0 and 65535 and ip addresses of 0.0.0.0 and 255.255.255.255 to ensure functionality.

Used pylint for style checking.

# DESIGN and IMPLEMENTATION

After reading the sprcifications, my first thought was to initialize a hash table with composite keys of all ports and ip addresses. I wanted the fastest lookup time and decided that the hash table initialization would take up the bulk of the time. I thought that a real-life firewall should have lowest latency in the lookup stage while all values are initialized and saved.

However, as I was testing (mentioned above) I realized that initializing every single composite key was taking way too long and I decided to go with the raw inputs of port and ip addresses as composite key of my hash table. This would greatly reduce the initialization time while the trade off would be a possible slower lookup.

I still wanted to take advantage of the O(1) lookup, and I made my accept_packet a O(1) complexity at best and a O(n) in the worst case.
