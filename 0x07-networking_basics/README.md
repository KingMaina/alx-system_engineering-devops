# Networking basics

* This repo contains answers to questions about networking basics and some commands to check network information.
* 0-3 files contain answers to questions about OSI model, LAN, WAN, internet, MAC address, IP address, TCP and UDP.
* 4-TCP_and_UDP contains a bash script that displays listening ports and shows the PID and name of the program to which each listening socket belongs.
* 5-is_the_host_on_the_network contains a bash script that pings an IP address passed as an argument 5 times.
* 4 and 5 are executable files.

## Usage

```bash
./4-TCP_and_UDP
```

```bash
./5-is_the_host_on_the_network <IP address>
```

* If an IP address is not passed as an argument, the script will display Usage: 5-is_the_host_on_the_network {IP_ADDRESS} and exit with code 1.
