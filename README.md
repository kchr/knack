knack
=====

Port knocking client for command-line usage

This is a minimal client implementation of the port knocking model. 

It basically tries to connect to a given set of ports on a remote host, without sending or receiving any data. The idea is that the remote host is listening for a specific pattern of ports to be opened in sequence, and then acting upon it in some fashion (mostly opening arbitrary ports for later usage). This can be used to keep weak services hidden from the public but accessible through simple TCP/IP operations.

Most port knocking setups involve a series of dummy (unused) ports being monitored for connection attempts. To keep the operation as stealth as possible the server should not reply to these requests, only register them. This makes it possible for other ports to be thrown in to confuse someone sniffing the wires, but makes it impossible for the client to separate packet loss from received knocks (both would time out if server is not configured to reply). 

Therefore this application will only treat local network (and routing) errors as fatal. Timeouts and completed attempts are treated as equally good knocks!

Note that this package does not handle the listening/server part of the port knocking protocol in any way, it only knocks. Please see [knockknock](https://github.com/moxie0/knockknock) for a server.

More information:

https://en.wikipedia.org/wiki/Port_knocking

http://www.portknocking.org/view/resources


Usage
-----

    $ knack [-h] [-t TIMEOUT] [-v] HOST PORT [PORT ...]
    
    positional arguments:
      HOST                  Hostname to knock at
      PORT                  Port(s) to use, in order specified
    
    optional arguments:
      -h, --help            show this help message and exit
      -t TIMEOUT, --timeout TIMEOUT
                            Timeout for connection attempt (seconds), default 10
      -v, --verbose         Show detailed information


A successful operation is silent, unless you supply the verbose flag (this will also show the reason for any failed attempts).

Return code is 0 for success and 1 for failures.
