# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:06:41 2020

@author: roger luo
"""

import pytest
from projectlibxx.pkg1 import mod2
import imblearn
import pandas 
import numpy 



# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4
    


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()

# content of test_class_demo.py
class TestClassDemoInstance:
    def test_one(self):
        assert 1

    def test_two(self):
        assert 1

        
# content of test_tmpdir.py
def test_needsfiles(tmpdir):
    print(tmpdir)
    assert 1
    