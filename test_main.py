#This file is for the individual unit tests
import functions

def test_multiplyFunc():
    assert multiplyFunc(0,1) == 0
    assert multiplyFunc(1,2) == 2
    assert multiplyFunc(125,0.45) == 56.25
    assert multiplyFunc(5,7) == 35
    assert multiplyFunc(7,10) == 70
    
def test_convertHeight():
    assert convertHeight(63) == 1.575
    assert convertHeight(55) == 1.375
    assert convertHeight(71) == 1.775
    assert convertHeight(87) == 2.175
    assert convertHeight(67) == 1.675

def test_squareFunc():
    assert squareFunc(1.575) == 2.480625
    assert squareFunc(1.375) == 1.890625
    assert squareFunc(1.775) == 3.150625
    assert squareFunc(2.175) == 4.730625
    assert squareFunc(5) == 25

def test_divideFunc():
    assert divideFunc(56.25, 2.480625) == 22.7
    assert divideFunc(50, 10) == 5
    assert divideFunc(4, 2) == 2
    assert divideFunc(10, 2) == 5
    assert divideFunc(21, 7) == 3
    
def test_getBMI():
    assert getBMI(125, 63) == 22.7
    assert getBMI(155, 65) == 26.4

def test_categorizeBMI():
    assert categorizeBMI(15) == 'underweight'
    assert categorizeBMI(19) == 'normal weight'
    assert categorizeBMI(28) == 'overweight'
    assert categorizeBMI(32) == 'obese'
    
def test_categorizeBMIboundaries():
    assert categorizeBMI(16) == 'underweight' #Exterior
    assert categorizeBMI(18.4) == 'underweight' #On
    assert categorizeBMI(18.5) == 'normal weight' #Off
    assert categorizeBMI(21) == 'normal weight' #Interior
    assert categorizeBMI(24.9) == 'normal weight' #On
    assert categorizeBMI(25) == 'overweight' #Off
    assert categorizeBMI(27) == 'overweight' #Interior
    assert categorizeBMI(29.9) == 'overweight' #Off
    assert categorizeBMI(30) == 'obese' #On
    assert categorizeBMI(32) == 'obese' #Exterior

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