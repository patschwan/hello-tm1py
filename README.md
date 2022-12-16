# hello-tm1py
HelloWorld tm1py playground - PLAYground! ;-) I'm learning by doing and trying out and failing miserable.

But I love [TM1py](https://github.com/cubewise-code/tm1py) and I really appreciate this awesome collection of [TM1py Samples](https://github.com/cubewise-code/TM1py-samples) which are a great startpoint to try some real world use cases!

## Hints (and Kunz)
WSL Dev Enviroment and struggling with the connection
- IP Adress from WSL to Windows/TM1 Server

```shell
cat /etc/resolv.conf
```
- Powershell (as admin) to create new Firewall rule

```powershell
New-NetFirewallRule -DisplayName "WSL" -Direction Inbound  -InterfaceAlias "vEthernet (WSL)"  -Action Allow
```
