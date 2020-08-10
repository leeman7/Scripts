#!/usr/bin/env python3
"""
A simple traceroute(8) application in Python
"""

from docopt import docopt
from network import Trace


def main():
    usage="""
Usage: py-traceroute [-m <hops>] <destination>
       py-traceroute --help
       py-traceroute --version
Arguments:
  destination                   Destination host to probe
Options:
  -m <hops>, --max-hops <hops>  Max number of hops to probe
                                [default: 30]
  -h, --help                    Display this usage info
  -v, --version                 Display version and exit
"""

    args = docopt(usage, version=1.0)
    tracer = Trace(
        dst=args['<destination>'],
        hops=int(30)
    )

    tracer.run()

if __name__ == '__main__':
    main()