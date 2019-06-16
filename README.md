# Network-Scan-Tool

Functions designed for scanning ports and pinging hosts.
#Port scanner uses multiprocessing to scan ports quickly

## Example how to use
### import the functions

```
from network_scanner_module.port_scanner_threading import scan_ports,tcp_connect
from network_scanner_module.network_scan import network_scan
```

### tcp_connect and scan ports
tcp_connect is used for single tcp connections.


```
test_tcp_port1 = tcp_connect("google.com",80)
test_tcp_port2 = tcp_connect("google.com",443)
test_tcp_port3 = tcp_connect("google.com",500)
```
These will all return true except for test_tcp_port3 since port 500 is closed on google.com


scan ports is designed for multiple ports
```
test_scan_port_range = scan_ports('google.com',1,1024) # Must state start and finish port
```

This will scan ports 1 through 1024 and then return a dictionary of all the ports that are open

### network_scan
This function is designed to ping a range of address or a particular hostname.

```
ping = network_scan("172.217.7.0","24") # must be in CIDR notation
ping_name = network_scan('google.com',hostname=True) # hostname is set to true for pinging one address or a hostname
ping_name1 = network_scan('Idontexist.com',hostname=True) 
```
