# P1: Python practice 

**Assigned**: Week 1, January 27th, 2022

**Due**: Week 2, February 1st, 2021 11:59PM

**Late deadline**: Friday, February 4th 11:59PM

## Description

You will be implementing some basic functions in Python as practice, including using iterators and built-in functions.

## Setup

Make sure Python 3.9 (or higher) is installed on your computer.

You should work on this project (and the other projects in this course) in a virtual environment.
Navigate to the root of a directory you will use for this class. You should use the same environment
for all projects in this course; you don't need more than one.
To create and activate one, enter the following commands in your terminal:

> Tip: You can clone the whole repo (`cmsc388j-spring22`) and use that as your root directory for this class. Then, you can just run `git pull` to get new projects.

For Mac/Linux:
```bash
$ python3 -m venv venv        # creates environment
$ source ./venv/bin/activate  # enters environment
```

For Windows:
```bash
$ py -m venv venv             # creates environment
$ ./venv/Scripts/activate     # enters environment
```

These instructions can also be found in the Week 1 slides.

Testing this project with our public tests requires a package called `pytest`.
To install it, run either of the following in your terminal while in your virtual environment:
```bash    
$ pip3 install -r requirements.txt
```
```bash
$ pip3 install pytest
```
Again, you **must** be in your virtual environment when installing packages with pip.

## Project

In `practice.py`, implement the following functions:

1. `hello_world()`

   Return the string `Hello, World!`

2. `sum_unique(l)`

   Given a sequence of integers, return the sum of the integers, not counting duplicates, i.e. 
   if you have two or more copies of an integer, it should be added to the final sum once.

   Examples:
   ```python
   >>> sum_unique([])
   0
   >>> sum_unique([4, 4, 5])
   9
   >>> sum_unique([4, 2, 5])
   11
   >>> sum_unique([2, 2, 2, 2, 1])
   3
   ```

3. `palindrome(x)`

    Given an integer or a string *x*, determine if *x* has the same value as *x* reversed.

    Examples:
    ```python
    >>> palindrome(1331)
    True
    >>> palindrome('racecar')
    True
    >>> palindrome(1234)
    False
    >>> palindrome('python')
    False
    ```

4. `sum_multiples(num)`

    Given a positive integer `num`, find the sum of all multiples of 3 and 5 upto and not including `num`.

    Examples:
    ```python
    >>> sum_multiples(10) # Multiples: [3, 5, 6, 9]
    23
    >>> sum_multiples(3) # Multiples: []
    0
    >>> sum_multiples(5) # Multiples: [3]
    3
    >>> sum_multiples(16) # Multiples: [3, 5, 6, 9, 10, 12, 15]
    60
    ```

5. `num_func_mapper(nums, funs)`

    Given a sequence of numbers `nums` and a sequence of functions `funs`, 
    apply each function to `nums` and store the result in a list.
    Return the list of results. 
    
    *Hint*: The list of results should be the same length as `funs`.

    Example:
    ```python
    >>> f_list = [sum_unique, sum]
    >>> num_list = [2, 2, 2, 4, 5]
    >>> num_func_mapper(num_list, f_list)
    [11, 15]
    ```

6. `validate_grid_indices(grid_indices, grid_size)`

    This problem is taken from an open-source LIDAR occupancy grid
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

    Example:
    ```python
    >>> validate_grid_indices((1, 3), 2)
    >>> validate_grid_indices((3, 73),
            (73, 143),
            (143, 213),), 70)
    ```
    NOTE: these inputs will not output anything

7. `pythagorean_triples(n)`

    Finds all pythagorean triples where `a`, `b`, and `c` (side lengths of a triangle)
    are all less than `n` units long. This function should not return distinct tuples
    that still represent the same triangle. For example, (3, 4, 5) and (4, 3, 5)
    are both valid pythagorean triples, but **only the first** should be in the final list.

    The tuple elements should be sorted in ascending order, and the
    list of tuples should be sorted in ascending order by the last element of the tuple.

    Examples:
    ```python
    >>> pythagorean_triples(10)
    [(3, 4, 5)]
    >>> pythagorean_triples(11)
    [(3, 4, 5), (6, 8, 10)]
    >>> pythagorean_triples(20)
    [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17)]
    ```

## Testing

Navigate into the `p1/` directory and run the command `pytest`.
You should see your test results in the terminal.

## Submission & Grading

Compress a `p1` directory into a .zip file containing `practice.py` and `test_practice.py`
and submit it on ELMS after testing thoroughly; all of your work should be in this module.

There are 16 public tests, and each will be worth 10 points.
If your submission doesn't have the `practice.py` and `test_practice.py` files, 
20 points will be deducted from your score.
Do not include your virtual environment in your submission.
Doing so will result in a deduction of 20 points.
