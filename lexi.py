import itertools
def times(i):
    A = list(itertools.permutations('0123456789',10))
    return A[i-1]
    
if __name__ == '__main__':
    print(''.join(times(1000000)))
