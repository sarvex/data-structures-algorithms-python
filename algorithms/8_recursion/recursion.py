def find_sum(n):
    return 1 if n==1 else n + find_sum(n-1)

def fib(n):
    # 0,1,1,2,3,5,8 <-- fibonacci numbers
    # --------------
    # 0,1,2,3,4,5,6 <-- index
    return n if n in [0, 1] else fib(n-1) + fib(n-2)

if __name__=='__main__':
    print(find_sum(5))
    print(fib(10))