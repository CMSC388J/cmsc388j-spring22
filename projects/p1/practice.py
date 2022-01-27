def hello_world():
    """ Returns 'Hello, World!'

    Arguments:
    None

    Usage:
    >>> hello_world()
    'Hello, World!'
    """
    raise NotImplementedError('Please implement this function for full credit')


def sum_unique(l):
    """ Sums values in l, not counting duplicates.

    Arguments:
    l -- a list of integers

    Usage:
    >>> sum_unique([])
    0
    >>> sum_unique([4, 4, 5])
    9
    >>> sum_unique([4, 2, 5])
    11
    >>> sum_unique([2, 2, 2, 2, 1])
    3
    """
    raise NotImplementedError('Please implement this function for full credit')


def palindrome(x):
    """ Determines if x, an integer or string, is a palindrome, i.e.
    has the same value reversed.

    Arguments:
    x -- an integer or string

    Usage:
    >>> palindrome(1331)
    True
    >>> palindrome('racecar')
    True
    >>> palindrome(1234)
    False
    >>> palindrome('python')
    False
    """
    raise NotImplementedError('Please implement this function for full credit')


def sum_multiples(num):
    """ Sums up all multiples of 3 and 5 upto and not including num.

    Arguments:
    num -- a positive integer

    Usage:
    >>> sum_multiples(10) # Multiples: [3, 5, 6, 9]
    23
    >>> sum_multiples(3) # Multiples: []
    0
    >>> sum_multiples(5) # Multiples: [3]
    3
    >>> sum_multiples(16) # Multiples: [3, 5, 6, 9, 10, 12, 15]
    60
    """
    raise NotImplementedError('Please implement this function for full credit')


def num_func_mapper(nums, funs):
    """Applies each function in funs to the list of numbers, nums, and
    returns a list consisting of the results of those functions. 

    Arguments:
    nums -- a sequence of numbers
    funs -- a sequence of functions
          - each function in funs acts on a sequence of numbers and returns a number

    Usage:
    >>> f_list = [sum_unique, sum]
    >>> num_list = [2, 2, 2, 4, 5]
    >>> num_func_mapper(num_list, f_list)
    [11, 15]
    """
    raise NotImplementedError('Please implement this function for full credit')


def validate_grid_indices(grid_indices, grid_size):
    """This problem is taken from an open-source LIDAR occupancy grid
    visualization project (not released, yet, though).
    Given a sequence of sequences of numbers `grid_indices` and
    an integer `grid_size`, validate that `grid_indices` satisfies
    these three conditions, and throw a ValueError with the specified
    error message if a certain condition is violated. Return nothing
    if the validation is successful.
    
    1. The length of `grid_indices` must be 1, 2, or 3.
        Error message on failure: "Length of grid_indices is wrong."
    2. The length of each sequence in `grid_indices` must be 2.
        Error message on failure: "Sub-sequences must be length 2."
    3. For each sub-sequence in `grid_indices`, the difference 
    between the second item and the first item must be equal to `grid_size`.
        Error message on failure: "Grid indexes do not match grid_size."

    Arguments:
    grid_indices -- A sequence of sequences of numbers
    grid_size -- An integer

    Usage:
    >>> validate_grid_indices((1, 3), 2)
    >>> validate_grid_indices((3, 73),
            (73, 143),
            (143, 213),), 70)
    """
    raise NotImplementedError('Please implement this function for full credit')


def pythagorean_triples(n):
    """ Finds all pythagorean triples where a, b, and c (sides of the triangle)
    are all less than n units long. This function should not return distinct tuples
    that still represent the same triangle. For example, (3, 4, 5) and (4, 3, 5)
    are both valid pythagorean triples, but only the first should be in the final list.

    The tuple elements should be sorted in ascending order, and the
    list of tuples should be sorted in ascending order by the last element of the tuple.

    Arguments:
    n -- a positive integer

    Usage:
    >>> pythagorean_triples(10)
    [(3, 4, 5)]
    >>> pythagorean_triples(11)
    [(3, 4, 5), (6, 8, 10)]
    >>> pythagorean_triples(20)
    [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17)]
    """
    raise NotImplementedError('Please implement this function for full credit')
