# Web stack debugging 4

## Introduction
Here, we are given an ubuntu server running and nginx server however ton performing a load test, there is a significant amount of failed requests.
Our job is to come up with a puppet script that will be deployed to the server so as to configure the nginx  server to handle the high number of requests.

## Load test
For starters we will run load test the server using attotal of 200 requests at a concurrency count  of 100 simultaneous connections.
Run the following command using Apache Benchmark.
```bash
ab -c 100 -n 2000 localhost/
```
The command displayed quite a number of failed requests. Exactly 658 although the number can vary.

## Debugging web server

We then inspect the server error logs to find out if there are error responses.
```bash
cat /var/logs/nginx/error.log
```
We see that quite a number of requests get a server 500 response with the message **Too many open files**
Upon further research on the error, it appears there is a limit on the number of concurrent files open. A quick look at the ULIMIT configuration says that it is capped at 15. We have to increase this number to accomodate the large volume of requests.
```bash
cat /etc/default/nginx # ULIMIT="-n 15"
```

## Corrective Measure

To correct the issue, we wrote a pppet script that increseas this limit and ensures that should the server state deviate, the scipt will return the state to the desired one.
Our puppet script ensures the following:
* Nginx is installed and running
* The file /etc/default/nginx exists and contains the desired ULIMIT value. We will put 65535.
* Notify the nginx service daemon and restart the service.
The script can be found [here](0-the_sky_is_the_limit_not.pp)

