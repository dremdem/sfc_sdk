#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Testing module for creating product using 
http://www.sendfromchina.com/default/index/webservice
"""

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from werkzeug.datastructures import MultiDict

from forms import SFCCreateOrder, SFCCreateProduct, SFCOrderDetail
from sfc_api import SFCAPI

app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)
app.secret_key = 's3cr3tasdasdasdasd'
header_request = {'customerId': 'R2036',
                  'appToken': 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDK1YNcdunmWXoK1ys6hyi+LWQdPx6Vmr/9kNlKOw4cK5Q8FWA3nfGeeG49Pq2TlYKVLdSw1fr60AAJFQOuXmol6lmyn+/xwx6j21XLx9/4vdDNSTR8Hcp7oqGNNr5DlI0onhJ7sd+rAxhIOwLNnZv6T/XtVqQNuGVXTq/dX0zkaQIDAQAB',
                  'appKey': 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDGmDLbsI4jELqCHgWikWqACICp299WSoiWgqghEXkQfvdEvwS5XWpdsSmdQwryR2rtg0DiS3vf74oVYBDJVHgcUdc2ov7QI5TPBqXJped7OoyrqYzaYFYshzGWgYC0wu5RCb71p2+4Z8NwDoJlvMVU4/fD9pL59PW8yYH1u3x4ewIDAQAB'}
wsdl = 'http://fulfill.sendfromchina.com/default/svc/wsdl'

sfcapi = SFCAPI(p_wsdl=wsdl, p_header_request=header_request)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/create_product", methods=['GET', 'POST'])
def create_product():
    res = None
    if request.method == 'POST':
        product_info = {k: v for k, v in request.form.items() if k not in ('csrf_token', 'pocId', 'poValue', 'imgUrl')}
        product_info['image'] = {'imgUrl': request.form['imgUrl']}
        product_info['qcs'] = {'pocId': request.form['pocId'], 'poValue': request.form['poValue']}
        res = sfcapi.create_product(product_info)
        form = SFCCreateProduct(request.form)
    else:
        form = SFCCreateProduct()
    return render_template('create_product.html', form=form, res=res)


@app.route("/create_order", methods=['GET', 'POST'])
def create_order():
    res = None
    if request.method == 'POST':
        order_info = {k: v for k, v in request.form.items() if k in
                      [i for i in SFCCreateOrder.__dict__.keys() if i[0] != '_']}

        order_detail= []

        order_detail.append({k.strip('detail1-'): v for k, v in request.form.items() if
                        k.startswith('detail1') and k != 'detail1-csrf_token' })
        order_detail.append({k.strip('detail2-'): v for k, v in request.form.items() if
                        k.startswith('detail2') and k != 'detail2-csrf_token' })
        order_detail.append({k.strip('detail3-'): v for k, v in request.form.items() if
                        k.startswith('detail3') and k != 'detail3-csrf_token' })

        res = sfcapi.create_order(p_order_info=order_info, p_order_detail=order_detail)
        form_order = SFCCreateOrder(MultiDict(order_info))
        form_order.detail1 = SFCOrderDetail(MultiDict(order_detail[0]))
        form_order.detail2 = SFCOrderDetail(MultiDict(order_detail[1]))
        form_order.detail3 = SFCOrderDetail(MultiDict(order_detail[2]))
    else:
        form_order = SFCCreateOrder()
        # init 3 test order detail elements
        form_order.detail1 = SFCOrderDetail()
        form_order.detail2 = SFCOrderDetail()
        form_order.detail3 = SFCOrderDetail()

    return render_template('create_order.html', form_master=form_order, res=res)


@app.route("/create_asn", methods=['GET', 'POST'])
def create_asn():
    res = None
    if request.method == 'POST':
        order_info = {k: v for k, v in request.form.items() if k in
                      [i for i in SFCCreateOrder.__dict__.keys() if i[0] != '_']}
        order_detail = {k: v for k, v in request.form.items() if
                        k in [i for i in SFCOrderDetail.__dict__.keys() if i[0] != '_']}
        res = sfcapi.create_order(p_order_info=order_info, p_order_detail=order_detail)
        form_order = SFCCreateOrder(MultiDict(order_info))
        form_order_detail = SFCOrderDetail(MultiDict(order_detail))
    else:
        form_order = SFCCreateASN()
    return render_template('create_order.html', form_master=form_order, form_detail=form_order_detail, res=res)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
