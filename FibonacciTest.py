import sys
from utils import sanitizeInputInt

# Somewhat fast fibonacci function
def computeFibonacci(n):
    a, b = 0, 1
    for i in range(2, n + 1):
        [a, b] = [a+b, a]
    return a

# Classic fibonacci function
def originalFibonacci(n):
    if n <= 2:
        return n - 1
    else:
        return originalFibonacci(n-1) + originalFibonacci(n-2)

WhichOne = sanitizeInputInt("Enter which one to use (1, 2): ", 1, 2)
N = sanitizeInputInt("Enter the number of terms to compute: ", 1)
# for i in range(1, N+1):
#   sys.stdout.write(str(computeFibonacci(i)) + "\n")
sys.set_int_max_str_digits(100000000)
match WhichOne:
    case 1:
        print(computeFibonacci(N))
    case 2:
        print(originalFibonacci(N))