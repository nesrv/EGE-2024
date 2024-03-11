import ipaddress
mask = 255, 255, 255, 224
addr = 162, 196, 0, 157


subnet_mask = '255.255.255.224'
ip_address = '162.198.0.157'

network = ipaddress.IPv4Network(ip_address + '/' + subnet_mask, strict=False)
print(network)
host_number = int(ipaddress.IPv4Address(ip_address)) - int(network.network_address)

print(host_number)
