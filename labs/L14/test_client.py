#!/usr/bin/python3

from client import approximate_size

def test_1000():
    assert approximate_size(1000000000000) == "1.0 TB"

def test_1024():
    assert approximate_size(1000000000000,True) == "931.3 GiB"

def test_4000_case1():
    assert approximate_size(4000,a_kilobyte_is_1024_bytes=False) == "4.0 KB"

def test_4000_case2():
    assert approximate_size(size =4000) == "4.0 KB"

def test_reverseOrder():
    assert approximate_size(a_kilobyte_is_1024_bytes=False, size=4000) == "4.0 KB"


def test_doc(): 
    assert approximate_size.__doc__ != None