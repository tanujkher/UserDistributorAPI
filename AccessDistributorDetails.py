from urllib import request
import urllib
from datetime import datetime

curr_user = ''
isAdmin = False

def user_func():
    i = 'U'
    while(i == 'U'):
        c = input(
            'Enter 1 to view User Details(Used GET Request)(Accessible to all)\n' +
            'Enter 2 to add User Details(Used POST Request)(Accessible to ADMIN ONLY)\n' +
            'Enter 3 to edit User Details(Used PUT Request)(Accessible to ADMIN ONLY)\n' +
            'Enter 4 to delete User Details(Used DELETE Request)(Accessible to ADMIN ONLY)\n'
        )
        if(c == '1'):
            su = input('Enter user_ID to be searched\n OR\n* for all users\n')
            if(su == '*'):
                r = request.Request('http://127.0.0.1:5000/user', method='GET')  
                try:
                    res = request.urlopen(r)
                    print(res.read())
                except urllib.error.HTTPError as e:
                    print(e.code, e.read())
            else:  
                r = request.Request('http://127.0.0.1:5000/user/{}'.format(su), method='GET')
                try:
                    res = request.urlopen(r)
                    print(res.read())
                except urllib.error.HTTPError as e:
                    print(e.code, e.read())
        if(c == '2'):
            if(isAdmin):
                au = input('Enter user_ID to be added\t')
                r0 = request.Request('http://127.0.0.1:5000/user/{}'.format(au), method='GET')
                try:
                    r1 = request.urlopen(r0)
                    print('User {} already exists'.format(au))
                except urllib.error.HTTPError as e:
                    print('Enter data of new user')
                    aud = {'user_ID' : '{}'.format(au), 'password' : '{}'.format(input('Enter new user password\t')), 'role' : '{}'.format(input('Enter new user role\t')), 'isAdmin' : '{}'.format(input('Enter if new user is Admin or Not\t'))}
                    data = urllib.parse.urlencode(aud)
                    data = data.encode('ascii')
                    r = request.Request('http://127.0.0.1:5000/user/{}'.format(au), method='POST', data=data)
                    try:
                        res = request.urlopen(r)
                        print(res.read())
                    except urllib.error.HTTPError as e:
                        print(e.code, e.read())
            else:
                print('ONLY ADMIN CAN ADD USERS\n')
        if(c == '3'):
            if(isAdmin):
                ap = input('Enter user_ID to edit details\t')
                r0 = request.Request('http://127.0.0.1:5000/user/{}'.format(ap), method='GET')
                try:
                    r1 = request.urlopen(r0)
                    print('Enter data to be updated\n')
                    aup = {'user_ID' : '{}'.format(ap), 'password' : '{}'.format(input('Enter new user password\t')), 'role' : '{}'.format(input('Enter new user role\t')), 'isAdmin' : '{}'.format(input('Enter if new user is Admin or Not\t'))}
                    data = urllib.parse.urlencode(aup)
                    data = data.encode('ascii')
                    r = request.Request('http://127.0.0.1:5000/user/{}'.format(ap), method='PUT', data=data)
                    try:
                        res = request.urlopen(r)
                        print(res.read())
                    except urllib.error.HTTPError as e:
                        print(e.code, e.read())
                except urllib.error.HTTPError as e:
                    print('User {} doesn\'t exists'.format(ap))
            else:
                print('ONLY ADMIN CAN EDIT USER DETAILS\n')
        if(c == '4'):
            if(isAdmin):
                ad = input('Enter user_ID to delete\t')
                r = request.Request('http://127.0.0.1:5000/user/{}'.format(ad), method='DELETE')
                try:
                    res = request.urlopen(r)
                    print(res.read())
                except urllib.error.HTTPError as e:
                    print(e.code, e.read())
            else:
                print('ONLY ADMIN CAN DELETE USERS\n')
        i = input('Press U for User Details or E to Exit\t')  

def dist_func():
    i = 'D'
    while(i == 'D'):
        di = input(
            'Enter 1 to view Distributor Records\n' + 
            'Enter 2 to add Distributor Records\n' + 
            'Enter 3 to extend Distributor Contract Date\n'+
            'Enter 4 to Cancel Distributor License\n'
        )
        if di == '1':
            vi = input('Enter Distributor ID\nOR\nEnter * to view all Distributors details\n')
            if vi == '*':
                r = request.Request('http://127.0.0.1:5000/dis', method='GET')
                try:
                    res = request.urlopen(r)
                    print(res.read())
                except urllib.error.HTTPError as e:
                    print(e.code, e.read())
            else:
                r = request.Request('http://127.0.0.1:5000/dis/{}'.format(vi), method='GET')
                try:
                    res = request.urlopen(r)
                    print(res.read())
                except urllib.error.HTTPError as e:
                    print(e.code, e.read())
        if di == '2':
            if isAdmin:
                ai = input('Enter new Distributor_ID\t')
                r0 = request.Request('http://127.0.0.1:5000/dis/{}'.format(ai), method='GET')
                try:
                    r1 = request.urlopen(r0)
                    print('Distributor {} already exists'.format(ai))
                except urllib.error.HTTPError as e:
                    aid = {'dis_ID' : '{}'.format(ai), 'product_name' : '{}'.format(input('Enter product name\t')), 'contract_date' : datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S')}
                    data = urllib.parse.urlencode(aid)
                    data = data.encode('ascii')
                    r = request.Request('http://127.0.0.1:5000/dis/{}'.format(ai), method='POST', data=data)
                    try:
                        res = request.urlopen(r)
                        print(res.read())
                    except urllib.error.HTTPError as e:
                        print(e.code, e.read())
            else:
                print('ONLY ADMIN CAN ADD DISTRIBUTOR RECORDS')
        if di == '3':
            if isAdmin:
                ci = input('Enter the Distributor_ID to extend contract\t')
                r0 = request.Request('http://127.0.0.1:5000/dis/{}'.format(ci), method='GET')
                try:
                    r1 = request.urlopen(r0)
                    cd = datetime.utcnow().strftime('%d-%m-%Y %H:%M:%S')
                    did = {'contract_date' : '{}'.format(cd)}
                    data = urllib.parse.urlencode(did)
                    data = data.encode('ascii')
                    r = request.Request('http://127.0.0.1:5000/dis/{}'.format(ci), method='PUT', data=data)
                    try:
                        res = request.urlopen(r)
                        print(res.read())
                    except urllib.error.HTTPError as e:
                        print('Distributor {} doesn\'t exist'.format(ci))
                except urllib.error.HTTPError as e:
                    print('Distributor {} doesn\'t exist'.format(ci))
            else:
                print('ONLY ADMIN CAN EXTEND DISTRIBUTOR CONTRACT DATE')
        if di == '4':
            if isAdmin:
                di = input('Enter the Distributor_ID to cancel License\t')
                r = request.Request('http://127.0.0.1:5000/dis/{}'.format(di), method='DELETE')
                try:
                    res = request.urlopen(r)
                    print(res.read())
                except urllib.error.HTTPError as e:
                    print(e.code, e.read())
            else:
                print('ONLY ADMIN CAN CANCEL DISTRIBUTOR LICENSE')
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
