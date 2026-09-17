"""
CMPS 6610  Problem Set 2
See problemset-02.pdf for details.
"""
import time
import tabulate

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))

    # so that a BinaryNumber can be compared directly against an int
    # (e.g. quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 4)
    def __eq__(self, other):
        if isinstance(other, BinaryNumber):
            return self.decimal_val == other.decimal_val
        return self.decimal_val == other

    def __hash__(self):
        return hash(self.decimal_val)

    def __int__(self):
        return self.decimal_val
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

# some useful utility functions to manipulate bit vectors
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y
    
def quadratic_multiply(x, y):
    """
    "Grade school" divide and conquer multiplication.

    Writing x = a*2^(n/2) + b and y = c*2^(n/2) + d, we have
        x*y = ac*2^n + (ad + bc)*2^(n/2) + bd,
    which requires four recursive multiplications of half-size inputs
    plus O(n) work to shift and add:
        W(n) = 4W(n/2) + O(n)  ==>  W(n) in Theta(n^2).

    Params:
      x......a BinaryNumber
      y......a BinaryNumber
    Returns:
      a BinaryNumber equal to x*y
    """
    # base case: a single bit is either 0 or 1, so the product is trivial
    if len(x.binary_vec) == 1 or len(y.binary_vec) == 1:
        return BinaryNumber(x.decimal_val * y.decimal_val)

    xvec, yvec = pad(x.binary_vec, y.binary_vec)
    n = len(xvec)
    a, b = split_number(xvec)
    c, d = split_number(yvec)

    ac = quadratic_multiply(a, c)
    ad = quadratic_multiply(a, d)
    bc = quadratic_multiply(b, c)
    bd = quadratic_multiply(b, d)

    return BinaryNumber(bit_shift(ac, n).decimal_val +
                        bit_shift(ad, n // 2).decimal_val +
                        bit_shift(bc, n // 2).decimal_val +
                        bd.decimal_val)

def subquadratic_multiply(x, y):
    """
    Karatsuba-Ofman multiplication.

    With x = a*2^(n/2) + b and y = c*2^(n/2) + d, the middle term
    ad + bc can be recovered from a single extra multiplication:
        ad + bc = (a+b)(c+d) - ac - bd,
    so only three recursive multiplications are needed:
        W(n) = 3W(n/2) + O(n)  ==>  W(n) in Theta(n^(log_2 3)) ~ Theta(n^1.585).

    Params:
      x......a BinaryNumber
      y......a BinaryNumber
    Returns:
      a BinaryNumber equal to x*y
    """
    # base case: a single bit is either 0 or 1, so the product is trivial
    if len(x.binary_vec) == 1 or len(y.binary_vec) == 1:
        return BinaryNumber(x.decimal_val * y.decimal_val)

    xvec, yvec = pad(x.binary_vec, y.binary_vec)
    n = len(xvec)
    a, b = split_number(xvec)
    c, d = split_number(yvec)

    ac = subquadratic_multiply(a, c)
    bd = subquadratic_multiply(b, d)
    abcd = subquadratic_multiply(BinaryNumber(a.decimal_val + b.decimal_val),
                                 BinaryNumber(c.decimal_val + d.decimal_val))
    middle = BinaryNumber(abcd.decimal_val - ac.decimal_val - bd.decimal_val)

    return BinaryNumber(bit_shift(ac, n).decimal_val +
                        bit_shift(middle, n // 2).decimal_val +
                        bd.decimal_val)

## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2

def test_multiply_random():
    import random
    for _ in range(200):
        x = random.randint(0, 2**20)
        y = random.randint(0, 2**20)
        assert quadratic_multiply(BinaryNumber(x), BinaryNumber(y)) == x*y
        assert subquadratic_multiply(BinaryNumber(x), BinaryNumber(y)) == x*y

# some timing functions here that will make comparisons easy    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    f(x,y)
    return (time.time() - start)*1000
    
def compare_multiply():
    res = []
    for n in [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]:
        qtime = time_multiply(BinaryNumber(n), BinaryNumber(n), quadratic_multiply)
        subqtime = time_multiply(BinaryNumber(n), BinaryNumber(n), subquadratic_multiply)        
        res.append((n, qtime, subqtime))
    print_results(res)


def compare_multiply_bits(bit_sizes=(16, 32, 64, 128, 256, 512, 1024, 2048)):
    """
    The inputs used by compare_multiply() only range over ~4 to ~30 bits,
    which is far too narrow to see the asymptotic difference. Here we
    scale the *number of bits* n, which is the actual input size for
    these algorithms.
    """
    res = []
    for n in bit_sizes:
        x = BinaryNumber(2**n - 1)   # n ones: a worst-case-ish n-bit input
        y = BinaryNumber(2**n - 1)
        qtime = time_multiply(x, y, quadratic_multiply)
        subqtime = time_multiply(x, y, subquadratic_multiply)
        res.append((n, qtime, subqtime))
    print("\n")
    print(
        tabulate.tabulate(
            res,
            headers=['n (bits)', 'quadratic (ms)', 'subquadratic (ms)'],
            floatfmt=".3f",
            tablefmt="github"))
    return res


def print_results(results):
    print("\n")
    print(
        tabulate.tabulate(
            results,
            headers=['n', 'quadratic', 'subquadratic'],
            floatfmt=".3f",
            tablefmt="github"))
    
    
if __name__ == '__main__':
    compare_multiply()
    compare_multiply_bits()
