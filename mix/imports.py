import math
from math import sqrt
from math import sqrt as root

def sqrt(x):
    return x * 2

def main():
    print(math.sqrt(25))     # Uses import math
    print(sqrt(100))         # Uses from math import sqrt
    print(root(100))

if __name__ == "__main__":
    main()
