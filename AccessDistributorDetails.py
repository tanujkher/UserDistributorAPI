from urllib import request
import urllib
from datetime import datetime

curr_user = ''
isAdmin = False

def user_func():
    i = 'U'
    while(i == 'U'):
        i = input('Press U for User Details or E to Exit\t')  

def dist_func():
    i = 'D'
    while(i == 'D'):
        i = input('Press D to view Distributor Details or E to Exit\t')

if(curr_user == ''):
    print('Login to Continue')
    user_ID = input('Enter your user_ID\t')
    rm = {'user_ID' : '{}'.format(user_ID), 'password' : '{}'.format(input('Enter your password\t'))}
    data = urllib.parse.urlencode(rm)
    data = data.encode('ascii')
    r = request.Request('http://127.0.0.1:5000/login/{}'.format(user_ID), method='POST', data=data)
    try:
        res = request.urlopen(r)
        if str(res.read())[3] == 'Y':
            isAdmin = True
            curr_user = user_ID
        print('Welcome {}'.format(user_ID))
        k = input('Press D to view Distributor Details, U for User Details or E to Exit\t')
        if(k == 'D'):
            dist_func()
        elif(k == 'U'):
            user_func()
    except urllib.error.HTTPError as e:
        print(e.code, e.read())
