#This file is for the individual unit tests
import functions

def test_multiplyFunc():
    assert functions.multiplyFunc(0,1) == 0
    assert functions.multiplyFunc(1,2) == 2
    assert functions.multiplyFunc(125,0.45) == 56.25
    assert functions.multiplyFunc(5,7) == 35
    assert functions.multiplyFunc(7,10) == 70
    
def test_convertHeight():
    assert functions.convertHeight(63) == 1.575
    assert functions.convertHeight(55) == 1.375
    assert functions.convertHeight(71) == 1.775
    assert functions.convertHeight(87) == 2.175
    assert functions.convertHeight(67) == 1.675

def test_squareFunc():
    assert functions.squareFunc(1.575) == 2.480625
    assert functions.squareFunc(1.375) == 1.890625
    assert functions.squareFunc(1.775) == 3.150625
    assert functions.squareFunc(2.175) == 4.730625
    assert functions.squareFunc(5) == 25

def test_divideFunc():
    assert functions.divideFunc(56.25, 2.480625) == 22.7
    assert functions.divideFunc(50, 10) == 5
    assert functions.divideFunc(4, 2) == 2
    assert functions.divideFunc(10, 2) == 5
    assert functions.divideFunc(21, 7) == 3
    
def test_getBMI():
    assert functions.getBMI(125, 63) == 22.7
    assert functions.getBMI(155, 65) == 26.4

def test_categorizeBMI():
    assert functions.categorizeBMI(15) == 'underweight'
    assert functions.categorizeBMI(19) == 'normal weight'
    assert functions.categorizeBMI(28) == 'overweight'
    assert functions.categorizeBMI(32) == 'obese'
    
def test_categorizeBMIboundaries():
    assert functions.categorizeBMI(16) == 'underweight' #Exterior
    assert functions.categorizeBMI(18.4) == 'underweight' #On
    assert functions.categorizeBMI(18.5) == 'normal weight' #Off
    assert functions.categorizeBMI(21) == 'normal weight' #Interior
    assert functions.categorizeBMI(24.9) == 'normal weight' #On
    assert functions.categorizeBMI(25) == 'overweight' #Off
    assert functions.categorizeBMI(27) == 'overweight' #Interior
    assert functions.categorizeBMI(29.9) == 'overweight' #Off
    assert functions.categorizeBMI(30) == 'obese' #On
    assert functions.categorizeBMI(32) == 'obese' #Exterior

if __name__ == '__main__':
    print("test_main.py: running unit tests")
    test_multiplyFunc()
    test_convertHeight()
    test_squareFunc()
    test_divideFunc()
    test_getBMI()
    test_categorizeBMI()
    test_categorizeBMIboundaries()
    print("test_main.py: all tests passed. ")