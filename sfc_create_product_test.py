#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Testing module from creating product using 
http://www.sendfromchina.com/default/index/webservice


"""

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField


class CreateProduct(FlaskForm):
    sku = StringField('sku')
    skuName = StringField('skuName')
    skuCNName = StringField('skuCNName')
    weight = IntegerField('weight')
    length = IntegerField('length')
    width = IntegerField('width')
    height = IntegerField('height')
    declareValue = IntegerField('declareValue')
    minQty = IntegerField('minQty')
    package = StringField('package')
    imgUrl = StringField('imgUrl')
    pocId = StringField('pocId')
    poValue = StringField('poValue')
    hsCode = StringField('hsCode')
    productDescription = StringField('productDescription')
    withbattery = StringField('withbattery')
    opOrigin = StringField('opOrigin')
    enMaterial = StringField('enMaterial')
    cnMaterial = StringField('cnMaterial')
    productPackectType = StringField('productPackectType')
    productUsage = StringField('productUsage')
    productLabel = StringField('productLabel')
    labelId = StringField('labelId')
    productBrand = StringField('productBrand')
    productBrandName = StringField('productBrandName')


app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)
app.secret_key = 's3cr3tasdasdasdasd'
import zeep

wsdl = 'http://fulfill.sendfromchina.com/default/svc/wsdl'

client = zeep.Client(wsdl=wsdl)

req = {'HeaderRequest': {'customerId': 'R2036',
                         'appToken': 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDK1YNcdunmWXoK1ys6hyi+LWQdPx6Vmr/9kNlKOw4cK5Q8FWA3nfGeeG49Pq2TlYKVLdSw1fr60AAJFQOuXmol6lmyn+/xwx6j21XLx9/4vdDNSTR8Hcp7oqGNNr5DlI0onhJ7sd+rAxhIOwLNnZv6T/XtVqQNuGVXTq/dX0zkaQIDAQAB',
                         'appKey': 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDGmDLbsI4jELqCHgWikWqACICp299WSoiWgqghEXkQfvdEvwS5XWpdsSmdQwryR2rtg0DiS3vf74oVYBDJVHgcUdc2ov7QI5TPBqXJped7OoyrqYzaYFYshzGWgYC0wu5RCb71p2+4Z8NwDoJlvMVU4/fD9pL59PW8yYH1u3x4ewIDAQAB' }}


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/create_product", methods=['GET', 'POST'])
def create_product():
    if request.method == 'POST':
        product_info = {k: v for k, v in request.form.items() if k not in ('csrf_token', 'pocId', 'poValue', 'imgUrl')}
        product_info['image'] = {'imgUrl': request.form['imgUrl']}
        product_info['qcs'] = {'pocId': request.form['pocId'], 'poValue': request.form['poValue']}
        res = client.service.createProduct(HeaderRequest=req['HeaderRequest'], ProductInfo=product_info)
        form = request.form
    else:
        form = CreateProduct()
    return render_template('create_product.html', form=form)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)





