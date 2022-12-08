from TM1py.Services import TM1Service

# Windows Firewall deaktivieren und im WSL cat /etc/resolv.conf IP Adresse Win Host
# IP erneuert nach Neustart der WSL Distro (statische IP vergeben?)
# > cat /etc/resolv.conf 
# https://github.com/Microsoft/WSL/issues/1032
# with TM1Service(address='losthost', port=52670, user='admin', password='apple', ssl=False) as tm1:
with TM1Service(address='192.168.80.1', port=52670, user='admin', password='apple', ssl=False) as tm1:
    for cube in tm1.cubes.get_all():
        print(cube)
