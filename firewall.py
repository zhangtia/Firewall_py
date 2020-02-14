"""
Firewall class that takes in a CSV file of all valid inputs.
accept_packet verifies if request is valid
"""


import csv
import ipaddress


class Firewall:
    """Firewall class. Initialize with a CSV files for all valid inputs"""
    def __init__(self, filepath):

        self.in_tcp = {}
        self.in_udp = {}
        self.out_tcp = {}
        self.out_udp = {}

        with open(filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[0] == "inbound" and row[1] == "tcp":
                    # INBOUND TCP
                    self.in_tcp[(row[2], row[3])] = 1
                elif row[0] == "inbound" and row[1] == "udp":
                    # INBOUND UDP
                    self.in_udp[(row[2], row[3])] = 1
                elif row[0] == "outbound" and row[1] == "tcp":
                    # OUTBOUND TCP
                    self.out_tcp[(row[2], row[3])] = 1
                elif row[0] == "outbound" and row[1] == "udp":
                    # OUTBOUND UDP
                    self.out_udp[(row[2], row[3])] = 1


    def accept_packet(self, direction, protocol, port, ip_addr):
        """ Usage: fw.accept_package(direction, protocol, port, ip address) """
        to_search = {}
        if direction == "inbound" and protocol == "tcp":
            to_search = self.in_tcp
        elif direction == "inbound" and protocol == "udp":
            to_search = self.in_udp
        elif direction == "outbound" and protocol == "tcp":
            to_search = self.out_tcp
        elif direction == "outbound" and protocol == "udp":
            to_search = self.out_udp

        if to_search.get((port, ip_addr)) == 1:
            # if composite key exists, O(1) lookup
            return True

        for record in to_search:
            if "-" in record[0] and "-" in record[1]:
                # both port and ip address stored are ranges
                if (int(record[0].split("-")[0]) <= port <= int(record[0].split("-")[1]) and
                        int(ipaddress.IPv4Address(record[1].split("-")[0])) <=
                        int(ipaddress.IPv4Address(ip_addr)) <=
                        int(ipaddress.IPv4Address(record[1].split("-")[1]))):
                    return True
            elif "-" in record[0]:
                # port is a range
                if (int(record[0].split("-")[0]) <= port <= int(record[0].split("-")[1])
                        and ip_addr == record[1]):
                    return True
            elif "-" in record[1]:
                # ip addr is a range
                if (port == int(record[0]) and int(ipaddress.IPv4Address(record[1].split("-")[0]))
                        <= int(ipaddress.IPv4Address(ip_addr))
                        <= int(ipaddress.IPv4Address(record[1].split("-")[1]))):
                    return True

        return False
