#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Testing module from creating product using 
http://www.sendfromchina.com/default/index/webservice


"""

from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect

from werkzeug.datastructures import MultiDict

from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, validators, FloatField


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


class CreateOrder(FlaskForm):
    referenceNo = StringField(u'User’s Reference Number', [validators.DataRequired(), validators.Length(max=32)])
    warehouseId = IntegerField('Warehouse ID. Default is 1. Refer to getWarehouse for details')
    consigneeFirstName = StringField('Recipient First Name', [validators.DataRequired(), validators.Length(max=32)])
    consigneeLastName = StringField('Recipient Last Name', [validators.DataRequired(), validators.Length(max=32)])
    consigneeCompany = StringField('Recipient Company', [validators.Length(max=128)])
    consigneeCountry = StringField('Country', [validators.DataRequired(), validators.Length(max=128)])
    shippingMethodCode = StringField('Shipping Method Code', [validators.DataRequired(), validators.Length(max=16)])
    consigneeZip = StringField('Postal Code', [validators.DataRequired(), validators.Length(max=16)])
    consigneeCity = StringField('City', [validators.Length(max=64)])
    consigneeState = StringField('State', [validators.Length(max=64)])
    consigneeAddress1 = StringField('Address Line 1', [validators.DataRequired(), validators.Length(max=128)])
    consigneeAddress2 = StringField('Address Line 2', [validators.Length(max=128)])
    consigneePhone = StringField('Recipient Telephone', [validators.Length(max=16)])
    consigneeEmail = StringField('Recipient Email', [validators.Length(max=64)])
    orderStatu = IntegerField('Order Status: 0 = Deleted; 1 = Draft; 2 = Pending Submit; 3 = Processing')
    instructions = StringField('Order Remarks', [validators.Length(max=50)])
    returnable = IntegerField('Return if Undeliverable? 0 = No; 1 = Yes', [validators.DataRequired()])
    evaluate = FloatField('Insured Value')
    taxesNumber = StringField(u'Recipient’s Tax ID', [validators.Length(max=50)])
    isRemoteConfirm = IntegerField('Agree to pay Remote Area Surcharge? 0=No; 1=Yes')
    payBy = IntegerField('Pay By 0=Receiver; 1=Sender (For domestic order only)')


class OrderDetail(FlaskForm):
    sku = StringField('Product ID', [validators.DataRequired(), validators.Length(max=16)])
    quantity = IntegerField('Quantity', [validators.DataRequired()])
    isQC = IntegerField('isQC')
    priorityLevel = IntegerField('priorityLevel')
    opDescription = StringField('Product Description', [validators.DataRequired(), validators.Length(max=200)])
    cnDescription = StringField('Product Chinese Description', [validators.DataRequired(), validators.Length(max=200)])
    supplierCode = StringField('supplierCode')
    unitPrice = StringField('unitPrice')
    barCode = StringField('barCode')


app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)
app.secret_key = 's3cr3tasdasdasdasd'
import zeep

wsdl = 'http://fulfill.sendfromchina.com/default/svc/wsdl'

client = zeep.Client(wsdl=wsdl)

req = {'HeaderRequest': {'customerId': 'R2036',
                         'appToken': 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDK1YNcdunmWXoK1ys6hyi+LWQdPx6Vmr/9kNlKOw4cK5Q8FWA3nfGeeG49Pq2TlYKVLdSw1fr60AAJFQOuXmol6lmyn+/xwx6j21XLx9/4vdDNSTR8Hcp7oqGNNr5DlI0onhJ7sd+rAxhIOwLNnZv6T/XtVqQNuGVXTq/dX0zkaQIDAQAB',
                         'appKey': 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDGmDLbsI4jELqCHgWikWqACICp299WSoiWgqghEXkQfvdEvwS5XWpdsSmdQwryR2rtg0DiS3vf74oVYBDJVHgcUdc2ov7QI5TPBqXJped7OoyrqYzaYFYshzGWgYC0wu5RCb71p2+4Z8NwDoJlvMVU4/fD9pL59PW8yYH1u3x4ewIDAQAB'}}


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
        res = client.service.createProduct(HeaderRequest=req['HeaderRequest'], ProductInfo=product_info)
        form = CreateProduct(request.form)
    else:
        form = CreateProduct()
    return render_template('create_product.html', form=form, res=res)


@app.route("/create_order", methods=['GET', 'POST'])
def create_order():
    res = None
    if request.method == 'POST':
        order_info = {k: v for k, v in request.form.items() if k in
                      [i for i in CreateOrder.__dict__.keys() if i[0] != '_']}
        factory = client.type_factory('ns0')
        order_detail = {k: v for k, v in request.form.items() if
                        k in [i for i in OrderDetail.__dict__.keys() if i[0] != '_']}
        f_order_detail = factory.orderDetail(_value_1=[order_detail])
        order_info['orderDetail'] = f_order_detail
        res = client.service.createOrder(HeaderRequest=req['HeaderRequest'], orderInfo=order_info)
        form_order = CreateOrder(MultiDict(order_info))
        form_order_detail = OrderDetail(MultiDict(order_detail))
    else:
        form_order = CreateOrder()
        form_order_detail = OrderDetail()
    return render_template('create_order.html', form_master=form_order, form_detail=form_order_detail, res=res)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
