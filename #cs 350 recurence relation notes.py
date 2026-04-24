#cs 350 recurence relation notes
#4/21/26

def main():
    n = int(input("enter the nth fibb number you are looking for\n"))
    table = [-1 for n in range(0, n+1)]
    table[0] = 0
    table[1] = 1
    ans = fibb_good(n, table)
    print(ans)
    return

def fibb_bad(n): # O(2^n) exponential time
    
    if n <= 1:
        return n

    return fibb_bad(n-1) + fibb_bad(n-2)

def fibb_good(n, table): # O(n) constant time #using memoization

    if table[n] != -1:
        return table[n]

    ans = fibb_good(n-1, table) + fibb_good(n-2, table)
    table[n] = ans
    return ans

if __name__ == "__main__":
    main()