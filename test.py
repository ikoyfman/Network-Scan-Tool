from network_scanner_module import network_scanning, Networks_Hosts, port_scanner_threading


def test_google_open():
    test_ip1 = port_scanner_threading.tcp_connect("google.com", 80)
    test_ip2 = port_scanner_threading.tcp_connect("google.com", 443)
    test_ip3 = port_scanner_threading.tcp_connect("google.com", 53)
    assert test_ip1 is True
    assert test_ip2 is True
    assert test_ip3 is False


def test_port_scan_multiple():
    results = port_scanner_threading.scan_ports("google.com", 1, 500)
    assert results[443] is True
    assert results[80] is True
    assert results[500] is False


def test_ping_scan_google_net():
    ping = network_scanning.network_scan("172.217.7.0", "24")
    # 172.217.7.14 is google.com
    assert ping["172.217.7.14"] is True

    ping_name = network_scanning.network_scan("google.com", hostname=True)
    ping_name1 = network_scanning.network_scan("IKhammer.com", hostname=True)
    assert ping_name["google.com"] is True
    assert ping_name1["IKhammer.com"] is False


def test_hosts():
    cloud_flare = Networks_Hosts.Network("173.245.48.0", 20)
    cloud_flare.discover_hosts()
    cloud_flare.discover_hostnames()


if __name__ == "__main__":
    results = network_scanning.network_scan("google.com", 1, 500)
    print(results)

