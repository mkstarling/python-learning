# Collatz sequence with validation.
def collatz():
    p = n
    p = int(p)
    while p > 1:
        
        if p % 2 == 0:
            p = p // 2
            print(p)
        elif p % 2 == 1:
            p = (3 * p) + 1
            print(p)

try:
    n = input('Give me a number')
    n = int(n)
    collatz()
except ValueError:
    print('Error: Please use an integer')
