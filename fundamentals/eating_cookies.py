'''
Input: an integer
Returns: an integer
'''
from itertools import combinations
from functools import lru_cache

@lru_cache(maxsize=500)
def eating_cookies(n, cache=None):
    # Your code here
    # brute force would be to use combinations
    # use a counter ? I think recursive would be good here
    # cookie breakdown:
        # all ones
        # if > 2
            # one 2, rest 1s
            #  if >3 , two 2s, rest 1s
    # Check the cache    
    # cache = {}
    # if n in cache:
    #     return cache[n]

    # # Compute the Nth term
    if n < 0:
        return
    elif n == 0:
        return 1 # apparently there is 1 way to eat 0 cookies using [1,2,3] cookies...
        # This actually means that there is a way to get to 0 cookies, from n
    elif n == 1 or n == 2:
        return n
    elif n == 3:
        return 4
    else:
        return (eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3))
    # cache[n] = value
    # return value

    # ok so a few things here. Recursion was best even though it was a little messy 
    # (better solved with an append to a list [1,1,2]), the logic there is fuzzy. 
    # Caching normally with a dict still didn't work for me for some reason. 
    # Using a decorator caused the test to hash by list, which is not possible. 
    # So I had to convert it to a tuple. 

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
