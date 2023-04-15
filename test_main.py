#This file is for the individual unit tests
import functions

def test_multiplyFunc():
    assert main.multiplyFunc(0,1) == 0
    assert main.multiplyFunc(1,2) == 2
    assert main.multiplyFunc(125,0.45) == 56.25
    assert main.multiplyFunc(5,7) == 35
    assert main.multiplyFunc(7,10) == 70
    
def test_convertHeight():
    assert main.convertHeight(63) == 1.575
    assert main.convertHeight(55) == 1.375
    assert main.convertHeight(71) == 1.775
    assert main.convertHeight(87) == 2.175
    assert main.convertHeight(67) == 1.675

def test_squareFunc():
    assert main.squareFunc(1.575) == 2.480625
    assert main.squareFunc(1.375) == 1.890625
    assert main.squareFunc(1.775) == 3.150625
    assert main.squareFunc(2.175) == 4.730625
    assert main.squareFunc(5) == 25

def test_divideFunc():
    assert main.divideFunc(56.25, 2.480625) == 22.7
    assert main.divideFunc(50, 10) == 5
    assert main.divideFunc(4, 2) == 2
    assert main.divideFunc(10, 2) == 5
    assert main.divideFunc(21, 7) == 3
    
def test_getBMI():
    assert main.getBMI(125, 63) == 22.7
    assert main.getBMI(155, 65) == 26.4

def test_categorizeBMI():
    assert main.categorizeBMI(15) == 'underweight'
    assert main.categorizeBMI(19) == 'normal weight'
    assert main.categorizeBMI(28) == 'overweight'
    assert main.categorizeBMI(32) == 'obese'
    
def test_categorizeBMIboundaries():
    assert main.categorizeBMI(16) == 'underweight' #Exterior
    assert main.categorizeBMI(18.4) == 'underweight' #On
    assert main.categorizeBMI(18.5) == 'normal weight' #Off
    assert main.categorizeBMI(21) == 'normal weight' #Interior
    assert main.categorizeBMI(24.9) == 'normal weight' #On
    assert main.categorizeBMI(25) == 'overweight' #Off
    assert main.categorizeBMI(27) == 'overweight' #Interior
    assert main.categorizeBMI(29.9) == 'overweight' #Off
    assert main.categorizeBMI(30) == 'obese' #On
    assert main.categorizeBMI(32) == 'obese' #Exterior

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