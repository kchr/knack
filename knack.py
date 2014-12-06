#!/usr/bin/env python

import argparse
import socket


parser = argparse.ArgumentParser()

parser.add_argument('host', metavar='HOST', type=str,
                    help='Hostname to knock at')
parser.add_argument('ports', metavar='PORT', type=int, nargs='+',
                    help='Port(s) to use, in order specified')
parser.add_argument('-t', '--timeout', type=int,
                    help='Timeout for connection attempt (seconds)')
parser.add_argument('-v', '--verbose', action="store_true",
                    help='Show detailed information about failed ports')

parser.set_defaults(timeout=10)

args = parser.parse_args()


TCP_IP = args.host
TIMEOUT = args.timeout
VERBOSE = args.verbose

ports_failed = []

for TCP_PORT in args.ports:
    print "[*] Knocking on port %d..." % TCP_PORT
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT)
        s.connect((TCP_IP, TCP_PORT))
        s.close()
    except socket.error, e:
        if VERBOSE:
            print "[x] FAILED: %s" % str(e)
        ports_failed.append(str(TCP_PORT))


if len(ports_failed):
    print "\nFailed ports: %s" % " ".join(ports_failed)
