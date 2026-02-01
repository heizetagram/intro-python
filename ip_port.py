# Task 2
def ip_port():
    ip_port='192.168.0.1:443'
    
    elements = ip_port.split(':')
    ip = elements[0]
    port = elements[1]

    print(f"ip is {ip} and the port is {port}")

ip_port()