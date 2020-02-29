# Optimize fibbonaci through the ram
import time
import sys

def recursive_fibonacci(n):
    """Return a result of recursive fibonacci"""
    if n == 0 or n == 1:
        return 1
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def dynamic_fibonacci(n, memo = {}):
    """Return a result of dynamic fibonacci, this use ram for optimize"""
    if n == 0  or  n == 1:
        return 1
    try:
        return memo[n]
    except KeyError as ke:
        result = dynamic_fibonacci(n -1, memo) + dynamic_fibonacci(n - 2, memo)
        memo[n] = result
        return result

if __name__=="__main__":
    n = int(input('Choice a number:'))
    recursive_result = int(input(
"""Do you want the result of recursive_fibonacci?
(This algorithm can damage your PC, when you enter large numbers(>50))
no:0
yes:1
"""
    ))
    if recursive_result:
        tic_rf = time.process_time()
        res_rf = recursive_fibonacci(n)
        toc_rf = time.process_time()

        print('Recursive Fibonacci: \tindex {} \tresult {} \tprocess time {}ms'.format(n, res_rf, (toc_rf - tic_rf) * 1000))
    
    tic_df = time.process_time()
    res_df = dynamic_fibonacci(n)
    toc_df = time.process_time()

    print('Dynamic Fibonacci: \tindex {} \tresult {} \tprocess time {}ms'.format(n, res_df, (toc_df - tic_df) * 1000))
    

