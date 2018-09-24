# sample_doctest.py
# Using unit tests included in docstrings 

def pow_of_two(x):
    """Return x to the power of 2.

    >>> pow_of_two(4)
    16
    >>> pow_of_two(-2)
    4
    """
    return x**2

def float_div_by_two(x):
    """Return x divided by 2 in floating point precision.

    >>> float_div_by_two(49)
    24.5
    >>> float_div_by_two(48)
    24.0
    """
    return x / 2.0

def get_evens(n):
    """Return the first n even numbers as a list.
    >>> get_evens(4)
    [2, 4]
    """
    new_lis = []
    for i in range(1,n+1):
        if i%2 == 0:
            new_lis.append(i)
    return new_lis[0:n]

def get_mid(data):
    """Return the midpoint value in data.
    >>> get_mid([1,2,3,4,5])
    3
    """
    lis_size = len(data) 

    return data[lis_size/2]

def get_last_half(data):
    """Return the values in the last half of data (slice) as a list.
    >>> get_last_half([1,2,3,4,5])
    [3, 4, 5]
    """

    return  data[get_mid(data)-1:]




