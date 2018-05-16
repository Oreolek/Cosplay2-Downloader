#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Himura Kazuto <himura@tulafest.ru>

from getpass import getpass
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen
from yaml import load

configfile = open("config.yml", "r")
config = load(configfile.read())
configfile.close()
event_name = config['event_name']
login = config['admin_cs2_name']

login_info = urlencode({'name':     login,
                        'password': getpass('Password for ' + login + ': ')}).encode('ascii')
try:
    with urlopen('http://' + event_name + '.cosplay2.ru/api/' + 'users/login', login_info) as r:
        print("Your cookie: '%s'\nStill hot!" % r.getheader('Set-Cookie'))
except HTTPError as e:
    print('Failed T_T Check your password...\n' + str(e))
