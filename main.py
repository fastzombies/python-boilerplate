#!/usr/bin/env python3

import sys, os
import argparse
import pathlib
import logging
from datetime import datetime
import module0
#import package1
from package1 import *
#from package1.module1 import *


# This class is for testing an arg
class StringAction(argparse.Action):
def __call__(self, parser, Namespace, values, option_string=None):
    if Namespace.string is 'x':
        parser.error('string value cannot be x')
    else:
        Namespace.string.replace('', values)

class ListAction(argparse.Action):
    def __call__(self, parser, Namespace, values, option_string=None):
        if len(Namespace.list) % 2:
            parser.error('list must be even number or args')
        else:
            Namespace.list.append(values)


def main(args):
    l.info(f'for loop')
    print(f'for loop')
    for _ in range(1):
        l.debug('main')
        l.info('main')
        #l.warning('main')
        #l.error('main')
        #l.critical('main')
        #l.fatal('main')
        print('main plain print\n')
        module0.module0_function0()
        module0.module0_function1()
        #package1.module1.module1_function1()
        module1.module1_function1()
        #module1_function1()



if __name__ == "__main__":
    """ This is executed when run from the command line """
    
    description = """
    A description that prints with help.
    """
    
    epilog = """
    An epilog if you want one.
    """
    
    parser = argparse.ArgumentParser(description=description,
                                    epilog=epilog,
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    # timestamp
    parser.add_argument('-t', '--timestamp',
                        required=False,
                        action='store',
                        dest="timestamp",
                        default=datetime.utcnow().strftime("UTC%Y%m%d%H%M"),
                        help='Specify a custom time stamp for the ward name. Othersie the current UTC will be used.')
    
    # Required positional argument
    #parser.add_argument('arg', 
    #                         help="Required positional argument")
    
    # Optional argument flag which defaults to False
    parser.add_argument('-f', '--flag', 
                        required=False,
                        dest='flag',
                        action="store_true", 
                        default=False,
                        help='This is a boolean flag that will store as True if used, False by default.')
    
    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument('-n', '--name', 
                        required=False,
                        action='store', 
                        dest='name')
    
    # Required argument which requires a parameter (eg. -d test)
    parser.add_argument('-fn', '--file',
                        required=False,
                        action="store",
                        dest="file",
                        help='A required arg with parameter.')
    
    # Required positional argument
    parser.add_argument('-i', '--index',
                        required=False,
                        type=int,
                        choices=range(0,100),
                        metavar='[0-100]',
                        default=13,
                        help="Required arg with a datatype and a range.")
    
    # Optional arg with a list of choices and a default.
    parser.add_argument('-m', '--multi', 
                        required=False,
                        action='store', 
                        default='yes',
                        const='yes', 
                        nargs='?',
                        choices=['yes', 'no', 'maybe'],
                        help="List of choices, default=yes.")
    
    # Optional arg with some kind of test
    parser.add_argument('-s', '--string',
                        required=False,
                        action=StringAction,
                        dest="string",
                        default='',
                        help='An optional arg with parameter and value test.')
    
    # Optional arg with some kind of test
    parser.add_argument('-l', '--list',
                        required=False,
                        action=ListAction,
                        dest="list",
                        nargs='+',
                        default=[],
                        help='An optional arg with parameters and values test.')
    
    # Optional path as pathlib object
    parser.add_argument('-p', '--path',
                        dest='path',
                        required=False,
                        type=pathlib.Path,
                        default=os.environ.get('PWD'),
                        help='A path stored as a pathlib object.')
    
    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument('-v', '--verbose',
                        action="count",
                        default=0,
                        help="Verbosity (-v, -vv, etc)")
    
    args = parser.parse_args()
    
    if args.verbose > 0:
        print(f'verbose = {args.verbose}')
    
    # Always print info
    # Set an advanced logging format
    #fmtdebug="%(levelname)s: [%(funcName)s():%(lineno)i] %(message)s"
    #fmtinfo="%(levelname)s: %(message)s"
    #fmt="%(levelname)s: %(funcName)s():%(lineno)i: %(name)s: %(message)s"
    
    l = logging.getLogger()
    fmtdebug = logging.Formatter('%(levelname)s: [%(funcName)s():%(lineno)i] %(message)s')
    fmtinfo=logging.Formatter('%(levelname)s: %(message)s')
    handler = logging.StreamHandler(sys.stdout)
    
    # If using any verbosity at all then print debug statements
    if args.verbose > 0:
        handler.setFormatter(fmtdebug)
        l.addHandler(handler)
        l.setLevel(10)
        #l.basicConfig(level=10, format=fmtdebug)
    else:
        handler.setFormatter(fmtinfo)
        l.addHandler(handler)
        l.setLevel(20)
        #l.basicConfig(level=20, format=fmtinfo)
    
    main(args)
