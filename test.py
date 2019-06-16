from network_scanner_module.port_scanner_threading import scan_ports,tcp_connect
from network_scanner_module.network_scan import network_scan

def test_google_open():
    test_ip1 = tcp_connect('google.com',80)
    test_ip2 = tcp_connect('google.com',443)
    test_ip3 = tcp_connect('google.com',53)
    assert test_ip1 == True
    assert test_ip2 == True
    assert test_ip3 == False

def test_port_scan_multiple():
    results = scan_ports('google.com',1,500)
    assert results[443] == True
    assert results[80] == True
    assert results[500] == False

def test_ping_scan_google_net():
    ping = network_scan("172.217.7.0","24")
    #172.217.7.14 is google.com
    assert ping['172.217.7.14'] == True

    ping_name = network_scan('google.com',hostname=True)
    ping_name1 = network_scan('IKhammer.com',hostname=True)
    assert ping_name['google.com'] == True
    assert ping_name1['IKhammer.com'] == False
