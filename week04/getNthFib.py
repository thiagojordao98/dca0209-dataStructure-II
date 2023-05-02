def getNthFib(n, memoize={1: 0, 2: 1}):
    """
  This function returns the nth number in the Fibonacci sequence, 
  where the first two numbers are 0 and 1, and each subsequent number
  is the sum of the two preceding numbers.

  Parameters:
  n (int): the position of the desired number in the Fibonacci sequence (1-based indexing)

  Returns:
  int: the nth number in the Fibonacci sequence

  Example:
  >>> getNthFib(6)
  5
  """
    if n in memoize:
        return memoize[n]

    else:
        memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
        print(memoize)
        return memoize[n]


print(getNthFib(5))
