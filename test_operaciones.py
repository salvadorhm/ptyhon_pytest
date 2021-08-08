import pytest
import operaciones as op

def test_suma():
    assert op.suma(3,4) == 7
    assert op.suma(8,2) == 10

def test_rest():
    assert op.rest(3,4) == -1
    assert op.rest(8,2) == 6

def test_mult():
    assert op.mult(3,4) == 12
    assert op.mult(8,2) == 16

def test_div():
    assert op.div(3,4) == 0.75
    assert op.div(8,2) == 4
    assert op.div(10,0) == "Division entre 0"

def test_mayor3():
    assert op.mayor3(1,2,3) == 3
    assert op.mayor3(3,2,1) == 3
    assert op.mayor3(3,3,2) == 3
    assert op.mayor3(2,3,3) == 3
    assert op.mayor3(3,3,3) == 3
    assert op.mayor3(1,3,2) == 3
