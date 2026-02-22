"""
ETCCDS202 - Data Structures
Unit 1 Experiment 2: Time Complexity Analysis

Single Loop -> O(n)
Nested Loop -> O(n^2)
Halving Loop -> O(log n)
"""

# ---------------------------
# O(n) Example
# ---------------------------
def linear_loop(n):
    for i in range(n):
        print(i, end=" ")
    print()


# ---------------------------
# O(n^2) Example
# ---------------------------
def nested_loop(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


# ---------------------------
# O(log n) Example
# ---------------------------
def halving_loop(n):
    while n > 0:
        print(n, end=" ")
        n = n // 2
    print()


# -------- Main Program --------
if __name__ == "__main__":
    num = int(input("Enter a number: "))

    print("\nO(n) Example:")
    linear_loop(num)

    print("\nO(n^2) Example:")
    nested_loop(num)

    print("\nO(log n) Example:")
    halving_loop(num)