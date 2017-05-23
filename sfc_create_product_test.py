#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Testing module from creating product using 
http://www.sendfromchina.com/default/index/webservice


"""

# import osa

import zeep

wsdl = 'http://fulfill.sendfromchina.com/default/svc/wsdl'

client = zeep.Client(wsdl=wsdl)

req = {'HeaderRequest': {'customerId': 'R2036',
                         'appToken': 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDK1YNcdunmWXoK1ys6hyi+LWQdPx6Vmr/9kNlKOw4cK5Q8FWA3nfGeeG49Pq2TlYKVLdSw1fr60AAJFQOuXmol6lmyn+/xwx6j21XLx9/4vdDNSTR8Hcp7oqGNNr5DlI0onhJ7sd+rAxhIOwLNnZv6T/XtVqQNuGVXTq/dX0zkaQIDAQAB',
                         'appKey': 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDGmDLbsI4jELqCHgWikWqACICp299WSoiWgqghEXkQfvdEvwS5XWpdsSmdQwryR2rtg0DiS3vf74oVYBDJVHgcUdc2ov7QI5TPBqXJped7OoyrqYzaYFYshzGWgYC0wu5RCb71p2+4Z8NwDoJlvMVU4/fD9pL59PW8yYH1u3x4ewIDAQAB' }}

res = client.service.getCountry(req['HeaderRequest'])

print res['data']





