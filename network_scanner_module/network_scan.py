from platform import system
from ipaddress import IPv4Network
from subprocess import Popen, PIPE

def network_scan(address="192.168.1.0", subnet=str(24),hostname=False):
    """
    This function is designed to use your OS ping command to ping hosts.
    Will return a dictionary of True and False for each ip address in the subnet
    """

    #Hostname ping
    if hostname:
        if system() == 'Windows':
            ping_arg = '-n'
        else:
            ping_arg = '-c'
        cmd = ['ping', ping_arg, '1', address]
        
        proc = Popen(cmd, stdout=PIPE)
        proc.wait()
        if proc.returncode == 0:
            return {address:True}
        else:
            return {address:False}
        

    # Get all usable hosts
    formated_address = address + "/" + subnet
    hosts = list(IPv4Network(formated_address).hosts())


    # Get your OS
    if system() == 'Windows':
        ping_arg = '-n'
    else:
        ping_arg = '-c'

    # CMD list for 
    cmd_list = [['ping', ping_arg, '1', hosts[host].compressed]
                for host in range(0, len(hosts))]

    # Ping all hosts capture response
    results = {}
    procs_list = [Popen(cmd, stdout=PIPE) for cmd in cmd_list]
    for proc in procs_list:
        proc.wait()
        if proc.returncode == 0:
            results.setdefault(proc.args[3], True)
        else:
            results.setdefault(proc.args[3], False)
    
    return results