from __future__ import print_function
import sys
import os
import string
import ctypes

from rsa_class import RsaClass

def generate_keys():
    private_key = RsaClass.generate_pri()
    public_key = RsaClass.generate_pub(private_key)
    RsaClass.save_pri("./rsapri.pem", private_key)
    RsaClass.save_pub("./rsapub.pem", public_key)

if __name__ == "__main__":
    generate_keys()
