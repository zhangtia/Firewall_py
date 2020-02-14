# Firewall_Python

How to use:
1) Git clone the repository and navigate to the directory
2) Run Python3 in interactive mode with 
### `python3 -i`
3) Import Firewall class with
### `from firewall import Firewall`
4) Create a Firewall object with a CSV file
### `fw = Firewall({ your-csv-file-path-here })`
5) Check if network packet is valid with
### `fw.accept_packet({ direction }, { protocol }, { port }, { ip address })`
an example can be found below
### `fw.accept_packet("inbound", "tcp", 80, "192.168.1.2")`
6) To exit python interactive mode, use
### `exit()`
