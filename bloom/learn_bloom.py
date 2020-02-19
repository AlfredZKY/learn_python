import pybloom_live
from pybloom_live import BloomFilter

Built_in_properties = ['BloomFilter', 'ScalableBloomFilter', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'pybloom', 'utils']
f = BloomFilter(capacity=1000,error_rate=0.001)
def print_properity():
    print(dir(pybloom_live.BloomFilter))

def test_bloom1():
    # 容量，能容忍的误报率
    print(f.add('Traim304'))

def test_bloom2():
    # 容量，能容忍的误报率
    
    print( 'Traim304' in f)

if __name__ == '__main__':
    test_bloom1()
    test_bloom2()
    print_properity()

