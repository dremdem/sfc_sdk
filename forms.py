#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FLask WTFForms for testing SFCAPI
"""

from flask_wtf import FlaskForm

from wtforms import StringField, IntegerField, validators, FloatField


class SFCCreateProduct(FlaskForm):
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


class SFCCreateOrder(FlaskForm):
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


class SFCOrderDetail(FlaskForm):
    sku = StringField('Product ID', [validators.DataRequired(), validators.Length(max=16)])
    quantity = IntegerField('Quantity', [validators.DataRequired()])
    isQC = IntegerField('isQC')
    priorityLevel = IntegerField('priorityLevel')
    opDescription = StringField('Product Description', [validators.DataRequired(), validators.Length(max=200)])
    cnDescription = StringField('Product Chinese Description', [validators.DataRequired(), validators.Length(max=200)])
    supplierCode = StringField('supplierCode')
    unitPrice = StringField('unitPrice')
    barCode = StringField('barCode')


