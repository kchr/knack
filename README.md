knack
=====

Port knocking client for command-line usage

Usage
-----

    $ knack [-h] [-t TIMEOUT] [-v] HOST PORT [PORT ...]
    
    positional arguments:
      HOST                  Hostname to knock at
      PORT                  Port(s) to use, in order specified
    
    optional arguments:
      -h, --help            show this help message and exit
      -t TIMEOUT, --timeout TIMEOUT
                            Timeout for connection attempt (seconds)
      -v, --verbose         Show detailed information about failed ports
