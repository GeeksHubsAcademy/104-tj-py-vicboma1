import pytest
import unittest   # The test framework

from kata import apply

class Test_kata(unittest.TestCase):
    
    def test_apply_01 (self):
        expected = False
        result = apply(None);
        assert(expected, result);
  
    def test_apply_02 (self):
        expected = False
        result = apply("");
        assert(expected == result)

    def test_apply_03 (self):
        expected = False
        result = apply("44878956X");
        assert(expected == result)

    def test_apply_04 (self):
        expected = False
        result = apply("44878956x");
        assert(expected == result)
 
    def test_apply_05 (self):
        expected = False
        result = apply("0000000");
        assert(expected == result)

    def test_apply_06 (self):
        expected = False
        result = apply("X0000000");
        assert(expected == result)

    def test_apply_07 (self):
        expected = False
        result = apply("000X0000");
        assert(expected == result)
 
    def test_apply_08 (self):
        expected = False
        result = apply("00000000s");
        assert(expected == result)
 
    def test_apply_09 (self):
        expected = False
        result = apply("03200000s");
        assert(expected == result)

    def test_apply_10 (self):
        expected = False
        result = apply("0320000Ss");
        assert(expected == result)
 
    def test_apply_11 (self):
        expected = False
        result = apply("S");
        assert(expected == result)
 
    def test_apply_12 (self):
        expected = False
        result = apply("s");
        assert(expected == result)
 
    def test_apply_13 (self):
        expected = False
        result = apply("000c0000");
        assert(expected == result)
 
    def test_apply_14 (self):
        expected= True;
        result = apply("68741024G");
        assert(expected == result)
 
    def test_apply_15 (self):
        expected= True;
        result = apply("96731267Y");
        assert(expected == result)
 
    def test_apply_16 (self):
        expected= True;
        result = apply("65973775T");
        assert(expected == result)
 
    def test_apply_17 (self):
        expected= True;
        result = apply("01893995Z");
        assert(expected == result)
 
    def test_apply_18 (self):
        expected= True;
        result = apply("12322160W");
        assert(expected == result)
 
    def test_apply_19 (self):
        expected= True;
        result = apply("55491653J");
        assert(expected == result)
 
    def test_apply_20 (self):
        expected = False
        result = apply("55491653Ñ");
        assert(expected == result)
 

if __name__ == '__main__':
	unittest.main()