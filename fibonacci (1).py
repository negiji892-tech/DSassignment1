"""
ETCCDS202 - Data Structures
Unit 1 Assignment
Program 2: Fibonacci (Naive + Memoized)

Naive Time Complexity: O(2^n)
Naive Space Complexity: O(n)

Memoized Time Complexity: O(n)
Memoized Space Complexity: O(n)
"""

# -------------------------------
# Naive Recursive Fibonacci
# -------------------------------
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# -------------------------------
# Memoized Fibonacci
# -------------------------------
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
        
    if n in memo:
        return memo[n]
        
    if n <= 1:
        return n
        
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# -------- Main Program --------
if __name__ == "__main__":
    try:
        num = int(input("Enter a non-negative integer: "))
        
        if num < 0:
            print("Invalid Input! Please enter a non-negative number.")
        else:
            print(f"\nNaive Fibonacci of {num}: {fib_naive(num)}")
            print(f"Memoized Fibonacci of {num}: {fib_memo(num)}")
    
    except ValueError:
        print("Invalid Input! Please enter a valid integer.")