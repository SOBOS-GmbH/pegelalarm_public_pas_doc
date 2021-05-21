# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 15:52:42 2018
Modified on Thu May 20 14:50:12 2021

@author: strasjoh
"""

import hmac
import hashlib
import base64


class AuthTokenGenerator(object):

    def calcXAuthToken(self, username, api_key):
        hmac_string = self.__createHMAC(username, api_key)

        api_key_byte_arr = api_key.encode("utf-8")
        api_key_encoded_base64_byte_arr = base64.b64encode(api_key_byte_arr)  # encode byte array as base64 byte array
        api_key_encoded_base64_string = api_key_encoded_base64_byte_arr.decode()

        return api_key_encoded_base64_string + "." + hmac_string

    def __createHMAC(self, message, secret):
        dig = hmac.new(secret.encode("utf-8"),
                       msg=message.encode("utf-8"),
                       digestmod=hashlib.sha256).digest()
        hmac_encoded_base64_byte_arr = base64.b64encode(dig)  # encode byte array as base64 byte array
        hmac_string = hmac_encoded_base64_byte_arr.decode()  # convert byte array to string
        return hmac_string
