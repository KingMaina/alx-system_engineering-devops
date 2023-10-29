# Simple Web Stack

## Diagram

![Simple Web Stack](0-simple_web_stack.png)

## Description

This diagram shows a simple web stack. It consists of a single server, a single web server, and a single database server.

## Components

1. 1 server
2. 1 web server
3. 1 application server
4. 1 database server
5. Application code
6. 1 domain name (www.foobar.com)

## Specifics

1. What is a server?
    * A server is a computer that provides a service to another computer program and its user, also known as the client.

2. What is the role of the domain name?
    * A domain name is a human-readable name that is easy to remember and is used to identify a computer on the internet.

3. What type of DNS record is www in www.foobar.com?
    * A DNS A record. It is a DNS record that maps a domain name to an IPv4 address. In this case, `www.foobar.com` could resolve to e.g `192.168.100.56`

4. What is the role of the web server?
    * A web server is a computer that stores web server software and a website's component files. It listens for requests made via HTTP, the basic network protocol used to distribute information on the World Wide Web. The server then serves up files, such as HTML, CSS, JavaScript, and images, to the requester.

5. What is the role of the application server (IIS)?
    * An application server is a server that hosts applications. It provides an environment for running applications written in a specific programming language. It typically sits between the database server and the web server.

6. What is the role of the database?
    * A database is a collection of information that is organized so that it can be easily accessed, managed and updated. Data is organized into rows, columns and tables, and it is indexed to make it easier to find relevant information.

7. What is the server using to communicate with the computer of the user requesting the website?
    * The server is using HTTP to communicate with the computer of the user requesting the website or HTTP over SSL (HTTPS) if the website is secured.

## Issues with this infrastructure

1. Single Point of Failure
    * If the server goes down, the website goes down. If the web server goes down, the website goes down. If the application server goes down, the website goes down. If the database server goes down, the website goes down.

2. Downtime during maintenance
    * If the server goes down for maintenance, the website goes down. If the web server goes down for maintenance, the website goes down. If the application server goes down for maintenance, the website goes down. If the database server goes down for maintenance, the website goes down.

3. Cannot scale if too much incoming traffic
    * When the server receives too much incoming traffic, it will not be able to handle it and the website will go down. This is because the server is not able to handle the load.
