# HTTPS SSL

## Description
In this section, we configure SSL termination in our haproxy load balancer so that encrypted web traffic can be processed.

## Tasks

### Display information about our subdomains

* In `0-world_wide_web` script, we use the `dig` command to query our website subdomains for DNS records and print them accordingly. The script takes 2 arguments; the website domain name and a subdomain.
* Usage: 
```sh
./0-world_wide_web <domain> <subdomain>
# Output: The subdomain <subdomain> is a <dns_record_type> record and points to <IP_address>
```

### Configure SSL termination in HAProxy

### Redirect HTTP traffic to HTTPS
