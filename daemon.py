#!/usr/bin/python2.7
#coding=utf-8
import requests
import os,sys,time,commands
pid=os.fork()
if pid>0:
	sys.exit(0)

#修改子进程的目录
os.chdir("/home/work")
os.setsid()
os.umask(0)

pid=os.fork()
if pid>0:
	sys.exit(0)
sys.stdout.flush()
sys.stderr.flush()
si=file("/dev/null",'r')
so=file("/home/work/test",'a+')
se=file("/dev/null",'a+',0)
os.dup2(si.fileno(),sys.stdin.fileno())
os.dup2(so.fileno(),sys.stdout.fileno())
os.dup2(se.fileno(),sys.stderr.fileno())

while True:
	os.system('cat /dev/null>/home/work/test')
	os.system('./mem.sh')
	url='http://localhost:5000/'
	files={'file':open('/home/work/test')}
	r=requests.post(url,files=files)
	time.sleep(5)




