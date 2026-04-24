#n choose k 4/23/26

def nchoosek_bad(n,k):
    if k == 1:
        return n
    if n == 1:
        return 1
    if k == n:
        return 1
    
    ans = nchoosek_bad(n-1, k-1) + nchoosek_bad(n-1, k)
    return ans

def main():
    n = 10
    k = 8

    print(nchoosek_bad(n,k))

main()