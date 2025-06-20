from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        network = random.randint(0x0B000000, 0xDF000000)
        prefix = random.randint(8, 24)
        IPv4Network.__init__(self, (network, prefix), strict=False)
    def regular(self):
        return self.is_global

list1 = []

while len(list1)<=50:
    ip = IPv4RandomNetwork()
    r = ip.regular()
    if r:
        list1.append(ip)

def value_ip(net):
    return int(net.netmask)*2**32 + int(net.network_address)

list2 = sorted(list1, key=value_ip)
for i in list2:
    print (str(i))
