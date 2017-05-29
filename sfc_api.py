#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SFC API interface

This is SDK for handle SOAP API SendFromChina, warehousing provider. 
http://www.sendfromchina.com/default/index/webservice
"""
import zeep


class SFCAPI(object):
    """
    Main SFCAPI class
    """

    def __init__(self, p_wsdl, p_header_request):
        """
        :param p_wsdl: SOAP wsdl URL
        :param p_header_request: dict with customerId, appToken and appKey 
        """
        self.header_request = p_header_request
        self.wsdl = p_wsdl

        # init connection to SFC SOAP
        self.client = zeep.Client(wsdl=self.wsdl)

        # type factory init
        self.factory = self.client.type_factory('ns0')

    def create_product(self, p_product_info):
        """
        Creating product, API function createProduct
        
        :param p_product_info:        
        :return: API result
        """
        return self.client.service.createProduct(HeaderRequest=self.header_request, ProductInfo=p_product_info)

    def create_order(self, p_order_info, p_order_detail):
        """
        Creating order, API function createOrder
        
        :param p_order_info: 
        :param p_order_detail: 
        :return: 
        """
        order_info = p_order_info
        order_detail = self.factory.orderDetail(_value_1=p_order_detail)
        order_info['orderDetail'] = order_detail
        return self.client.service.createOrder(HeaderRequest=self.header_request, orderInfo=order_info)

    def get_shipping_methods(self):
        """
        Get shipping method list
        :return: 
        """

        return self.client.service.getShippingMethod(HeaderRequest=self.header_request)

    def get_countries(self):
        """
        Get country list         
        :return: 
        """

        return self.client.service.getCountry(HeaderRequest=self.header_request)

    def get_warehouses(self):
        """
        Get warehouses list
        :return: 
        """

        return self.client.service.getWarehouse(HeaderRequest=self.header_request)

    def create_asn(self, asn_info):
        """
        create ASN
        :param asn_info: 
        :return: 
        """

        return self.client.service.createASN(HeaderRequest=self.header_request, ASNInfo=asn_info)
