#!/usr/bin/python
# -*- coding: utf-8 -*-
"""options"""
import argparse

parser = argparse.ArgumentParser(description='Kernel Exception Management')
parser.add_argument('--expires_in', help='Specify length of days to expire', required=False)
parser.add_argument('--report', default=False, action='store_true', help='Outputs (stdout) a list of servers with more than one kernel package')
parser.add_argument('--execute', default=False, action='store_true', help='Adds exceptions for non-running extra kernels')

class Options(object):
    """options class"""
    def __new__(cls):
        args = vars(parser.parse_args())
        return args
